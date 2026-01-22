# NAVER D2 - LLMOps를 위한 프롬프트 엔지니어링 도구 개발 경험기 분석

> 분석일: 2026-01-22
> 원본: 박슬기 (네이버 Business Analytics)
> 작성일: 2024.08.12
> 조회수: 11,205

---

## 1. 자료 구성

| 섹션 | 내용 | 핵심 키워드 |
|------|------|------------|
| 개발 배경 | 프롬프트 히스토리 관리 어려움, 반복적 업무 | 버전 관리, 배포 |
| 프롬프트 엔지니어링 도구란 | 필요 기능, 오픈소스 검토 | Agenta, PromptTools |
| 개발한 도구 소개 | 기본 개념, 아키텍처 | Streamlit, LangChain, Ragas, Vitess |
| LLM 애플리케이션 개발 및 평가 과정 | 실습 예시 (텍스트 분류) | 프롬프트 생성, 테스트, 평가 |
| 코드 | 기존 vs 개선된 코드 비교 | Python Library 활용 |

---

## 2. 기존 학습 내용과 비교

### 이미 커버된 내용 (기존 guide/ 및 fastcampus)

| 기존 자료 | 커버 내용 | D2 글 대응 |
|----------|----------|-----------|
| fastcampus Part 6 | 테스트 방법론, 루브릭 | 평가 기능 일부 |
| fastcampus Part 7 | 정량적/정성적 평가 | 평가 메트릭 |
| fastcampus Part 8 | 버전 관리, Semantic Versioning | 프롬프트 버저닝 |
| 04-llm-as-judge | LLM 기반 평가 | Ragas, ARES 메트릭 |

### 새로 배울 내용

| 우선순위 | 주제 | 설명 | 기존 커버리지 |
|---------|------|------|--------------|
| ⭐⭐⭐ | **프롬프트 엔지니어링 도구 구현** | 실제 도구 아키텍처 | 없음 |
| ⭐⭐⭐ | **합성 테스트 데이터 생성** | Milvus, LangChain 활용 Q/A 쌍 생성 | 없음 |
| ⭐⭐ | **평가 메트릭 실전 적용** | Ragas, ARES 실제 사용 사례 | 이론만 있음 |
| ⭐⭐ | **배포 없는 프롬프트 변경** | 프롬프트 분리 아키텍처 | 없음 |

---

## 3. 핵심 개념 정리

### 3.1 프롬프트 엔지니어링 도구의 필요성

#### 문제점 (기존 방식)
```
- 프로젝트 저장소에 프롬프트 버전별 존재
- 프롬프트 변경 시마다 새로 배포 필요
- 이슈에 프롬프트 수정 사항 업데이트 → 히스토리 파악 어려움
- 평가 수치 한눈에 보이지 않음 → 의사결정 지연
```

#### 필요 기능 4가지
1. **프롬프트 테스트**
2. **프롬프트 버저닝 및 배포**
3. **테스트 데이터셋 관리** + 합성 테스트 데이터 생성
4. **평가**

---

### 3.2 도구 아키텍처

```
┌─────────────────────────────────────────────────────┐
│                    Streamlit UI                      │
├─────────────────────────────────────────────────────┤
│              Custom Python Library                   │
│         (LangChain, Ragas 활용)                      │
├─────────────────────────────────────────────────────┤
│                 Vitess (MySQL)                       │
│   ┌──────────┬──────────┬──────────┬──────────┐    │
│   │ 프롬프트  │ 애플리케이션│ 테스트셋  │   평가   │    │
│   └──────────┴──────────┴──────────┴──────────┘    │
└─────────────────────────────────────────────────────┘
```

---

### 3.3 핵심 개념 정의

#### 프롬프트 버전
- 하나의 프롬프트에 **여러 개의 버전** 존재 가능
- **active 버전은 오직 1개**

#### 애플리케이션
```
애플리케이션 = 모델 + 프롬프트(active 버전) + LLM 옵션
```

#### 합성 테스트 데이터
- 시드 문서 기반 Q/A 쌍 자동 생성
- 지원 소스: Milvus Collection, 텍스트 파일, CSV 파일
- 참고: [LangChain Data Generation](https://python.langchain.com/v0.1/docs/use_cases/data_generation/), [Ragas Testset Generation](https://docs.ragas.io/en/latest/concepts/testset_generation.html)

---

### 3.4 평가 메트릭

| 카테고리 | 메트릭 | 설명 |
|---------|--------|------|
| **기본** | Exact Match String | 정확히 일치하는지 |
| **기본** | Embedding Distance | 임베딩 거리 기반 유사도 |
| **Ragas** | FAITHFULNESS | 응답의 충실도 |
| **Ragas** | CONTEXT_PRECISION | 컨텍스트 정확도 |
| **Ragas** | ANSWER_SEMANTIC_SIMILARITY | 응답 의미 유사도 |
| **ARES** | CONTEXT_RELEVANCE | 컨텍스트 관련성 |
| **ARES** | ANSWER_RELEVANCE | 응답 관련성 |
| **ARES** | ANSWER_FAITHFULNESS | 응답 충실도 |

> ARES는 평가용 파인튜닝 LLM 생성 기능 포함

---

### 3.5 코드 비교

#### 기존 방식 (프롬프트 하드코딩)
```python
# 프로젝트에 여러 개의 프롬프트 명시 필요
OLD_SYSTEM_PROMPT = """..."""
NEW_SYSTEM_PROMPT = """..."""

prompt = ChatPromptTemplate.from_messages([...])
chain = chat_prompt_template | model | StrOutputParser()
```

#### 개선된 방식 (도구 활용)
```python
from llm_lib.prompttools.prompt import PromptToolsChatTemplate

prompt = PromptToolsChatTemplate("text-classification")
chat_prompt_template = prompt.get_chat_template()

chain = chat_prompt_template | model | StrOutputParser()
```

#### 이점
- 하나의 프로젝트에서 여러 프롬프트 관리 용이
- 프로젝트 내부에 프롬프트 버전별 생성 불필요
- **프로젝트 배포 없이 프롬프트 변경 가능**

---

## 4. 검토한 오픈소스

| 도구 | URL | 비고 |
|------|-----|------|
| Agenta | https://github.com/Agenta-AI/agenta | 2024.02 기준 미흡 → 현재 개선됨 |
| PromptTools | https://github.com/hegelai/prompttools | 2024.02 기준 미흡 → 현재 개선됨 |
| Ragas | https://docs.ragas.io | 평가 메트릭 라이브러리 |
| ARES | https://github.com/stanford-futuredata/ARES | Stanford, 평가용 LLM 파인튜닝 |

---

## 5. 반영 계획

### 기존 학습 내용과 연계

| 기존 자산 | 연계 방안 |
|----------|----------|
| fastcampus Part 8 (버전 관리) | 실제 구현 사례로 보완 |
| 04-llm-as-judge | Ragas, ARES 실전 적용 사례 추가 |
| experiments/ | 합성 테스트 데이터 생성 기법 적용 |

### 추가 학습 필요 항목

1. **Ragas 라이브러리 실습**
   - Testset Generation
   - 평가 메트릭 활용

2. **ARES 논문 및 라이브러리 검토**
   - 평가용 LLM 파인튜닝 방법론

3. **Streamlit 기반 프롬프트 관리 UI 프로토타입**
   - 버전 관리
   - 테스트/평가 대시보드

---

## 6. 핵심 인사이트

### 프롬프트 관리의 Pain Point
> "프롬프트를 변경하거나 추가할 때마다 새로 배포해야 했습니다"

### 해결책
> **프롬프트를 코드에서 분리** → DB에서 관리 → 배포 없이 변경

### 도구의 가치
> "UI 기반의 편리한 사용성으로 **개발자뿐만 아니라 기획자도 사용 가능**"

### 향후 개선 방향 (네이버)
- 테스트 데이터셋 유연한 확장
- 프롬프트 버전별 평가 결과 피벗 테이블
- 다중 Chaining 지원

---

## 7. 참고 자료

- [LangChain Data Generation](https://python.langchain.com/v0.1/docs/use_cases/data_generation/)
- [Ragas Testset Generation](https://docs.ragas.io/en/latest/concepts/testset_generation.html)
- [Ragas Metrics](https://docs.ragas.io/en/latest/references/metrics.html)
- [ARES - Stanford](https://github.com/stanford-futuredata/ARES)
- [Agenta](https://github.com/Agenta-AI/agenta)
- [PromptTools](https://github.com/hegelai/prompttools)
