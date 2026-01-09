# Prompt Engineering 학습 노트

> scrape-hub 프로젝트 적용을 목표로 한 프롬프트 엔지니어링 학습 기록

## 폴더 구조

```
_learning/
├── guide/              # 레포 교육내용 (Prompt-Engineering-Guide 학습)
├── inspirations/       # 외부 영감 (블로그, 사이트 분석 등)
└── experiments/        # 프롬프트 실험 관리
```

## 1. Guide - 레포 교육내용

이 레포(Prompt-Engineering-Guide)의 콘텐츠를 학습하며 정리한 내용

| 폴더 | 내용 | 상태 |
|------|------|------|
| `01-basics/` | 프롬프트 기초 개념 | ✅ 완료 |
| `02-few-shot/` | Few-Shot Prompting | ✅ 완료 |
| `03-chain-of-thought/` | Chain-of-Thought | ✅ 완료 |
| `04-llm-as-judge/` | LLM-as-a-Judge 패턴 | ✅ 완료 |
| `05-practical-design/` | scrape-hub용 실전 프롬프트 | ✅ 완료 |

## 2. Inspirations - 외부 영감

외부 블로그, 사이트, 논문 등에서 영감 받은 내용

| 폴더 | 내용 | 출처 |
|------|------|------|
| `woowahan/` | LLMOps로 확장하는 AI플랫폼 2.0 | 우아한형제들 기술블로그 |
| `from_sujin/` | The Prompt Test 사이트 분석 | test.the-prompt.me |

## 3. Experiments - 프롬프트 실험

The Prompt Test 스타일의 프롬프트 실험 관리 시스템

```
experiments/
├── prompts/      # 프롬프트 정의 (YAML)
├── datasets/     # 테스트 데이터셋
├── runs/         # 실행 결과 로그 (gitignore)
├── .env          # API 키 (gitignore)
└── runner.py     # 실행 스크립트
```

### 프롬프트 버전

#### NER 검증 (ner_validation)

| 버전 | 패턴 | 설명 | max_tokens |
|------|------|------|------------|
| v1 | Few-shot | 기본 예시 4개 | 50 |
| v2 | Few-shot (확장) | 모든 타입별 예시 16개 | 50 |
| v3 | Chain-of-Thought | 추론 과정 포함 | 200 |
| v4 | LLM-as-Judge | 검증 결과 품질 평가 | 300 |

#### TREATS 관계 검증 (treats_relation)

| 버전 | 패턴 | 설명 |
|------|------|------|
| v1 | Few-shot + CoT | Drug-Disease 관계 유효성 검증 |

### 사용법

```bash
cd experiments

# 프롬프트 목록
python runner.py --list

# 드라이런 (API 호출 없음)
python runner.py --prompt ner_validation_v2 --dataset ner_test_v2.jsonl --dry-run

# 대화형 테스트
python runner.py --prompt ner_validation_v3 --test

# 배치 실행 (API 키 필요)
python runner.py --prompt ner_validation_v2 --dataset ner_test_v2.jsonl

# 결과 비교
python runner.py --compare result1.json result2.json
```

### 데이터셋

| 파일 | 내용 | 항목 수 |
|------|------|--------|
| `ner_test_v2.jsonl` | NER 검증 테스트 | 22 |
| `treats_test_v1.jsonl` | TREATS 관계 테스트 | 10 |

## 학습 완료 요약

### 핵심 개념
1. **Few-Shot**: 예시를 통한 패턴 학습
2. **Chain-of-Thought**: 추론 과정 명시화
3. **LLM-as-Judge**: 출력 품질 평가

### scrape-hub 적용
- NER 오매칭 필터링 (Gazetteer false positive)
- TREATS 관계 검증 (Drug-Disease)
- 품질 모니터링 (Judge 패턴)

## 다음 단계

- [ ] API 키 설정 후 실제 테스트
- [ ] v2 vs v3 비교 실험
- [ ] scrape-hub에 프롬프트 통합

## 참고

- 원본 레포: `pages/` 폴더
- scrape-hub 리포트: `c:/jimin/scrape-hub/project/ner/docs/`

---

학습 시작일: 2026-01-09
학습 완료일: 2026-01-09
