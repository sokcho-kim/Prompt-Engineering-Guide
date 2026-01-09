# Chain-of-Thought (CoT) Prompting 학습 노트

## 핵심 개념

### CoT란?
- **중간 추론 단계**를 포함시켜 복잡한 문제를 해결하는 기법
- "답만 말해"가 아니라 "생각 과정을 보여줘"
- Few-shot과 결합하면 더 강력해짐

### 작동 원리
```
일반 프롬프트: 질문 → 답
CoT 프롬프트: 질문 → 추론과정 → 답
```

## 세 가지 방식

### 1. Few-shot CoT
예시에 추론 과정을 포함시킴

```
Q: 홀수들의 합이 짝수인가? 4, 8, 9, 15, 12, 2, 1
A: 홀수는 (9, 15, 1)이고 합은 25. 25는 홀수. 답: False

Q: 홀수들의 합이 짝수인가? 15, 32, 5, 13, 82, 7, 1
A: [모델이 추론과정과 함께 답변]
```

### 2. Zero-shot CoT
마법의 문구: **"Let's think step by step"** (단계별로 생각해보자)

```
[질문]

단계별로 생각해보자.
```

- 예시 없이도 추론 능력 발휘
- 간단하지만 효과적

### 3. Auto-CoT
- 수동으로 예시 만들기 귀찮음 → 자동화
- 질문 클러스터링 → 대표 질문 선정 → Zero-shot CoT로 추론 생성
- [Amazon 오픈소스](https://github.com/amazon-science/auto-cot)

## scrape-hub 적용 아이디어

### NER 검증에 CoT 적용
기존 (Few-shot만):
```
텍스트: "cancer 관련 연구"
매칭: "er" → Biomarker
판정: 무효
```

CoT 적용:
```
텍스트: "cancer 관련 연구"
매칭: "er" → Biomarker
추론:
1. "er"이 독립 단어인가? → 아니오, "cancer"의 일부
2. 문맥상 ER(에스트로겐 수용체)를 의미하는가? → 아니오
3. 대소문자 확인: "er"은 소문자 → 바이오마커는 보통 대문자
판정: 무효
```

### 장점
- **투명성**: 왜 그렇게 판단했는지 알 수 있음
- **디버깅 용이**: 추론 과정에서 오류 발견 가능
- **신뢰성**: LLM-as-a-Judge에서 판단 근거 제공

### 단점
- 토큰 사용량 증가 (비용 ↑)
- 응답 시간 증가
- max_tokens 늘려야 함

## Entity Linking에 CoT 활용

```
엔티티: "고혈압"
후보 CUI: [C0020538, C0085580, C0155607]

단계별로 생각해보자:
1. 각 CUI의 정의 확인
   - C0020538: Hypertensive disease (고혈압 질환)
   - C0085580: Essential Hypertension (본태성 고혈압)
   - C0155607: Malignant Hypertension (악성 고혈압)

2. 문맥 확인: "본태성 고혈압 환자"

3. 가장 적합한 매칭: C0085580 (본태성 고혈압)
```

## 실험 계획

1. **v3 프롬프트**: CoT 방식으로 NER 검증
2. **비교 실험**: v2 (Few-shot) vs v3 (CoT)
   - 정확도 비교
   - 토큰 사용량 비교
   - 응답 시간 비교

## 핵심 문구 모음

| 한국어 | 영어 |
|--------|------|
| 단계별로 생각해보자 | Let's think step by step |
| 하나씩 분석해보자 | Let's analyze this one by one |
| 먼저 ~를 확인하자 | First, let's check ~ |
| 따라서 | Therefore |
| 결론적으로 | In conclusion |

## 참고 논문
- [Wei et al. (2022)](https://arxiv.org/abs/2201.11903) - CoT 원조
- [Kojima et al. (2022)](https://arxiv.org/abs/2205.11916) - Zero-shot CoT
- [Zhang et al. (2022)](https://arxiv.org/abs/2210.03493) - Auto-CoT
