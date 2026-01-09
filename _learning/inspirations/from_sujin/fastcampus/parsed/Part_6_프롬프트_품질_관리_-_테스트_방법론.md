# Part 6. 프롬프트 품질 관리 - 테스트 방법론

> 파싱 일시: 2026-01-09 17:59:10
> 총 페이지: 40
> 텍스트 추출 성공: 31
> OCR 필요: 9

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering
Chapter 03. 프롬프트 품질 관리: 테스트 방법론

---

## 페이지 2

Prompt Engineering A to Z
Chapter 01. LLM 차별화의 열쇠
01. 프롬프트 엔지니어 핵심 역량 및 주요 업무
02. 프롬프트 엔지니어링 학습해야 하는 이유
Chapter 02. 프롬프트의 이해
Part 01. 프롬프트유형탐구
Part 02. 효과적인프롬프트분석기법
Ø Chapter 03. 실무 프롬프트 엔지니어링 A to Z
Part 03 . 목적 중심의 프롬프트 기획 전략
Part 04. 프롬프트 제작의 기초: 핵심 원리와 방법론
Chapter 04. 프롬프트 엔지니어링 파이널 프로젝트
Part 05. 프롬프트 제작 심화: 고급 기술과 최적화
Part 06. 프롬프트 품질 관리: 테스트 방법론 Part 09. 생성형 AI 프롬프트 프로젝트
Part 07. 프롬프트 성능 평가
Chapter 05. 프롬프트 엔지니어링 현재와 미래
Part 08. 프롬프트 기록과 버전 관리

---

## 페이지 3

Prompt EngineeringA to Z
프롬프트 테스트의 필요성과 가치
효과적인 프롬프트 테스트 기준 수립
프롬프트 엔지니어링 A to Z
프롬프트 테스트 방법론 개요
Chapter 03
프롬프트 테스트의 깊이 더하기: 질적 분석을 통한 프롬프트
Part 06. 프롬프트 품질 관리: 테스트
테스트 방법
방법론
프롬프트 성능의 수치화: 정량적 접근법
프롬프트 테스트 실습 (cid:13273)1(cid:13274): 구조 및 내용 최적화 기법
프롬프트 테스트 실습 (cid:13273)2(cid:13274): 다양한 LLM간 프롬프트 성능 비교

---

## 페이지 4

Course Objectives & Learning Outcomes
학습 목표
01
ü 프롬프트 테스트의 필요성 및 가치를 이해한다.
02
효과적인 프롬프트 평가 기준을 수립할 수 있다.
03
프롬프트 테스트 방법론을 개괄적으로 이해한다.
04
프롬프트 테스트를 통해 다양한 LLM의 성능을 비교할 수 있다.

---

## 페이지 5

Course Objectives & Learning Outcomes
기대 학습 성과
01
ü 프롬프트 평가 기준을 체계적으로 적용할 수 있다.
02
프롬프트 성능을 수치화하고 정량적 분석을 수행할 수 있다.
03
다양한 테스트 실습을 통해 구조 최적화와 성능 비교를 할 수 있다.

---

## 페이지 6 (OCR)

Chapter 3 
01. 프롬프트 테스트의 필요성과 가치 
Fast campus

---

## 페이지 7

Chapter 03. 프롬프트픔질관리:테스트방법론
Iterative process for prompt development
Reference: https://techcommunity.microsoft.com/t5/ai-machine-learning-
blog/harness-the-power-of-large-language-models-with-azure-
machine/ba-p/3828459

---

## 페이지 8

Chapter 03. 프롬프트픔질관리:테스트방법론
Ø 프롬프트 테스트의 어려움
프롬프트 = 텍스트
일관성과
품질 안정성
프롬프트 = 정답 (X)
LLM의 빠른 발전 속도

---

## 페이지 9 (OCR)

Chapter 3 
02. 효과적인 프롬프트 테스트 기준 수립 
Fast campus

---

## 페이지 10

Chapter 03. 프롬프트픔질관리:테스트방법론
Ø 프롬프트 테스트 아홉 가지 규칙
1. 프롬프트는 최소 두 가지 버전으로 작성
2. 프롬프트 버전은 기능 이름으로 정하기 (cid:13273) (cid:13274)
systemprompt(cid:13255)v1, productrecommender(cid:13255)v2
3. 프롬프트 이름은 기능 확장이나 세부 카테고리를 반영하여 제작
FinancialAnalysis(cid:13255)Revenue(cid:13255)v1 (cid:14097) FinanacialAnalysis(cid:13255)Expense(cid:13255)v1
4. 각 버전의 프롬프트 목표와 기대 성능을 문서화
5. 프롬프트 테스트에 작위적인 문장은 사용하지 않기 (cid:13273)실제 사용자 발화 데이터, 실제 데이터(cid:13274)
6. 테스트 데이터셋 사용
7. 프롬프트는 같은 테스트 도구 최소 열 번 이상 생성(cid:13273)OpenAI Playground(cid:13274)
8. 최소 세 명의 작업 관계자가 참여.
9. 다양한 언어 모델 버전을 사용하여 테스트 하기

---

## 페이지 11 (OCR)

Chapter 03. 프롬프트 픔질관리: 테스트 방법론 
프롬프트 문서화 예시 
프롬프트 원문 
# [Introduction] 
You have a mind and your role is to generate possible three questions auser may 
want to ask next based on {{$User input: 제주도 감귤 초콜릿은 얼마야?}} The questio ns 
must be from the perspective of me, the user askingyou a question. 
## [Response temp late] Predicted user question as followed: 
1. High certainty 
2. Moderate certainty, yet intriguing 
3. Low certainty, but strong potential for user engagement 
### [Ending] 
Answer in half speech form of Korean (반말) · 
Don , t be over five words Only provide three questions. 
mode l=GPT3-5-turbo 
max_tokens=200 
temperatures=0.5 
frequency_penalty=1 
presence_penalty=1 
Fast campus

---

## 페이지 12 (OCR)

Chapter 03. 프롬프트 품질관리: 테스트 방법론 
프롬프트 유형 Type C 
제목 Question_Generator 
설명 사용자가 후속 질문으로 자주 물을 것 같은 질문을 생성하는 프롬프트 
기대 결과 사용자 질문과 관련된 세 개의 답변이 나와야 한다. 
- 세 개의 내용이 서로 겹치지 않아야 한다. 
- 한국어로 답변이 나와야 한다. 
- 답변의 길이가 너무 길어서는 안 된다. 
- 글자 깨짐이나 특수 기호가 나오면 안 된다. 
- 여러 턴이 이어지더라도 주제에 대한 프롬프트가 잘 나와야 한다. 
작업 과정 설계 중 이슈 기록: 
· 설계한 질문 생성기를 사용자가 몇 회까지 사용할 수 있을지에 대한 데이터가 필요하다. 
이는 언어 모델의 최대 토큰 수를 초과하면 질문 생성 기능이 작동하지 않기 때문이다. 이 
전 대화 내용을 기억하도록 프롬프트를 설계해야 하며, 사용자가 갑자기 다른 주제로 전환 
했다가 다시 이전 주제로 돌아가도 주제에 따라 질문을 생성할 수 있어야 한다. 
· 질문 생성기에 사용된 프롬프트 토큰은 최적화하는 것이 좋다. 사용자의 입력 토큰이 증가 
하기 때문이다. 실시간 검색을 기반으로 하는 질문, 예를 들어 날씨, 환율, 현재 지역과 같 
은 주제에 대한 후속 질문은 사용성을 저해할 수 있다. 사용자가 해당 질문을 클릭했을 때 
언어 모델이 올바른 답변을 제공하지 못하기 때문이다. 
기타메모 질문 생성기를 활용하여 기업 광고를 해 볼 수 있지 않을까? 
· 질문 생성기를 활용하여 사용자 개인 맞춤형 제작을 할 수 있다. 사용자를 알아봐 주는 프 
롬프트를 만들면 사용자가 좋아할 것이다. 
Fast campus

---

## 페이지 13

Chapter 03. 프롬프트픔질관리:테스트방법론
테스트 데이터 셋
o 대표적이고 빈번하게 사용되는 실제 사용자 발화 데이터
o 다양하고 포괄적인 내용의 발화 데이터
o 예상치 못한 사항이 포함된 데이터
o 사용자 오류 패턴이 있는 데이터
o LLM의 한계가 드러난 발화 데이터

---

## 페이지 14 (OCR)

Chapter 3 
03. 프롬프트 테스트 방법론 개요 
Fast campus

---

## 페이지 15

Chapter 03. 프롬프트픔질관리:테스트방법론
Ø 프롬프트 테스트 단계 업무 절차
테스트 결과 정리
테스트 기준 마련 프롬프트 품질 분석
최종 프롬프트 선별 사용자 피드백 및 이슈 관리
프롬프트 언어 분석 지속적인 결과 개선

---

## 페이지 16

Chapter 03. 프롬프트픔질관리:테스트방법론
Ø 프롬프트 테스트 두 가지 방법
정성적 방법 정량적 방법

---

## 페이지 17

Chapter 03. 프롬프트픔질관리:테스트방법론
Test Tool: The Prompt Testbed
Sign-up: https://the-prompt-playground.vercel.app/

---

## 페이지 18

Chapter 3
04. 프롬프트 테스트 깊이 더하기:
질적 분석을 통한 프롬프트 테스트 방법

---

## 페이지 19

Chapter 03. 프롬프트픔질관리:테스트방법론
질적 분석. 프롬프트 성능 고도화/ 프롬프트 분석
1. 목적 확인
2. 구조 분석
3. 효율성 평가

---

## 페이지 20

Chapter 03. 프롬프트픔질관리:테스트방법론
1. 목적 확인 &구조 분석 You have a mind, and your role is to
generate possible three questions a user
may want to ask next based on (cid:13275)(cid:13275)(cid:13900)User
input: 개발자로 살아남으려면??(cid:13276)(cid:13276)
(1) 핵심 단어와 구문 추출
The questions must be from the
모델이 응답을 생성할 때
perspective of me, the user asking you a
중요한 역할 적절한 키워드 question.
## (cid:13277)Response template(cid:13278)
(2) 문장 구성 분석
Predicted user question as followed:
q 프롬프트가 단순한지, 복잡한지 (cid:13247)High certainty
(cid:13247) Moderate certainty, yet intriguing
q 명령어인지, 질문인지
(cid:13247) Low certainty, but strong potential for
q 정보의 흐름이 논리적인지
user engagement
### (cid:13277)Ending(cid:13278)
Always answer in half(cid:13247)speech form of
일반적 -> 구체적
Korean(cid:13273)반말(cid:13274). Don(cid:13364)t be over five words.
구조화
Only provide three questions.

---

## 페이지 21

Chapter 03. 프롬프트픔질관리:테스트방법론
2. 구조 분석
Type 1 Type 2
You have a mind, and your role is to
You have a mind, and your role is to
generate possible three questions a user
generate possible three questions a user
may want to ask next based on (cid:13275)(cid:13275)(cid:13900)User
may want to ask next based on (cid:13275)(cid:13275)(cid:13900)User
input: 개발자로 살아남으려면??(cid:13276)(cid:13276)
input: 개발자로 살아남으려면??(cid:13276)(cid:13276)
The questions must be from the
The questions must be from the
perspective of me, the user asking you a
perspective of me, the user asking you a
question.
question.
### (cid:13277)Ending(cid:13278)
## (cid:13277)Response template(cid:13278)
Always answer in half(cid:13247)speech form of
Predicted user question as followed:
Korean(cid:13273)반말(cid:13274). Don(cid:13364)t be over five words.
(cid:13247)High certainty
Only provide three questions.
(cid:13247) Moderate certainty, yet intriguing
(cid:13247) Low certainty, but strong potential for
## (cid:13277)Response template(cid:13278)
user engagement
Predicted user question as followed:
(cid:13258)High certainty
### (cid:13277)Ending(cid:13278)
(cid:13258) Moderate certainty, yet intriguing
Always answer in half(cid:13247)speech form of
(cid:13258) Low certainty, but strong potential for
Korean(cid:13273)반말(cid:13274). Don(cid:13364)t be over five words.
user engagement
Only provide three questions.

---

## 페이지 22 (OCR)

Chapter 03. 프롬프트 픔질관리: 테스트 방법론 
변수 처리 테스트 gpt-4o-mini V Options 
SYSTEM 
Control 
{$지시} 
{$엔딩} 순서 섞기 
{$답변 템플릿} 
{$지시} 
지 
You have a mind, and your role is to generate 
possible three questions a user may want to ask 
next based on {{$User input: 개발자로 살아남으려 
면??}} 
The questions must be from the perspective of 
/ 
{$엔딩} 
엔 Korean(반말). 
Always answer in half-speech form of 
지시문: You have a mind, and your role is to generate possible three questions a user may 
want to ask next based on User input: 개발자로 살아남으려면? The questions must be from Don't be over five words. Only provide three 
the perspective of me, the user asking you a question. questions. 
{응답: ## [Response template] Predicted user question as followed:-High certainty- 
Moderate certainty, yet intriguing 
- Low certainty, but strong potential for user engagement} 
{결말: {### [Ending] Always answer in half-speech form of Korean(반말). Don't be over five {$답변 템플릿} 
words. Only provide three questions.} Fiedicted usei question as TOllowed. 
답 
-High certainty 
- Moderate certainty, yet intriguing 
- Low certainty, but strong potential for user 
engagement 
Fast campus

---

## 페이지 23 (OCR)

Chapter 03. 프롬프트 품질관리: 테스트 방법론 
Result 
{$지시} {$지시} 
{$엔딩} {$답변 템플릿} 
{$답변 템플릿} {$엔딩} 구조 변경 차이 없음 
Token Input: 114 / Output: 33 Token Input: 114 / Output: 32 
1. 어떤 기술 배워야 해? 2. 경력 쌓는 법은? 3. 개발자 커뮤니티는 어때? - 어떤 기술 배우면 좋을까? - 개발자로서 경력 쌓는 법? - 요즘 트렌드는 뭐 
야? 
{$엔딩} {$엔딩} 
{$지시} {$답변 템플릿} 
{$답변 템플릿} {$지시} 
Token Input: 114 / Output: 27 Token Input: 114 / Output: 30 
어떤 기술 배워야 해? 경쟁자들은 어떻게 하나? 프리랜서로도 가능해? 어떤 기술 배워야 해? 경쟁자들 어떻게 이길까? 프리랜서 괜찮을까? 
{$답변 템플릿} {$답변 템플릿} 
{$지시} {$엔 딩} 
{$엔딩} {$지시} 
Token Input: 114 / Output: 30 Token Input: 114 / Output: 26 
- 어떤 기술 배워야 해? - 경력 쌓는 법은? - 개발자 커뮤니티 추천해줘! 어떤 기술 배워야 해? 경쟁자들은 누구야? 일자리 찾는 팁 있어? 
Fast campus

---

## 페이지 24

Chapter 03. 프롬프트픔질관리:테스트방법론
번역 Task
Type 2
Type 1
한국어로 번역해줘
0. Please list out all the target words at first.
0. Please list out all the target words at first.
1. Use beginner-level Korean language. For
1. Use beginner-level Korean language. For
instructions, please also provide a set of
instructions, please also provide a set of
English instructions in parentheses after the
English instructions in parentheses after the
Korean instructions.
Korean instructions.
2. Encourage David to speak more than you
2. Encourage David to speak more than you
do.
do.
3. Provide feedback on grammar, help apply
3. Provide feedback on grammar, help apply
new concepts, and expand vocabulary.
new concepts, and expand vocabulary.
4. Adapt your teaching style based on David’s
4. Adapt your teaching style based on David’s
responses and progress.
responses and progress.
5. Use Korean for target vocabulary and
5. Use Korean for target vocabulary and
example sentences. Use English for explanations
example sentences. Use English for explanations
and instructions.
and instructions.
한국어로 번역해줘.

---

## 페이지 25

Chapter 03. 프롬프트픔질관리:테스트방법론
Type 1 Type 2
- 구조 변경 차이 있음

---

## 페이지 26

Chapter 03. 프롬프트픔질관리:테스트방법론
Type 1 Type 2
- 구조 변경 차이 있음

---

## 페이지 27

Chapter 03. 프롬프트픔질관리:테스트방법론
3. 프롬프트 효율성평가 You have a mind, and your role is to
generate possible three questions a user
may want to ask next based on (cid:13275)(cid:13275)(cid:13900)User
input: 개발자로 살아남으려면??(cid:13276)(cid:13276)
(1) 프롬프트 길이
The questions must be from the
불필요하게 긴지,
perspective of me, the user asking you a
더 간단하게 표현할 수 있는지 평가 question.
## (cid:13277)Response template(cid:13278)
(2) 컨텍스트 평가
Predicted user question as followed:
컨텍스트가 충분하지, 과도한지 평가 (cid:13247)High certainty
(cid:13247) Moderate certainty, yet intriguing
(cid:13247) Low certainty, but strong potential for
user engagement
### (cid:13277)Ending(cid:13278)
Always answer in half(cid:13247)speech form of
Korean(cid:13273)반말(cid:13274). Don(cid:13364)t be over five words.
Only provide three questions.

---

## 페이지 28

Chapter 03. 프롬프트픔질관리:테스트방법론
You have a mind, and your role is to
3. 프롬프트 효율성평가
generate possible three questions a user
may want to ask next based on (cid:13275)(cid:13275)(cid:13900)User
input: 개발자로 살아남으려면??(cid:13276)(cid:13276)
The questions must be from the
(1) 간단한 버전 vs (2) 원래 버전
perspective of me, the user asking you a
question.
Please generate three questions based on
## (cid:13277)Response template(cid:13278)
(cid:13275)(cid:13275)(cid:13900)User input: 개발자로 살아남으려면?(cid:13276)(cid:13276) in
Predicted user question as followed:
Korean. Be short.
(cid:13247)High certainty
(cid:13247) Moderate certainty, yet intriguing
(cid:13247) Low certainty, but strong potential for
user engagement
### (cid:13277)Ending(cid:13278)
Always answer in half(cid:13247)speech form of
Korean(cid:13273)반말(cid:13274). Don(cid:13364)t be over five words.
Only provide three questions.

---

## 페이지 29 (OCR)

Chapter 03. 프롬프트 픔질관리: 테스트 방법론 
질적 분석. 프롬프트 테스트 루브릭 
프롬프트 제목 각 슬라이드 내용 작성 프롬프트 A 
사용자가 입력한 주제에 맞게 슬라이드 한 장 한 장의 내용을 자세하고 꼼 
제작 목적 & 기능 
꼼하게 완성해주는 프롬프트다. 
평가 항목 점수 개선 사항 및 의견 
정확성 2 슬라이드 주제와 100% 맞게 생성하지 않는다. 
일관성 5 내용에 흐름이 있고 전개 방식이 일정하다. 
언뜻보면 주제와 맞는 내용을 생성하지만, 사용자가 이 프롬 
유용성 2 프트의 결과물을 바로 사용하기에는 어렵다. 추가 수정 작업 
을 거쳐야 해서 유용성이 떨어진다. 
한국어가 자연스럽고, 슬라이드 내용에 딱 맞는 문단으로 구 
문법 및 문체 5 
성되어 있다. 
대부분의 모델에서 잘 응답한다. 특히 GPT-4-turbo의 품질 
모델 대응 5 
이 매우 좋다. 
내용의 정확성을 보완하고, 유용한 내용을 생성할 수 있도록 
종합점수 19/25 프롬프트를 개선할 필요가 있다. 사용자가 원하는 주제에 맞 
게 자세한 내용을 생성할 수 있도록 만드는 작업이 필요하다. 
Fast campus

---

## 페이지 30 (OCR)

05. 프롬프트 성능 수치화: 정량적 접근 방법 
Fast campus

---

## 페이지 31

Chapter 03. 프롬프트픔질관리:테스트방법론
정량적 테스트를 위한 여러 가지 방법
1. N번 생성해보기 (N > 100)
2. 응답 패턴 찾기
3. 모델별 테스트

---

## 페이지 32

Chapter 03. 프롬프트픔질관리:테스트방법론
1회차/ N=20회 응답 패턴 분석
질문: 개발자로 살아남으려면?

---

## 페이지 33

Chapter 03. 프롬프트픔질관리:테스트방법론
2회차/ N=20회 응답 패턴 분석
질문: 안구 건조증에 좋은 음식?

---

## 페이지 34

Chapter 03. 프롬프트픔질관리:테스트방법론
3회차/ N=20회 응답 패턴 분석
Q. 영어에 어떻게 대응하나? What’s the Best food in Hawaii?

---

## 페이지 35

Chapter 3
06. 프롬프트 테스트 실습 (cid:13273)1(cid:13274): 구조 및 내용 최적화 기법

---

## 페이지 36

Chapter 03. 프롬프트픔질관리:테스트방법론
Practice : 다음 프롬프트로 구조화 및 내용 최적화 테스트를
해보세요.
System Prompt_ Complete Version
Your name is (cid:13275)(cid:13275)(cid:13900)사용자 지정 (cid:13276)(cid:13276). As my friendly AI language assistant,
you are tasked with providing me an accurate information.
If you find that the information at hand is inadequate, please ask me
for further information. Furthermore, I trust your judgment to adjust
the language tone and manner.
(cid:13277)Strong Rule(cid:13278)
1. Modify the response structure to align with your preferred format.
2. If you don(cid:13380)t have any real(cid:13247)time information about the user(cid:13364)s
query, please be honesty./n
Your knowledge cutoff: year(cid:13247)month
Current UTC: (cid:13275)(cid:13275)(cid:13900)Today(cid:13276)(cid:13276).
Let(cid:13380)s get started.

---

## 페이지 37

Chapter 03. 프롬프트픔질관리:테스트방법론
Practice : 다음 프롬프트로 구조화 및 내용 최적화 테스트를
해보세요.
Data Generation Word List: 단어를 다양하게 생성하는 작업
3살 어린 아이가 쉽게 이해할 수 있는 아주 쉬운 단어를 사용해서 3(cid:13247)5단락
정도의 이야기를 써줘. 이야기에는 동사 (cid:13275)random.choice(cid:13273)verbs(cid:13255)list(cid:13274)(cid:13276), 명사
(cid:13275)random.choice(cid:13273)nouns(cid:13255)list(cid:13274)(cid:13276) 그리고 형용사
(cid:13275)random.choice(cid:13273)adjectives(cid:13255)list(cid:13274)(cid:13276) 를 사용해야 해.
다음 특징을 꼭 반영해 (cid:13275)random.choice(cid:13273)features(cid:13255)list(cid:13274)(cid:13276).
꼭 쉬운 단어를 사용해야 해.

---

## 페이지 38

Chapter 3
06. 프롬프트 테스트 실습 (cid:13273)2(cid:13274):
다양한 LLM간 프롬프트 성능 비교

---

## 페이지 39

Chapter 03. 프롬프트픔질관리:테스트방법론
Practice : 다음 프롬프트로 LLM 모델별 테스트를 진행해보세요.
모델별 프롬프트 답변 특징을 파악하고, 문제를 찾아 개선해보세요.
• 테스트 데이터 셋 사용하기
Revised Version
You are an AI assistant helping users with various
tasks. Your name is (cid:13275)(cid:13275)(cid:13900)사용자 지정(cid:13276)(cid:13276). If you find the
information insufficient, please ask the user to
rephrase their question. Always respond in Korean.

---

## 페이지 40

Chapter 03. 프롬프트픔질관리:테스트방법론
Practice : 다음 프롬프트로 LLM 모델별 테스트를 진행해보세요.
모델별 프롬프트 답변 특징을 파악하고, 문제를 찾아 개선해보세요.
• 테스트 데이터 셋 사용하기
Data Generation
Summary: {a short summary generated by LLM}
Features: {copy the features from the initial prompt}
Sentence: {a sentence generated by LLM, which should be present in the story}
Words: {copy the words from the initial prompt} Story:
Prompt 예시
요약 : {LLM이 생성한 짧은 요약을 내용에 포함}
특징: { 내용에 반전이 있어야 함}
문장: {구어체 }
단어: {한국어 의성어, 의태어 많이 사용}
이야기: {중국으로 간 팬더 푸바오의 하루}

---
