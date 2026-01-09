# 8단계: 프롬프트 기록과 버전 관리

> 학습일: 2026-01-09
> 출처: Fastcampus Part 8

---

## 1. 프롬프트 관리의 어려움

### 현실 문제

| 문제 | 설명 |
|------|------|
| 수정 내역 관리 | 체계적 관리 어려움 |
| 협업 어려움 | 팀원 간 공유/동기화 |
| 도구 제한 | 프롬프트 전용 도구 부족 |

### 현재 사용되는 도구들

```
Git / VS Code      → 개발자 친화적, 비개발자 어려움
Notion            → 유연함, 버전 관리 수동
Google Spreadsheet → 협업 용이, 구조화 한계
Dropbox           → 파일 공유, 버전 관리 약함
```

---

## 2. 프롬프트 관리 도구

### 2.1 Anthropic Prompt Library

**특징**: Claude 최적화 프롬프트 모음

**카테고리 예시**:
- Cosmic keystrokes: 인터랙티브 게임 생성
- Corporate clairvoyant: 보고서 요약
- Website wizard: 웹사이트 생성
- Excel formula expert: 엑셀 수식 생성
- SQL sorcerer: 자연어 → SQL

**URL**: https://docs.anthropic.com/claude/prompt-library

### 2.2 Claude for Sheets

**특징**: Google Sheets에서 Claude 직접 사용

```
A1: 프롬프트 입력
B1: 모델 선택 (claude-3-haiku-20240307)
C1: =CLAUDE(A1, B1)  → 응답
```

### 2.3 PromptLayer

**특징**: 프롬프트 버전 관리 + 팀 협업 + 평가

```yaml
기능:
  - 버전 히스토리 (Version 1, 2, 3...)
  - 변경 사항 메모
  - A/B 테스트
  - 성능 메트릭 (Latency, Score)
  - 태그 관리

예시:
  프롬프트: sql-buddy/promptlayer-sql
  버전: 12 of 12
  평균 지연: 3.54s
  평균 점수: 67
```

**URL**: https://promptlayer.com

### 2.4 LangSmith

**특징**: LangChain 연동 + 추적 + 평가

```yaml
기능:
  - Prompt Commits (버전 관리)
  - Playground (테스트)
  - 파라미터 설정 (Temperature, Max Tokens 등)
  - 실행 추적

예시:
  템플릿: ChatPromptTemplate
  모델: gpt-4o-mini
  Temperature: 0.4
  Max Output Tokens: 1005
```

**URL**: https://smith.langchain.com

### 2.5 LangChain Hub

**특징**: 커뮤니티 프롬프트 공유

```yaml
인기 프롬프트:
  - hardkothari/prompt-maker: 프롬프트 개선기
  - rlm/rag-prompt: RAG용 프롬프트
  - homanp/superagent: 에이전트용

필터:
  - Use Cases: Agents, Chatbots, QA, Summarization...
  - Type: ChatPromptTemplate, StringPromptTemplate...
  - Language: English, Korean, Chinese...
```

**URL**: https://smith.langchain.com/hub

---

## 3. Semantic Versioning 규칙

### 버전 형식

```
Major.Minor.Patch
  │     │     │
  │     │     └── 버그 수정 (1.0.0 → 1.0.1)
  │     └──────── 마이너 업데이트 (1.0 → 1.1)
  └────────────── 주요 기능 변경 (1.0 → 2.0)
```

### 규칙 상세

#### 규칙 1: 주요 기능 변경 → Major 증가

```yaml
변경 유형:
  - 새로운 기능 추가
  - 프롬프트 메인 구조 변경
  - 토큰 수 대폭 변경

예시: 1.0 → 2.0 → 3.0
```

#### 규칙 2: 마이너 업데이트 → Minor 증가

```yaml
변경 유형:
  - 일부 문장 수정
  - 성능 개선
  - 기존 기능 일부 추가

예시: 1.0 → 1.1 → 1.2
```

#### 규칙 3: 버그 수정 → Patch 증가

```yaml
변경 유형:
  - 오타 수정
  - 출력 깨짐 수정
  - 긴급 문제 해결

예시: 1.0.0 → 1.0.1 → 1.0.2
```

#### 규칙 4: 피드백 반영

```yaml
변경 유형:
  - 사용자 피드백 기반 수정
  - 아랍어 출력 방지
  - 특수 기호 이슈 수정

버전: Minor 또는 Patch (변경 크기에 따라)
```

#### 규칙 5: 주기적 검토

```yaml
기준: 기능의 크기로 결정
예시: 시스템 프롬프트 개선 = Major (1.0 → 2.0)
```

---

## 4. Notion 기반 프롬프트 관리

### 프롬프트 데이터베이스 스키마

| Property | Type | Description |
|----------|------|-------------|
| **Name** | Title | 프롬프트 이름 |
| **Status** | Select | Draft / In Progress / In Review / Done |
| **Version** | Number | 버전 번호 (1.0, 1.1...) |
| **Author** | Person | 작성자 |
| **Created at** | Created Time | 생성 날짜 |
| **Updated at** | Last Edited | 마지막 수정 |
| **Project** | Multi-Select | 관련 프로젝트 |
| **Change Log** | Relation | 변경 로그 연결 |

### 변경 로그 데이터베이스

| Property | Type | Description |
|----------|------|-------------|
| **Name** | Title | 변경 로그 이름 |
| **Prompt** | Relation | 프롬프트 연결 |
| **Version** | Number | 버전 번호 |
| **Change Summary** | Text | 변경 내용 요약 |
| **Changed By** | Person | 변경자 |
| **Changed at** | Created Time | 변경 날짜 |

### 예시 뷰

```
Prompt Portfolio
─────────────────────────────────────────────────
│ 프롬프트 제목    │ Status      │ Version │ Created At │
├─────────────────┼─────────────┼─────────┼────────────┤
│ sample_prompt   │ In progress │ V1.0    │ 2024-08-16 │
│ Prompt Template │ Not started │ -       │ 2024-08-16 │
└─────────────────┴─────────────┴─────────┴────────────┘
```

---

## 5. scrape-hub 적용

### 현재 프롬프트 버전 관리

```yaml
experiments/prompts/
├── ner_validation_v1.yaml  # 1.0.0 - 초기 버전
├── ner_validation_v2.yaml  # 1.1.0 - Few-shot 예시 추가
├── ner_validation_v3.yaml  # 1.2.0 - CoT 적용
├── ner_validation_v4_judge.yaml  # 2.0.0 - LLM-as-Judge (Major)
└── treats_relation_v1.yaml  # 1.0.0 - 새로운 기능
```

### 개선 방안

```yaml
버전 네이밍 개선:
  AS-IS: ner_validation_v1
  TO-BE: ner_validation_1.0.0

문서화 추가:
  - 각 프롬프트 목적/기대 성능
  - 변경 사항 기록
  - 테스트 결과 연결

도구 도입 검토:
  - PromptLayer (팀 협업 필요시)
  - LangSmith (LangChain 사용시)
  - Notion (간단한 관리)
```

### 프롬프트 문서화 템플릿

```yaml
# ner_validation_v3.yaml

metadata:
  name: NER Validation with CoT
  version: 1.2.0
  author: jimin
  created: 2026-01-09
  updated: 2026-01-09
  status: in_review

description: |
  Gazetteer 매칭 엔티티의 유효/무효 판단
  Chain-of-Thought 방식으로 추론 과정 포함

expected_behavior:
  - 단계별 추론 과정 출력
  - 최종 판정 (유효/무효)
  - 판정 근거 제시

change_log:
  - version: 1.0.0
    date: 2026-01-09
    changes: 초기 버전
  - version: 1.1.0
    date: 2026-01-09
    changes: Few-shot 예시 추가
  - version: 1.2.0
    date: 2026-01-09
    changes: CoT 방식 적용

test_results:
  - run: 2026-01-09_171653
    accuracy: 0.85
    model: gpt-4o-mini
```

---

## 6. 버전 관리 체크리스트

### 프롬프트 생성 시

- [ ] 기능 기반 이름 설정
- [ ] 초기 버전 1.0.0 부여
- [ ] 목적과 기대 성능 문서화
- [ ] 테스트 데이터셋 연결

### 프롬프트 수정 시

- [ ] 변경 유형 판단 (Major/Minor/Patch)
- [ ] 버전 번호 증가
- [ ] Change Log 기록
- [ ] 테스트 재실행

### 프롬프트 배포 시

- [ ] Status → Done 변경
- [ ] 최종 테스트 결과 기록
- [ ] 이전 버전 아카이브

---

## 학습 완료 체크

- [x] 프롬프트 관리 도구 이해
- [x] Semantic Versioning 규칙
- [x] Notion 기반 관리 방법
- [ ] PromptLayer 실습
- [ ] LangSmith 실습
- [ ] 기존 프롬프트 버전 관리 적용

---

## 참고 자료

- Fastcampus Part 8: 프롬프트 기록과 버전 관리
- PromptLayer: https://promptlayer.com
- LangSmith: https://smith.langchain.com
- Anthropic Prompt Library: https://docs.anthropic.com/claude/prompt-library
- Semantic Versioning: https://semver.org
