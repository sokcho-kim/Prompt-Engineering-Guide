"""
Prompt Experiment Runner

프롬프트 실험 실행 및 결과 로깅
"""

import argparse
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional
import os

# .env 파일 로드 (설치 필요: pip install python-dotenv)
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass  # dotenv 없어도 환경변수에서 직접 읽을 수 있음

# OpenAI API (설치 필요: pip install openai)
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: openai 패키지가 설치되지 않았습니다. pip install openai")

BASE_DIR = Path(__file__).parent
PROMPTS_DIR = BASE_DIR / "prompts"
DATASETS_DIR = BASE_DIR / "datasets"
RUNS_DIR = BASE_DIR / "runs"


def load_prompt(name: str) -> dict:
    """프롬프트 YAML 파일 로드"""
    # 버전 포함된 이름 또는 최신 버전 찾기
    if "_v" in name:
        path = PROMPTS_DIR / f"{name}.yaml"
    else:
        # 최신 버전 찾기
        versions = list(PROMPTS_DIR.glob(f"{name}_v*.yaml"))
        if not versions:
            raise FileNotFoundError(f"프롬프트를 찾을 수 없습니다: {name}")
        path = sorted(versions)[-1]

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dataset(name: str) -> list:
    """데이터셋 JSONL 파일 로드"""
    path = DATASETS_DIR / name
    if not path.exists():
        path = DATASETS_DIR / f"{name}.jsonl"

    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return data


def format_prompt(prompt: dict, variables: dict) -> list:
    """변수를 대입하여 메시지 포맷팅"""
    messages = []
    for msg in prompt["messages"]:
        content = msg["content"]
        for key, value in variables.items():
            content = content.replace(f"{{{key}}}", str(value))
        messages.append({"role": msg["role"], "content": content})
    return messages


def extract_verdict(output: str) -> str:
    """CoT 출력에서 판정만 추출"""
    # "판정: 유효" 또는 "판정: 무효" 형식에서 추출
    import re
    match = re.search(r'판정[:\s]*([유무]효)', output)
    if match:
        return match.group(1)
    # 단순 출력인 경우 그대로 반환
    return output.strip()


def run_single(prompt: dict, variables: dict, client: Optional["OpenAI"] = None) -> dict:
    """단일 프롬프트 실행"""
    messages = format_prompt(prompt, variables)
    model_config = prompt.get("model", {})

    if client is None:
        # 드라이런 모드
        return {
            "input": variables,
            "messages": messages,
            "output": "[DRY RUN - API 호출 없음]",
            "model": model_config.get("name", "gpt-4o-mini"),
            "dry_run": True
        }

    # 실제 API 호출
    response = client.chat.completions.create(
        model=model_config.get("name", "gpt-4o-mini"),
        messages=messages,
        temperature=model_config.get("temperature", 0.1),
        max_tokens=model_config.get("max_tokens", 100),
        top_p=model_config.get("top_p", 1)
    )

    return {
        "input": variables,
        "output": response.choices[0].message.content.strip(),
        "model": response.model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
    }


def run_batch(prompt: dict, dataset: list, client: Optional["OpenAI"] = None) -> list:
    """배치 실행"""
    results = []
    total = len(dataset)

    for i, item in enumerate(dataset):
        print(f"  [{i+1}/{total}] {item.get('entity', item)[:30]}...")
        result = run_single(prompt, item, client)
        result["expected"] = item.get("expected")

        # CoT 형식 처리: 판정만 추출하여 비교
        verdict = extract_verdict(result["output"])
        result["verdict"] = verdict  # 추출된 판정 저장
        result["correct"] = verdict == item.get("expected") if "expected" in item else None
        results.append(result)

    return results


def save_run(prompt_name: str, results: list, run_type: str = "test") -> Path:
    """실행 결과 저장"""
    RUNS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{timestamp}_{prompt_name}_{run_type}.json"
    path = RUNS_DIR / filename

    # 통계 계산
    stats = {
        "total": len(results),
        "correct": sum(1 for r in results if r.get("correct") is True),
        "incorrect": sum(1 for r in results if r.get("correct") is False),
        "unknown": sum(1 for r in results if r.get("correct") is None)
    }
    if stats["total"] > 0:
        stats["accuracy"] = stats["correct"] / (stats["correct"] + stats["incorrect"]) if (stats["correct"] + stats["incorrect"]) > 0 else None

    run_data = {
        "prompt_name": prompt_name,
        "run_type": run_type,
        "timestamp": timestamp,
        "stats": stats,
        "results": results
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(run_data, f, ensure_ascii=False, indent=2)

    return path


def compare_runs(run_files: list) -> dict:
    """여러 실행 결과 비교"""
    runs = []
    for f in run_files:
        with open(f, "r", encoding="utf-8") as file:
            runs.append(json.load(file))

    comparison = {
        "runs": [
            {
                "file": str(f),
                "prompt": r["prompt_name"],
                "stats": r["stats"]
            }
            for f, r in zip(run_files, runs)
        ]
    }

    return comparison


def interactive_test(prompt: dict, client: Optional["OpenAI"] = None):
    """대화형 테스트 모드"""
    print("\n=== 대화형 테스트 모드 ===")
    print("변수를 입력하세요. 'q'로 종료.\n")

    variables = {}
    var_defs = prompt.get("variables", [])

    while True:
        # 변수 입력
        for var in var_defs:
            var_name = var if isinstance(var, str) else var.get("name")
            value = input(f"{var_name}: ")
            if value.lower() == 'q':
                return
            variables[var_name] = value

        # 실행
        print("\n실행 중...")
        result = run_single(prompt, variables, client)
        print(f"\n결과: {result['output']}\n")
        print("-" * 40)

        cont = input("계속? (Enter/q): ")
        if cont.lower() == 'q':
            return
        variables = {}


def main():
    parser = argparse.ArgumentParser(description="Prompt Experiment Runner")
    parser.add_argument("--prompt", "-p", help="프롬프트 이름 (예: ner_validation_v1)")
    parser.add_argument("--dataset", "-d", help="데이터셋 파일명")
    parser.add_argument("--test", "-t", action="store_true", help="대화형 테스트 모드")
    parser.add_argument("--dry-run", action="store_true", help="API 호출 없이 테스트")
    parser.add_argument("--compare", "-c", nargs="+", help="실행 결과 비교")
    parser.add_argument("--list", "-l", action="store_true", help="프롬프트 목록")

    args = parser.parse_args()

    # 프롬프트 목록
    if args.list:
        print("\n=== 프롬프트 목록 ===")
        for p in PROMPTS_DIR.glob("*.yaml"):
            with open(p, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            print(f"  - {p.stem}: {data.get('description', '')}")
        return

    # 비교 모드
    if args.compare:
        run_files = [RUNS_DIR / f for f in args.compare]
        result = compare_runs(run_files)
        print("\n=== 실행 결과 비교 ===")
        for r in result["runs"]:
            print(f"\n{r['prompt']}:")
            print(f"  정확도: {r['stats'].get('accuracy', 'N/A')}")
            print(f"  맞음/틀림: {r['stats']['correct']}/{r['stats']['incorrect']}")
        return

    if not args.prompt:
        parser.print_help()
        return

    # 프롬프트 로드
    prompt = load_prompt(args.prompt)
    print(f"\n프롬프트: {prompt['name']} v{prompt['version']}")
    print(f"설명: {prompt.get('description', '')}")

    # OpenAI 클라이언트
    client = None
    if not args.dry_run and HAS_OPENAI:
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            client = OpenAI(api_key=api_key)
        else:
            print("Warning: OPENAI_API_KEY가 설정되지 않았습니다. --dry-run 모드로 실행합니다.")

    # 대화형 테스트
    if args.test:
        interactive_test(prompt, client)
        return

    # 배치 실행
    if args.dataset:
        dataset = load_dataset(args.dataset)
        print(f"데이터셋: {len(dataset)}개 항목")

        results = run_batch(prompt, dataset, client)
        path = save_run(args.prompt, results, "batch")

        # 결과 출력
        stats = {
            "correct": sum(1 for r in results if r.get("correct") is True),
            "incorrect": sum(1 for r in results if r.get("correct") is False),
        }
        total = stats["correct"] + stats["incorrect"]
        accuracy = stats["correct"] / total if total > 0 else 0

        print(f"\n=== 결과 ===")
        print(f"정확도: {accuracy:.1%} ({stats['correct']}/{total})")
        print(f"저장됨: {path}")

        # 틀린 것들 출력
        incorrect = [r for r in results if r.get("correct") is False]
        if incorrect:
            print(f"\n=== 오답 ({len(incorrect)}개) ===")
            for r in incorrect[:5]:
                print(f"  - {r['input'].get('entity')}: 예상={r['expected']}, 실제={r['output']}")


if __name__ == "__main__":
    main()
