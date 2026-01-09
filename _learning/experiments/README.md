# Prompt Experiments

> 프롬프트 실험 관리 시스템 (The Prompt Test 스타일)

## 폴더 구조

```
experiments/
├── prompts/          # 프롬프트 정의 (YAML)
├── runs/             # 실행 결과 로그 (JSON)
├── datasets/         # 테스트 데이터셋
├── runner.py         # 실행 스크립트
└── README.md
```

## 사용법

### 1. 프롬프트 작성

`prompts/` 폴더에 YAML 파일 생성:

```yaml
# prompts/ner_validation_v1.yaml
name: ner_validation
version: 1
description: "Gazetteer 오매칭 필터링"

model:
  name: gpt-4o-mini  # 또는 gpt-5-nano, gpt-5-mini 등
  temperature: 0.1
  max_tokens: 100

messages:
  - role: system
    content: |
      당신은 의료 NER 검증 전문가입니다.
      Gazetteer가 매칭한 엔티티가 유효한지 판단하세요.

  - role: user
    content: |
      ### 유효 예시
      - "HER2 양성" → HER2 = Biomarker (유효)
      - "고혈압 환자" → 고혈압 = Disease (유효)

      ### 무효 예시
      - "...er..." → er = Biomarker (무효, 부분문자열)
      - "주사를 맞다" → 주사 = Disease (무효, 동음이의어)

      ### 검증 대상
      텍스트: {text}
      매칭: "{entity}" → {entity_type}

      ### 출력
      판정:

variables:
  - text
  - entity
  - entity_type
```

### 2. 데이터셋 준비

`datasets/` 폴더에 JSONL 파일:

```jsonl
{"text": "환자는 Ki-67 검사를 받았다", "entity": "Ki-67", "entity_type": "Biomarker", "expected": "유효"}
{"text": "주사를 맞았다", "entity": "주사", "entity_type": "Disease", "expected": "무효"}
```

### 3. 실행

```bash
# 단일 테스트
python runner.py --prompt ner_validation_v1 --test

# 배치 실행
python runner.py --prompt ner_validation_v1 --dataset ner_test.jsonl

# 결과 비교
python runner.py --compare ner_validation_v1 ner_validation_v2
```

### 4. 결과 확인

`runs/` 폴더에 자동 저장:

```
runs/
├── 2026-01-09_ner_validation_v1_test.json
├── 2026-01-09_ner_validation_v1_batch.json
└── ...
```

## 버전 관리

- 프롬프트 수정 시 버전 번호 증가 (v1 → v2)
- Git으로 변경 이력 자동 추적
- runs/에서 버전별 결과 비교 가능

## scrape-hub 연동

scrape-hub의 실제 데이터로 테스트:

```bash
# scrape-hub의 샘플 데이터 가져오기
python runner.py --import-from "C:/Jimin/scrape-hub/project/ner/data/cg_parsed_sampled_1000_labeled.jsonl"
```

## 향후 확장

- [ ] Langfuse 연동 (Trace 로깅)
- [ ] 웹 UI 추가
- [ ] 자동 평가 (LLM-as-a-Judge)
