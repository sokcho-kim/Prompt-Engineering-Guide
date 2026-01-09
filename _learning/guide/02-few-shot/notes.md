# 2단계: Few-Shot Prompting

> 학습일: 2026-01-09

## 1. 핵심 개념

**Few-Shot Prompting** = 예시(demonstrations)를 제공해서 모델이 패턴을 학습하게 하는 기법

| 방식 | 예시 수 | 사용 시점 |
|------|---------|----------|
| Zero-Shot | 0개 | 단순한 태스크 |
| One-Shot | 1개 | 빠른 테스트 |
| Few-Shot | 2~5개+ | 패턴 학습 필요할 때 |

---

## 2. 예시: 새로운 단어 학습

```
A "whatpu" is a small, furry animal native to Tanzania.
An example of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.

To do a "farduddle" means to jump up and down really fast.
An example of a sentence that uses the word farduddle is:
```

→ 출력: `When we won the game, we all started to farduddle in celebration.`

**1개 예시만으로** 새로운 단어 사용법 학습!

---

## 3. 중요한 발견 (Min et al. 2022)

| 요소 | 중요도 | 설명 |
|------|--------|------|
| **라벨 공간** | 높음 | 어떤 라벨이 있는지 보여주는 것 자체가 중요 |
| **포맷 일관성** | 높음 | 형식이 일정해야 함 |
| **라벨 정확성** | 낮음 | 놀랍게도 라벨이 틀려도 어느 정도 작동! |

### 실험: 랜덤 라벨

```
This is awesome! // Negative  ← 틀린 라벨
This is bad! // Positive      ← 틀린 라벨
Wow that movie was rad! // Positive
What a horrible show! //
```
→ 출력: `Negative` (정답!)

**교훈**: 라벨이 랜덤이어도 **포맷과 라벨 공간**을 보여주는 것만으로 효과 있음

---

## 4. Few-Shot의 한계

**복잡한 추론 문제에서 실패**:

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
A:
```
→ 출력: `Yes, the odd numbers add up to 107, which is an even number.` ❌ (107은 홀수)

예시를 4개 줘도 **여전히 틀림**

**해결책**: Chain-of-Thought (CoT) - 단계별 추론

---

## 5. Few-Shot 설계 팁

### 5.1 예시 선택 기준
- 각 라벨/카테고리별로 균형있게
- 경계 케이스(애매한 경우) 포함
- 실제 데이터와 유사한 분포

### 5.2 포맷 일관성
```
[좋은 예]
텍스트: "..." → 라벨: A
텍스트: "..." → 라벨: B
텍스트: "..." → 라벨: ?

[나쁜 예]
"..." 는 A
B: "..."
텍스트 "..." →
```

### 5.3 예시 순서
- 다양한 패턴을 번갈아 배치
- 마지막 예시는 질문과 유사한 난이도로

---

## 6. scrape-hub 적용

### 현재 프롬프트 (v1) 분석

| 타입 | 유효 예시 | 무효 예시 |
|------|----------|----------|
| Biomarker | HER2 | er |
| Disease | 고혈압 | 주사 |
| Drug | - | - |
| Procedure | - | - |

**개선점**:
- Drug, Procedure 예시 추가 필요
- 경계 케이스 추가 (예: "ER 양성" - ER은 Biomarker인가 부분문자열인가?)

---

## 7. 다음 단계

- [ ] 프롬프트 v2 작성 (예시 보강)
- [ ] Chain-of-Thought 학습 (복잡한 판단용)

---

## 참고 자료

- `pages/techniques/fewshot.en.mdx`
- Min et al. 2022: https://arxiv.org/abs/2202.12837
- Brown et al. 2020 (GPT-3): https://arxiv.org/abs/2005.14165
