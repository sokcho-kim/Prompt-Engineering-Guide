# 1단계: 프롬프트 기초 개념

> 학습일: 2026-01-09

## 1. 프롬프트 엔지니어링이란?

모델이 원하는 작업을 수행하도록 **효과적인 프롬프트를 설계**하는 것

### 예시

```
[약한 프롬프트]
The sky is
→ blue.

[강한 프롬프트]
Complete the sentence: The sky is
→ blue during the day and dark at night.
```

**핵심**: 지시(instruction)가 명확할수록 결과가 좋다

---

## 2. 프롬프트 구성요소 (4가지)

| 요소 | 영어 | 설명 | 필수 여부 |
|------|------|------|----------|
| **지시** | Instruction | 모델이 수행할 구체적인 작업 | 거의 필수 |
| **맥락** | Context | 더 나은 응답을 위한 배경 정보 | 선택 |
| **입력** | Input Data | 처리할 데이터/질문 | 태스크에 따라 |
| **출력 형식** | Output Indicator | 원하는 출력 형태 | 권장 |

### 예시 분석

```
Classify the text into neutral, negative, or positive   ← [Instruction]

Text: I think the food was okay.                        ← [Input Data]

Sentiment:                                               ← [Output Indicator]
```

---

## 3. Zero-Shot vs Few-Shot

| 방식 | 설명 | 언제 사용 |
|------|------|----------|
| **Zero-Shot** | 예시 없이 바로 질문 | 단순한 태스크 |
| **Few-Shot** | 예시를 먼저 보여주고 질문 | 패턴 학습 필요할 때 |

### Few-Shot 예시 (분류)

```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```
→ 출력: `Negative`

---

## 4. 모델 파라미터 (Settings)

| 파라미터 | 설명 | 낮을 때 | 높을 때 |
|----------|------|---------|---------|
| **Temperature** | 출력 다양성 | 결정적, 일관됨 | 창의적, 다양함 |
| **Top P** | 토큰 선택 범위 | 확실한 답변 | 다양한 답변 |
| **Max Length** | 최대 토큰 수 | 짧은 응답 | 긴 응답 |
| **Frequency Penalty** | 반복 패널티 (빈도 비례) | 반복 허용 | 반복 억제 |
| **Presence Penalty** | 반복 패널티 (존재 여부) | 반복 허용 | 반복 억제 |

### 주의사항
- Temperature와 Top P 중 **하나만** 조정
- Frequency/Presence Penalty도 **하나만** 조정

### scrape-hub 적용
- 오매칭 필터링: **Temperature 낮게 (0~0.3)** → 일관된 판단 필요

---

## 5. 프롬프트 설계 팁

### 5.1 간단하게 시작 (Start Simple)
- 복잡한 태스크 → 작은 단위로 분해
- 점진적으로 요소 추가

### 5.2 명확한 지시어
- "Write", "Classify", "Summarize", "Translate" 등
- 구분자로 섹션 분리: `###`

```
### Instruction ###
Translate the text below to Spanish:

Text: "hello!"
```

### 5.3 구체적으로 (Specificity)
```
[모호함] Keep the explanation short
[구체적] Use 2-3 sentences to explain to a high school student
```

### 5.4 "하지 마라"보다 "해라"
```
[나쁨] DO NOT ASK FOR INTERESTS.
[좋음] Recommend from top trending movies only.
```

---

## 6. scrape-hub 적용 포인트

오매칭 필터링 프롬프트 구조:

```
[Instruction]
Gazetteer 매칭 엔티티의 유효/무효 판단

[Context]
유효/무효 예시 (Few-Shot)

[Input Data]
검증할 텍스트 + 매칭 결과

[Output Indicator]
판정 (유효/무효):
```

설계 팁 적용:
- Temperature: 0.1 (일관된 판단)
- 구분자 `###` 사용
- 구체적 기준 명시 (부분 문자열, 동음이의어 등)
- "무효로 판단하지 마라" ❌ → "유효 조건을 만족할 때만 유효로 판단하라" ✅

---

## 학습 완료 체크

- [x] basics.en.mdx - 프롬프팅 기본
- [x] elements.en.mdx - 구성요소
- [x] settings.en.mdx - 파라미터
- [x] tips.en.mdx - 설계 팁
