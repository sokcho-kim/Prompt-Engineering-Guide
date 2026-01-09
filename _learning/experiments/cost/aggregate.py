"""
비용 집계 스크립트

runs/ 폴더의 실행 결과에서 비용을 계산하고 일별 로그 생성
"""

import argparse
import json
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path(__file__).parent
RUNS_DIR = BASE_DIR.parent / "runs"
DAILY_DIR = BASE_DIR / "daily"
PRICING_FILE = BASE_DIR / "pricing.yaml"


def load_pricing() -> dict:
    """가격 정보 로드"""
    with open(PRICING_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_model_price(model_name: str, pricing: dict) -> dict:
    """모델 가격 조회 (per token)"""
    models = pricing.get("models", {})

    # 정확한 매칭
    if model_name in models:
        p = models[model_name]
        return {"input": p["input"] / 1_000_000, "output": p["output"] / 1_000_000}

    # 부분 매칭 (gpt-4o-mini-2024-07-18 -> gpt-4o-mini)
    for key in models:
        if key in model_name:
            p = models[key]
            return {"input": p["input"] / 1_000_000, "output": p["output"] / 1_000_000}

    # 기본값
    default = pricing.get("default", "gpt-4o-mini")
    p = models.get(default, {"input": 0.15, "output": 0.60})
    return {"input": p["input"] / 1_000_000, "output": p["output"] / 1_000_000}


def calculate_run_cost(run_file: Path, pricing: dict) -> dict:
    """단일 실행 결과의 비용 계산"""
    with open(run_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    prompt_tokens = 0
    completion_tokens = 0
    model_name = None

    for result in data.get("results", []):
        usage = result.get("usage", {})
        prompt_tokens += usage.get("prompt_tokens", 0)
        completion_tokens += usage.get("completion_tokens", 0)
        if not model_name:
            model_name = result.get("model", "gpt-4o-mini")

    price = get_model_price(model_name, pricing)
    cost = prompt_tokens * price["input"] + completion_tokens * price["output"]

    return {
        "file": run_file.name,
        "prompt": data.get("prompt_name", "unknown"),
        "timestamp": data.get("timestamp", ""),
        "items": data.get("stats", {}).get("total", 0),
        "model": model_name,
        "tokens": {
            "prompt": prompt_tokens,
            "completion": completion_tokens,
            "total": prompt_tokens + completion_tokens
        },
        "cost_usd": round(cost, 6)
    }


def aggregate_by_date(date_str: str = None) -> dict:
    """특정 날짜의 비용 집계"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    pricing = load_pricing()
    runs = []
    total_cost = 0
    total_tokens = {"prompt": 0, "completion": 0, "total": 0}

    for run_file in RUNS_DIR.glob("*.json"):
        # 파일명에서 날짜 추출 (2026-01-09_171612_...)
        file_date = run_file.name[:10]
        if file_date == date_str:
            run_cost = calculate_run_cost(run_file, pricing)
            runs.append(run_cost)
            total_cost += run_cost["cost_usd"]
            for key in total_tokens:
                total_tokens[key] += run_cost["tokens"][key]

    return {
        "date": date_str,
        "runs": runs,
        "summary": {
            "run_count": len(runs),
            "total_tokens": total_tokens,
            "total_cost_usd": round(total_cost, 6)
        }
    }


def aggregate_by_month(month_str: str) -> dict:
    """월간 비용 집계"""
    pricing = load_pricing()
    daily_data = defaultdict(lambda: {"runs": [], "cost": 0})

    for run_file in RUNS_DIR.glob("*.json"):
        file_date = run_file.name[:10]
        if file_date.startswith(month_str):
            run_cost = calculate_run_cost(run_file, pricing)
            daily_data[file_date]["runs"].append(run_cost)
            daily_data[file_date]["cost"] += run_cost["cost_usd"]

    daily_summary = [
        {"date": date, "runs": len(data["runs"]), "cost_usd": round(data["cost"], 6)}
        for date, data in sorted(daily_data.items())
    ]

    total_cost = sum(d["cost_usd"] for d in daily_summary)

    return {
        "month": month_str,
        "daily": daily_summary,
        "summary": {
            "days_active": len(daily_summary),
            "total_runs": sum(d["runs"] for d in daily_summary),
            "total_cost_usd": round(total_cost, 6)
        }
    }


def save_daily_log(date_str: str = None):
    """일별 로그 저장"""
    DAILY_DIR.mkdir(exist_ok=True)

    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    data = aggregate_by_date(date_str)

    if data["runs"]:
        output_file = DAILY_DIR / f"{date_str}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"저장됨: {output_file}")
        return output_file
    else:
        print(f"{date_str}: 실행 기록 없음")
        return None


def print_summary(data: dict):
    """요약 출력"""
    if "month" in data:
        print(f"\n=== {data['month']} 월간 비용 ===")
        for d in data["daily"]:
            print(f"  {d['date']}: {d['runs']}건, ${d['cost_usd']:.6f}")
        print(f"\n총 {data['summary']['days_active']}일, "
              f"{data['summary']['total_runs']}건, "
              f"${data['summary']['total_cost_usd']:.6f}")
    else:
        print(f"\n=== {data['date']} 일별 비용 ===")
        for run in data["runs"]:
            print(f"  {run['prompt']}: {run['items']}건, "
                  f"{run['tokens']['total']:,} tokens, ${run['cost_usd']:.6f}")
        print(f"\n총 {data['summary']['run_count']}건, "
              f"{data['summary']['total_tokens']['total']:,} tokens, "
              f"${data['summary']['total_cost_usd']:.6f}")


def main():
    parser = argparse.ArgumentParser(description="비용 집계")
    parser.add_argument("--date", "-d", help="집계할 날짜 (YYYY-MM-DD)")
    parser.add_argument("--month", "-m", help="집계할 월 (YYYY-MM)")
    parser.add_argument("--save", "-s", action="store_true", help="일별 로그 저장")
    parser.add_argument("--all", "-a", action="store_true", help="전체 기간 집계")

    args = parser.parse_args()

    if args.month:
        data = aggregate_by_month(args.month)
        print_summary(data)
    elif args.all:
        # 전체 기간
        pricing = load_pricing()
        total_cost = 0
        for run_file in sorted(RUNS_DIR.glob("*.json")):
            run_cost = calculate_run_cost(run_file, pricing)
            print(f"{run_cost['timestamp']} | {run_cost['prompt']}: "
                  f"${run_cost['cost_usd']:.6f}")
            total_cost += run_cost["cost_usd"]
        print(f"\n전체 비용: ${total_cost:.6f}")
    else:
        data = aggregate_by_date(args.date)
        print_summary(data)

        if args.save:
            save_daily_log(args.date)


if __name__ == "__main__":
    main()
