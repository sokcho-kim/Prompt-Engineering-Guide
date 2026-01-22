# 우아한형제들 - AI플랫폼 2.0 LLMOps 분석

> 분석일: 2026-01-22
> 원문: https://techblog.woowahan.com/22839/
> 작성자: 이준수 (우아한형제들 AI플랫폼팀)
> 작성일: 2025.09.29

---

## 1. 자료 구성

| 섹션 | 내용 | 핵심 키워드 |
|------|------|------------|
| 배경 | MLOps → LLMOps 전환, AI 프로덕트 확산 | AI플랫폼 1.0 → 2.0 |
| 운영 중 마주한 8가지 문제 | 실제 운영 Pain Points | Provider 복잡성, 프롬프트 관리, 안정성 |
| GenAI 컴포넌트 | Studio, SDK, API Gateway, Labs | Langfuse, LiteLLM |
| 8가지 문제 해결 사례 | 실제 해결 방법 | 정책화, 표준화, 자동화 |
| 결과 | 정량적 성과 | 사용자 50%↑, 프로젝트 69%↑ |

---

## 2. 기존 학습 내용과 비교

### 이미 커버된 내용

| 기존 자료 | 커버 내용 | 우아한 글 대응 |
|----------|----------|---------------|
| naver_d2 | 프롬프트 엔지니어링 도구 개발 | GenAI Studio, Labs |
| fastcampus Part 6 | 테스트 방법론 | Evaluation, Golden Dataset |
| fastcampus Part 8 | 버전 관리 | 프롬프트 버저닝, Langfuse |
| 04-llm-as-judge | LLM 기반 평가 | LLM-as-a-Judge |

### 새로 배울 내용

| 우선순위 | 주제 | 설명 | 기존 커버리지 |
|---------|------|------|--------------|
| ⭐⭐⭐ | **엔터프라이즈 LLMOps 아키텍처** | 4개 컴포넌트 통합 설계 | 없음 |
| ⭐⭐⭐ | **운영 8가지 문제 + 해결책** | 실제 장애/비용/보안 사례 | 없음 |
| ⭐⭐⭐ | **Langfuse 도입 사례** | 솔루션 선택 과정, Self-hosted | 없음 |
| ⭐⭐ | **Observability 파이프라인** | ClickHouse + Superset 설계 | 없음 |
| ⭐⭐ | **크레덴셜 발급 정책** | PoC vs 정식 분리 | 없음 |
| ⭐ | **Context Engineering** | 최신 트렌드 언급 | 없음 |

---

## 3. 핵심 개념 정리

### 3.1 운영 중 마주한 8가지 문제

| # | 문제 | 상세 | 해결 컴포넌트 |
|---|------|------|--------------|
| 1 | **멀티 Provider 복잡성** | Azure, Gemini, Bedrock API 스펙 상이 | API Gateway, SDK |
| 2 | **프롬프트 관리 한계** | 코드/시트/파일 분산, 버전 추적 불가 | Studio |
| 3 | **안정성 문제** | 응답 지연, 장애, 정책 차단 | SDK, Studio |
| 4 | **비용·리소스 관리 어려움** | 프로젝트별 비용 가시성 부족 | Studio, Superset |
| 5 | **실험 관리 부재** | 결과 공유/재현성 부족 | Labs, Studio |
| 6 | **새로운 고객층** | PM/기획자도 LLM 활용 희망 | Labs, Studio, SDK |
| 7 | **크레덴셜 발급 허들** | 보안 검토로 PoC 지연 | 거버넌스 정책 |
| 8 | **보안·개인정보 보호** | PII 외부 전송 위험 | SDK, Studio |

---

### 3.2 GenAI 컴포넌트 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                      GenAI Platform 2.0                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│   │  GenAI Labs  │◄──►│ GenAI Studio │◄──►│  GenAI SDK   │  │
│   │  (실험/평가)  │    │  (Langfuse)  │    │  (LiteLLM)   │  │
│   └──────────────┘    └──────┬───────┘    └──────┬───────┘  │
│                              │                    │          │
│                              ▼                    ▼          │
│                    ┌─────────────────────────────────┐       │
│                    │      GenAI API Gateway          │       │
│                    │   (OpenAI-Compatible API)       │       │
│                    └─────────────────────────────────┘       │
│                                    │                         │
├────────────────────────────────────┼─────────────────────────┤
│                                    ▼                         │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│   │  Azure   │  │  Google  │  │   AWS    │  │  기타    │    │
│   │ OpenAI   │  │  Gemini  │  │ Bedrock  │  │  LLM     │    │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.3 4개 컴포넌트 상세

#### GenAI Studio (Langfuse 기반)

| 기능 | 설명 |
|------|------|
| **프롬프트 관리** | 버전별 저장, 변경 이력 추적, 롤백 |
| **Observability** | 요청 단위 Trace, 지연/비용/오류 모니터링 |
| **크레덴셜 관리** | 중앙 집중 API Key 관리 |
| **Evaluation** | Golden/Evaluation Dataset 기반 평가 |

##### Langfuse 선택 이유

| 후보 | 탈락 이유 |
|------|----------|
| MLflow | LLM 특화 기능 부족, 프롬프트 기능 제한 |
| PromptFlow | Azure 종속, 독립 웹 UI 없음 |
| LangSmith | LangChain 중심 설계, 범용성 제한 |
| Agenta, Opik | 엔터프라이즈 성숙도 부족 |
| Pezzo | 운영 모니터링/피드백 기능 없음 |
| OpenPrompt | 로깅/버전관리/권한 체계 부족 |

**Langfuse 강점:**
- 프롬프트 관리 & 버전 제어
- Trace 기반 Observability
- 토큰/비용 대시보드
- A/B 테스트, 사용자 피드백
- 온프레미스(Self-hosted) 지원

---

#### GenAI SDK

| 기능 | 설명 |
|------|------|
| **단일화된 인터페이스** | LiteLLM 기반, 모델명만 변경하면 호출 |
| **라우팅/Fallback** | 리전 장애 시 자동 전환 |
| **크레덴셜 단순화** | Studio API Key 하나로 모든 모델 호출 |
| **Context Engineering** | Studio 프롬프트 불러와 동적 컨텍스트 주입 |

---

#### GenAI API Gateway

| 기능 | 설명 |
|------|------|
| **OpenAI-Compatible API** | OpenWebUI, LangChain, LlamaIndex 즉시 연동 |
| **SDK 기능 내장** | 라우팅, Fallback, Trace, 크레덴셜 관리 |
| **Non-Python 지원** | REST API로 모든 환경에서 호출 |

---

#### GenAI Labs

| 기능 | 설명 |
|------|------|
| **단일 테스트** | 프롬프트 초기 개발, 빠른 검증 |
| **배치 실험** | Golden Dataset 기반 성능 평가 |
| **데이터셋 업로드** | 입력/출력 매핑 후 Studio 업로드 |
| **Custom Evaluation** | 코드 레벨 평가 함수 정의 |
| **Context Engineering** | Prompt Variables 동적 주입 |

##### Labs 직접 개발 이유
- Studio UI만으로 Context Engineering 어려움
- Langfuse Playground 멀티모달 미지원
- 신기능 빠른 검토 필요

---

### 3.4 Observability 파이프라인

```
┌─────────────────────────────────────────────────────────────┐
│                    3계층 Observability                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [Application Layer]                                         │
│       Studio → LLM 응답 수집                                 │
│                                                              │
│  [Collection Layer]                                          │
│       Traces → ClickHouse                                    │
│       Metrics → Prometheus                                   │
│                                                              │
│  [Analysis Layer]                                            │
│       ClickHouse + Superset → 비용/성능 대시보드              │
│       Prometheus + Grafana → 시스템 모니터링                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**기존 Grafana 한계:**
- Latency 원인 분석 어려움
- Average Response Time 변동폭 큼
- Client Timeout 이슈 파악 불가

**Langfuse 도입 후:**
- 모델별 응답 속도 Percentile 분석
- Traces로 병목 지점 명확히 확인
- 프로젝트별 비용 모니터링 + 알림

---

### 3.5 크레덴셜 발급 정책

```
┌────────────────────────────────────────────────────────────┐
│                    크레덴셜 발급 프로세스                     │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  [기존 프로세스]                                             │
│     아이디어 → 보안 검토 → 비용 승인 → 키 발급 → 실험 시작    │
│                    (병목 구간)                               │
│                                                             │
│  [개선된 프로세스]                                            │
│     PoC 단계: 보안 검토 → 공용 API Key로 자유롭게 실험        │
│     정식 단계: 필요 모델만 정식 API Key 발급                  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

### 3.6 LLMOps 워크플로우

| 단계 | 컴포넌트 | 활동 |
|------|---------|------|
| **개발** | Studio + SDK + Gateway | 프롬프트 저장, SDK로 호출, Trace 추적 |
| **연구** | Studio + SDK + Labs | 실험 수행, 자동 평가, 결과 기록 |
| **운영** | Studio + SDK | A/B 테스트, 배포, Observability |

---

## 4. 8가지 문제 해결 사례 요약

| 문제 | 해결 전략 |
|------|----------|
| 멀티 Provider | SDK 단일 인터페이스 + Gateway OpenAI-Compatible |
| 프롬프트 관리 | Studio 중앙 관리, 버전/Trace 추적 |
| 안정성 | SDK Retry/Fallback + PII 필터링 |
| 비용 관리 | Studio 토큰 기록 + Superset 대시보드 + 알림 |
| 실험 관리 | Labs Golden/Evaluation Dataset + Studio 저장 |
| 새 사용자층 | Labs/Studio UI로 비개발자 셀프 서비스 |
| 크레덴셜 허들 | PoC 공용 키 / 정식 분리 발급 정책 |
| 보안/PII | SDK PII 탐지 모듈 + Studio 정책화 |

---

## 5. 정량적 결과

| 지표 | 수치 | 비고 |
|------|------|------|
| **사용자 성장** | +50% (YoY 2025) | LLMOps 도입 후 |
| **프로젝트 성장** | +69% (YoY 2025) | 개발 중 + 배포 완료 |
| **비개발 직군 비중** | 38.3% (2025) | 2022-2024 DS/MLE 중심 → 확대 |

> "LLMOps는 단순히 운영 자동화를 넘어 **전사적인 생산성 레버리지**로 자리 잡았습니다"

---

## 6. 핵심 인사이트

### 운영의 Pain Point
> "프로젝트 초반부터 불필요한 리소스가 소모... 서비스 수가 늘어남에 따라 코드와 키 관리 복잡도는 계속 증가"

### LLM 운영의 특수성
> "LLM API는 기존 ML 서빙과 달리 **장기 지연과 불확실성을 전제로** 운영 전략을 세워야 한다"

### 플랫폼의 가치
> "프로덕트 → 플랫폼 → 다시 프로덕트"로 이어지는 **선순환 구조**

### 미래 방향
- **Context Engineering** 중요성 증가
- **Agentic Design Patterns** 도입
- Langflow, n8n 같은 시각적 워크플로우 툴 검토

---

## 7. 반영 계획

### 기존 학습 내용과 연계

| 기존 자산 | 연계 방안 |
|----------|----------|
| naver_d2 | 소규모 도구 → 엔터프라이즈 확장 사례로 비교 |
| fastcampus Part 8 | Langfuse 실제 도입 사례로 보완 |
| 04-llm-as-judge | LLM-as-a-Judge 운영 환경 적용 사례 |

### 추가 학습 필요 항목

1. **Langfuse 실습**
   - Self-hosted 설치
   - ClickHouse + Superset 연동

2. **LiteLLM 학습**
   - 멀티 Provider 통합
   - Fallback/라우팅 설정

3. **Observability 설계**
   - Trace 수집 파이프라인
   - 비용 모니터링 대시보드

---

## 8. NAVER D2 vs 우아한형제들 비교

| 항목 | NAVER D2 | 우아한형제들 |
|------|----------|-------------|
| **규모** | 팀 단위 도구 | 전사 플랫폼 |
| **솔루션** | 자체 개발 (Streamlit) | Langfuse 도입 + 커스텀 |
| **핵심 기능** | 프롬프트 버저닝, 평가 | 4개 컴포넌트 통합 |
| **평가** | Ragas, ARES | LLM-as-a-Judge, Custom |
| **Observability** | 기본 | ClickHouse + Superset |
| **사용자** | 개발자 | 개발자 + PM/기획자 |

**공통점:**
- 프롬프트 히스토리 관리 문제 해결
- 버전 관리 + 평가 기능 필수
- 배포 없이 프롬프트 변경

**차이점:**
- 우아한: 엔터프라이즈급 Observability, 멀티 Provider, 거버넌스
- 네이버: 팀 단위 빠른 구축, 합성 테스트 데이터 생성

---

## 9. 참고 자료

### 우아한형제들 기술 블로그
- [배민 앱에도 AI 서비스가? AI 서비스와 MLOps 도입기](https://techblog.woowahan.com/11582/)
- [안정적인 AI 서빙 시스템 + 자동화](https://techblog.woowahan.com/19548/)
- [GPT를 활용한 카탈로그 아이템 생성](https://techblog.woowahan.com/21294/)

### Langfuse
- [공식 문서](https://langfuse.com/docs/prompt-management/overview)
- [Infrastructure Evolution](https://langfuse.com/blog/2024-12-langfuse-v3-infrastructure-evolution)
- [Langfuse vs LangSmith](https://langfuse.com/faq/all/langsmith-alternative)
- [Observability in Multi-step LLM Systems](https://langfuse.com/blog/2024-10-observability-in-multi-step-llm-systems)

### 기타
- [Context Engineering Survey (Mei et al., 2025)](https://arxiv.org/abs/2507.13334)
- [AWS Bedrock Inference Profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)
- [McKinsey: PoC 이후 운영 확장 어려움](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/overcoming-two-issues-that-are-sinking-gen-ai-programs)
