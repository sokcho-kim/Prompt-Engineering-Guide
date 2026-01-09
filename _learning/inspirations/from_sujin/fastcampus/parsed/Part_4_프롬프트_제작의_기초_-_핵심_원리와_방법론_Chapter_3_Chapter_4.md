# Part 4. 프롬프트 제작의 기초 - 핵심 원리와 방법론 (Chapter 3 ~ Chapter 4)

> 파싱 일시: 2026-01-09 17:58:20
> 총 페이지: 83
> 텍스트 추출 성공: 76
> OCR 필요: 7

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering

---

## 페이지 2

Chapter 03. Part 04.
Prompt Engineering Techniques
Level : Basic (cid:13249) Advanced (cid:13247) Applications

---

## 페이지 3

Chapter 03
Taxonomy of Prompt Engineering Techniques
Advanced
Basic Applications
• Generate Knowledge Prompting, •데이터생성과분류하기
•Zero-Shot Prompting Prompt Chaining, Tree of Thoughts
•코드생성하기
•Few-Shot Prompting • Retrieval Augmented Generation,
•펑션콜함수
Automatic Prompt Engineer,
•Chain-of-Thought Prompting
Active-Prompt,
•Self-consistency Directional Stimulus Prompting,
ReAct

---

## 페이지 4

Table of Contents
8 Advanced Prompt Engineering Techniques
Generate Knowledge Prompting
01
02 Prompt Chaining
03 Tree of Thoughts
04 Retrieval Augmented Generation
05 Automatic Prompt Engineer
06 Active-Prompt
07 Directional Stimulus Prompting
08 React

---

## 페이지 5

Chapter 03.
The Advanced Prompt Engineering Techniques
01. Generate Knowledge Prompting

---

## 페이지 6

Chapter 3. 프롬프트엔지니어링심화
Generate Knowledge Prompting
개요: 언어 모델의 추론 능력을 더 향상시키기 위한 방법
목적:
o 할루시네이션 현상을 완화하기 위한 방법
o 언어 모델이 추가 지식을 활용하게 하는 것
o 언어 모델이 오픈 Q(cid:13247)A 테스크 방식을 활용 하여 스스로 지식을 생성함
o 모델로부터 최종 답변을 얻기 전 모델이 직접 관련 정보를
가져오도록 한 다음 이를 활용해서 답을 가져오도록 하는 방식
이전:
• 사람이 직접 관련 정보를 넣어야 하는 번거로움, 별도의 모델,
• 검색 엔진 필요
• 외부 지식 IR 정보 추출
• 구글 검색 결과 활용
• 백과 사전 검색

---

## 페이지 7

Chapter 3. 프롬프트엔지니어링심화
작동 방식 세 단계
o Step 1. 지식 생성(cid:13273)knowledge Generation(cid:13274)
Few-shot prompting 을 사용해서 언어 모델로부터 관련 정보를 생성
o Step 2. 지식 통합(cid:13273)knowledge Integration(cid:13274) 두 번째 언어 모델을 사용하여, 1단계에서 생성된 정보에 대해 예측하게 함
그 다음, 가장 높은 확신을(High-confidence prediction) 가진 예측을
최종 답변으로 선택
o Step 3. 답변 생성(cid:13273)Answer Generation(cid:13274)

---

## 페이지 8

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Generated knowledge prompting for commonsense reasoning (Liu et al., 2021)
프롬프트 구성 요소 Instruction, Human-Written Demonstration, Question
프롬프트: 입력에대한지식을생성하십시오.
예시:
입력: 구름에의해형성되는물의종류는무엇인가요?
지식: 구름은수증기로만들어집니다.
입력: 음식을상하지않게하는방법은무엇인가요?
지식: 탈수처리는음식을보존하는데사용됩니다.
입력: 유전자가전달되는과정은무엇인가요?
지식: 유전자는부모로부터자손에게전달됩니다.
입력: 위장은몸에서어떤역할을하나요?
지식: 위장은소화시스템의일부입니다.
입력: 암석을부수는원인은무엇인가요?
지식: 기계적풍화는암석이기계적수단으로부서질때발생합니다
.
입력: (cid:13275)질문(cid:13276)
지식:
• QASC (cid:13273)Question Answering via Sentence Composition(cid:13274)는문장구성을통한질문응답을위한데이터셋. 초등학교
과학에관한9,980개의8지선다형질문으로구성되어있음.
Liu, J., Liu, A., Lu, X., Welleck, S., West, P., Bras, R. L., ... & Hajishirzi, H. (2021). Generated knowledge prompting for commonsense reasoning.arXivpreprint arXiv:2110.08387.

---

## 페이지 9

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Knowledge Integration Via Prompting
*k1, k2, ..., kM은 모델이 생성한 다양한 지식 문장
o 예시: 판다의 다리는 몇 개입니까?
• 모델 예측:
Step 1. 지식 생성:
각 결합된 질문(cid:13273)q0, q1, q2, q3(cid:13274)을 모델에게 주고 답변을 예측
(cid:13247) 판다는 네 개의 다리를 가지고 있다.
가장 신뢰할 수 있는 답변 선택:
(cid:13247) 판다는 포유류이다.
모델이 예측한 답변들 중 가장 신뢰할 수 있는 답변 선택
(cid:13247) 판다는 중국에서 서식한다.
Step 2. 질문 결합
• 이 지식들을 질문과 결합
예를 들어:
•q0 (cid:13965) (cid:13379)판다의 다리는 몇 개입니까?(cid:13379)
정답: q1
•q1 (cid:13965) (cid:13379)판다는 네 개의 다리를 가지고 있다. 판다의 다리는 몇 개입니까?(cid:13379)
•q2 (cid:13965) (cid:13379)판다는 포유류이다. 판다의 다리는 몇 개입니까?(cid:13379)
•q3 (cid:13965) (cid:13379)판다는 중국에서 서식한다. 판다의 다리는 몇 개입니까?(cid:13379)
Liu, J., Liu, A., Lu, X., Welleck, S., West, P., Bras, R. L., ... & Hajishirzi, H. (2021). Generated knowledge prompting for commonsense reasoning.arXivpreprint arXiv:2110.08387.

---

## 페이지 10

Chapter 3. 프롬프트엔지니어링심화
실험 결과
Baseline 비교
ü Generated Knowledge Prompting은 검색해서 정답을 얻는 방법에 준하는 결과
Vanilla baseline:
•기본적인모델성능.
Random sentences:
•무작위문장을사용.
Context sentences:
•문맥정보를제공.
Template(cid:13247)based:
•템플릿기반접근방식.
Retrieval(cid:13247)based:
•검색기반접근방식.
Answers:
•정답을제공.
Ours
• Generate Knowledge Prompting
Table 3: Experimental results of applying different knowledge generation methods on various tasks and inference models. T5-11b is the zero-shot inference model, whereas other inference
models are finetuned based on T5-11b. We bold the best and underline the second bestnumbers. Previous SOTA and retrieval-based methods are also based on the inference model in their
corresponding column: * T5-11b 1.1 +digits (Submission by ISI Waltham); ** T5-11b + IR (Yan, 2021); # UQA-11b-ft (Khashabiet al., 2020) (SOTA of single-model methods without referencing
ConceptNet); † Unicorn-ft (Talmor et al., 2021); †† Unicorn-ft + Google snippets (Talmor et al., 2021); ‡ UQA-11b-ft (Khashabiet al., 2020).
• NumerSense는숫자상식을평가하기위한데이터셋으로, 0에서10 사이의숫자가마스킹된문장들로구성되어있음.
• 데이터셋은언어모델이마스킹된숫자를정확히예측할수있는지를테스트함.
• QASC (cid:13273)Question Answering via Sentence Composition(cid:13274)는문장구성을통한질문응답을위한데이터셋. 초등학교과학에관한9,980개의8지선다형질문으로구성되어있음.
• CSQA (cid:13273)Commonsense Question Answering(cid:13274)는상식기반질문에답변하기위한데이터셋

---

## 페이지 11

Chapter 3. 프롬프트엔지니어링심화
실험 결과
Baseline 비교
o Knowledge 를 몇 개까지 만드는게 좋은가? o Integration 방법 3 개중 Knowledge 방법이 제일 좋음
(cid:13273)20개 까지(cid:13274)
o Ours: 프롬프트 (cid:13961) 지식 추가
o Mixture(cid:13247)of(cid:13247)Experts: 외부 모델과의 결합
o Product(cid:13247)of(cid:13247)Experts: 확률 값을 곱하는 방식

---

## 페이지 12

Chapter 3. 프롬프트엔지니어링심화
실험 결과
실제로 유용한 knowledge 인가?
사람 평가 결과
도움이 되는 & 유해한 지식 분포
o 선택된 지식이 모델 예측을 개선하는 데 매우 효과적임
o 유해한 지식을 비율을 줄여야 함
잘못 생성된 지식 중에서는
Harmful/neutral
• Grammatic/Relevant: 문법적으로 올바르고 관련성 있음
• Factual: 사실에 기반한 진술
• Helpful : 모델의 예측에 도움이 되는지 평가

---

## 페이지 13

Chapter 03.
The Advanced Prompt Engineering Techniques
02. Prompt Chaining

---

## 페이지 14

Chapter 3. 프롬프트엔지니어링심화
Prompt Chaining
o 복잡한 작업을 더 작고 관리하기 쉬운 하위 작업으로 나누어 각각의 하위 작업을 별도의 프롬프트로 처리하는 기법
o 한 프롬프트의 출력이 다음 프롬프트의 입력으로 사용
o 대형 언어 모델(cid:13273)LLM(cid:13274)의 성능과 신뢰성을 향상시키고 투명성, 제어 가능성, 신뢰성을 높임
1. 다단계 작업:
주제 조사, 에세이 작성 계획, 에세이 작성, 에세이 형식화 등 여러 개의 분리된 단계가 필요한 작업의 경우,
고품질 결과 보장
2. 복잡한 지시사항
LLM이 처리하기 어려운 복잡한 작업을 단계로 나누어, 각 단계의 작업 성능을 높임 (예시. CS챗봇)
3. 출력물 검증
체이닝을 사용하여 자신의 출력을 기준에 따라 검증. 출력물의 안전성과 정확성을 향상시킬 수 있음
4. 병렬 처리: 독립적인 하위 작업의 병렬 작업으로 시간 절약
Source: https://docs.anthropic.com/en/docs/chain-prompts

---

## 페이지 15

Chapter 3. 프롬프트엔지니어링심화
Use Cases for Prompt Chaining
o 긴 텍스트에서 ＂질의 응답(cid:13362) 기능 프롬프트
o 두 가지 프롬프트 제작:
(cid:13273)1(cid:13274) 질문에 답하기 위해 문서 내 관련 문장 추출
(cid:13273)2(cid:13274) (cid:13273)1(cid:13274)에서 추출한 문장 활용하여 주어진 질문에 답생성
Prompt 1. 인용문 추출하기
Prompt 1. (cid:13275)(cid:13275)quotes(cid:13276)(cid:13276) Extraction
You are a helpful assistant. Your task is to help answer
너는 나의 어시스턴트야. 너의 임무는 문서에 주어진 질문에 답하는 거야. 첫
a question given in a document. The first step is to extract 번째 단계는 ####로 구분된 문서에서 질문과 관련된 인용문을
quotes relevant to the question from the document, delimited 추출하는거야.
by ####.
인용문 목록을 (cid:13968)quotes(cid:13967)(cid:13968)/quotes(cid:13967) 태그로 출력해줘.
관련된 인용문을 찾지 못하면 (cid:13379)No relevant quotes found!(cid:13379)라고 응답해
Please output the list of quotes using (cid:13968)quotes(cid:13967)(cid:13968)/quotes(cid:13967).
####
Respond with (cid:13379)No relevant quotes found!(cid:13379) if no relevant
(cid:13275)(cid:13275)document(cid:13276)(cid:13276)
quotes were found.
####
####
(cid:13275)(cid:13275)document(cid:13276)(cid:13276)
질문: 앤트로픽 회사에 대한 문장
####

---

## 페이지 16

Chapter 3. 프롬프트엔지니어링심화
Use Cases for Prompt Chaining Prompt 2. (cid:13273)1(cid:13274) 결과물 이용해서 답변 생성하기
문서에서 가져온 관련 인용구를 사용하여 질문에 답변해.
Prompt 2. (cid:13275)(cid:13275)Quotes(cid:13276)(cid:13276) Question Answering
Here is a document, in <document></document> XML 여기 문서가 있어:
<document>
tags:
{{DOCUMENT}}
</document>
<document>
{{DOCUMENT}}
</document>
여기 질문과 가장 관련 있는 문서의 직접 인용구야:
<quotes>
Please extract, word-for-word, any quotes relevant to the {{QUOTES}}
question {{QUESTION}}. Please enclose the full list of </quotes>
quotes in <quotes></quotes> XML tags. If there are no
quotes in this document that seem relevant to this
이것들을 사용하여 "{{QUESTION}}"에 대한 답변을 구성해.
question, please say "I can't find any relevant quotes"
답변이 정확하고 인용구에 직접적으로 뒷받침되지 않는 정보는
포함하지 말아.
{{QUESTION}}: 앤트로픽은 어떤 회사인가요?

---

## 페이지 17

Chapter 03.
The Advanced Prompt Engineering Techniques
03. Tree of Thought

---

## 페이지 18

Chapter 3. 프롬프트엔지니어링심화
Tree of Thoughts, ToT
o 더 복잡하고, 전략적인 과제 해결을 위한 프레임워크
o CoT 프롬프트를 일반화하고, 언어 모델을 사용한 일반 문제 해결을 위해 중간 단계를 거치며 탐색
o 문제를 해결하기 위해 여러 가능성을 탐색하며 최적의 해결책을 찾아감
네 단계 과정
1단계. 생각 분해하기 (cid:13273)thought decomposition(cid:13274)
2단계. 생각 생성하기 (cid:13273)thought generator(cid:13274)
3단계. 생각 평가하기 (cid:13273)state evaluator(cid:13274)
4단계. 검색 알고리즘 (cid:13273)search algorithm(cid:13274)

---

## 페이지 19

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Yao et al. 2024)
CoT 와 ToT 기법을 비교하면 큰 차이점.
CoT 는 회귀를 할 수 없다. 언어 모델에 입력 값을 넣으면 순차적으로 진행하면 추론한 결과를 내놓는다(cid:13273)linear search(cid:13274).
ToT 는 중간에 회귀를 하고 더 좋은 방법을 시도한다.
o 각각의 직사각형 박스는 생각을 대표함.
o 각 상자는 문제해결을 위한 중간단계로
일관된 언어 순서인 생각을 나타냄.
o 생각이 어떻게 생성되고, 평가되며
검색되는지 보여줌.
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2024). Tree of thoughts: Deliberate problem solving with large language models.Advances in
Neural Information Processing Systems,36.

---

## 페이지 20

Chapter 3. 프롬프트엔지니어링심화
Tree of Thoughts: Deliberate Problem Solving with Large Language Models
ü 3 new tasks GPT(cid:13247)4 can(cid:13380)t solve directly or with CoT
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2024). Tree of thoughts: Deliberate problem solving with large language models.Advances in
Neural Information Processing Systems,36.

---

## 페이지 21

Chapter 3. 프롬프트엔지니어링심화
Q. 숫 자 네 개 (cid:13273)4, 9, 10, 13(cid:13274)으로 사칙연산으로 24를 만들 수 있는가?
생각 분해 생각 생성 생각 평가
중간 중간 수식과 남은 숫자를 다음 단계에서는 (cid:13363)Possible next 다음 숫자를 통해서 24를 만들 수
표시하면서 생각 분해 과정 거침 inputs(cid:13364) 라는 프롬프트를 사용해 있는지를 평가 (cid:13273)가능 _ 불가능(cid:13274)
생각을 만듦 그러면서 정답에 도달
1. 4 (cid:13961) 9 (cid:13247)13 (cid:13961) 10 1. 4 * 6 (cid:13965) 24 (cid:14067) 가능
4, 9, 10, 13 (cid:14067) 13(cid:13247)9(cid:13965)4; 4*6(cid:13965)24
2. (cid:13273)4 * 10(cid:13274) (cid:13247)(cid:13273)9 (cid:13961) 13(cid:13274) 2. 10 (cid:13961) 13 (cid:13247)3 (cid:13965) 20 (cid:14067) 불가능

---

## 페이지 22

Chapter 3. 프롬프트엔지니어링심화
o ToT의 문제 풀이 성공률
CoT 에 비해 ToT 는 적은 개수를 풀고도 가장 높은 성공률
CoT는 첫 시도부터 오답
ToT는 단계별 정답 생성했기 때문에 오답률이 0.0 에
가까움
Results. As shown in Table 2, IO, CoT, and CoT-SC prompting methods perform badly on the task, achieving only 7.3%, 4.0%, and 9.0% success
rates. In contrast, ToTwith a breadth of b = 1 already achieves a success rate of 45%, while b = 5 achieves 74%. We also consider an oracle
setup for IO/CoT, by calculating the success rate using best of k samples (1 ≤ k ≤ 100). To compare IO/CoT(best of k) with ToT, we consider
calculating the tree nodes visited per task in ToTacross b = 1 · · · 5, and map the 5 success rates in Figure 3(a), treating IO/CoT(best of k) as
visiting k nodes in a bandit. Not surprisingly, CoTscales better than IO, and best of 100 CoTsamples achieve a success rate of 49%, but still
much worse than exploring more nodes in ToT(b > 1).
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2024). Tree of thoughts: Deliberate problem solving with large language models.Advances in
Neural Information Processing Systems,36.

---

## 페이지 23

Chapter 3. 프롬프트엔지니어링심화
o ToT 기법의 한계
GPT(cid:13247)4/4o가 대체로 많은 영역에서 좋은 성능 (cid:13247) ToT기법 적용 가능 범위 적음
많은 연산 과정이 필요 (cid:13247) 과제를 수행하는데 시간과 API비용
코드 https://github.com/princeton-nlp/tree-of-thought-llm

---

## 페이지 24

Chapter 3. 프롬프트엔지니어링심화
Tree-of-thoughts-prompting (X Framework)
Hulbert (2023)
ToT 의 컨셉을 활용하여 단순한 프롬프트 엔지니어링 기법 제안
하나의 프롬프트에 언어 모델이 중간 단계를 평가할 수 있도록 함
Imagine three different experts are answering this question. All experts will write down 1 step of their thinking,
then share it with the group. Then all experts will go on to the next step, etc. If any expert realises they're
wrong at any point then they leave. The question is...
Simulate three brilliant, logical experts collaboratively answering a question. Each one verbosely explains their
thought process in real-time, considering the prior explanations of others and openly acknowledging
mistakes. At each step, whenever possible, each expert refines and builds upon the thoughts of others,
acknowledging their contributions. They continue until there is a definitive answer to the question. For clarity,
your entire response should be in a markdown table. The question is...
Identify and behave as three different experts that are appropriate to answering this question.
All experts will write down the step and their thinking about the step, then share it with the group.
Then, all experts will go on to the next step, etc.
At each step all experts will score their peers response between 1 and 5, 1 meaning it is highly unlikely, and 5
meaning it is highly likely.
If any expert is judged to be wrong at any point then they leave.
After all experts have provided their analysis, you then analyze all 3 analyses and provide either the consensus
solution or your best guess solution.
The question is...
Source: https://github.com/dave1010/tree-of-thought-prompting

---

## 페이지 25

Chapter 3. 프롬프트엔지니어링심화
Tree-of-thought-prompting 예시
세 명의 다른 전문가가 이 질문에 답하는 모습을 상상해보세요. 모든 전문가는 그들의 생각을
한 단계씩 작성한 후 그룹과 공유할 것입니다. 그런 다음 모든 전문가는 다음 단계로
진행합니다. 만약 어떤 전문가가 어느 순간에 자신이 틀렸다는 것을 깨닫는다면, 그들은 전문가 (cid:13249) 생각 공유
떠나게 됩니다. 질문은...
세 명의 뛰어나고 논리적인 전문가가 협력하여 질문에 답하는 것을 시뮬레이션합니다. 각
전문가는 다른 전문가들의 이전 설명을 고려하며 실시간으로 자신의 사고 과정을 장황하게
전문가 (cid:13249) 생각 공유 (cid:13249) 응답 표로 작성
설명하고 실수를 공개적으로 인정합니다. 각 단계에서 가능한 한 서로의 생각을 정제하고
구축하며, 기여를 인정합니다. 그들은 질문에 대한 명확한 답이 나올 때까지 계속합니다.
명확성을 위해, 응답 전체를 마크다운 표로 작성해야 합니다. 질문은...
이 질문에 답하는 데 적합한 세 명의 다른 전문가를 식별하고 그들처럼 행동하세요. 모든
전문가는 단계와 해당 단계에 대한 생각을 작성한 후 그룹과 공유합니다. 그런 다음 모든
전문가는 다음 단계로 진행합니다. 각 단계에서 모든 전문가는 동료의 응답을 1에서 5까지
점수로 평가합니다. 1은 가능성이 매우 낮음을 의미하고, 5는 가능성이 매우 높음을
전문가 (cid:13249) 동료 평가 (cid:13249) 최적 솔루션
의미합니다. 어떤 전문가가 어느 시점에서 틀렸다고 판단되면, 그들은 떠나게 됩니다.
모든 전문가가 분석을 제공한 후, 세 가지 분석을 모두 분석하고 합의된 솔루션이나 최선의
추정 솔루션을 제공합니다. 질문은...

---

## 페이지 26

Chapter 03.
The Advanced Prompt Engineering Techniques
03. RAG
(cid:13273)Retrieval Augmented Generation(cid:13274)

---

## 페이지 27

Chapter 3. 프롬프트엔지니어링심화
RAG (Retrieval Augmented Generation)
o 검색증강생성
o 프롬프트로 컨텍스트 정보를 추가해, 언어 모델의 결과 품질을 높이는 것
o 질문에 대한 답변을 생성할 때, 먼저 외부 데이터베이스에서 관련 정보를 검색(Retrieval)하고, 이를
바탕으로 답변을 생성(Generation)하는 방식
o 정확한 답변 제공, 다양한 도메인에 적용 가능, 정보 업데이트
o Key Points o When to use RAG:
• 언어 모델이 학습하지 않은 정보에 대해 생성할 때
정보 검색: 주어진 질문이나 입력 문장과 관련된 문서를 외부
데이터베이스나 지식베이스에서 검색. TF(cid:13247)IDF, BM25, dense • 할루시네이션의 비율을 줄이고 싶을 때
retrievers와 같은 정보 검색 알고리즘 사용 • 언어 모델의 응답을 특정 문서 내에서 생성할 때
정보 통합: 검색된 관련 문서들을 바탕으로 필요한 정보를 추출하고
통합. 생성 단계에서 사용할 수 있는 풍부한 컨텍스트 제공
자연어 생성: 통합된 정보를 바탕으로 질문에 대한 답변 생성. 이
단계에서는 Transformer 기반의 언어 모델, 예를 들어 GPT(cid:13247)3,
BERT 등을 활용하여 자연스러운 문장 생성

---

## 페이지 28

Chapter 3. 프롬프트엔지니어링심화
RAG (Retrieval Augmented Generation)
Standard Prompt: RAG-enhanced prompt:
Where does Ilya Sutskever work? Here is some relevant context for this conversation:
”"" {PASTE TEXT FROM WIKIPEDIA
https://en.wikipedia.org/wiki/Ilya_Sutskever}
""”
For the following question, please answer questions
based on the document above. Where does Ilya
Sutskever work?

---

## 페이지 29

Chapter 3. 프롬프트엔지니어링심화
RAG (Retrieval Augmented Generation)
Standard Prompt: RAG-enhanced prompt:
Explain the impact of climate change "Using the latest data from scientific studies, explain
on polar bear populations. the impact of climate change on polar bear
populations."
Output:
Output:
"According to a 2022 study published in the journal Nature
Climate change has a significant impact on
Climate Change, polar bear populations are experiencing
polar bear populations primarily through the
significant declines due to the rapid loss of sea ice in the
loss of sea ice habitat. As global temperatures
Arctic. The study highlights that the extent of sea ice has
rise, sea ice melts earlier and forms later each
decreased by approximately 13% per decade since 1979,
year, reducing the time polar bears have to
directly affecting the hunting and breeding habitats of polar
hunt seals, their primary food source. This leads
bears. Furthermore, the research indicates that by 2100, if
to malnutrition, decreased body condition, and
current trends continue, polar bears could lose over 80% of
lower cub survival rates. Additionally, polar
their habitat, leading to severe population declines. Another
bears may be forced to swim longer distances
report from the World Wildlife Fund (WWF) emphasizes that
to find suitable habitats, increasing the risk of
polar bear cub survival rates have dropped by 30% over the
drowning.
past decade due to malnutrition caused by shorter hunting
seasons."

---

## 페이지 30

Chapter 3. 프롬프트엔지니어링심화
RAG (Retrieval Augmented Generation)
고도화된 RAG 프롬프트 예시
프롬프트 엔지니어링
프롬프트:
명확한 요청
Using the latest scientific data, particularly from the
Using the latest scientific data
2022 Nature Climate Change journal and the World
Wildlife Fund reports, explain the impact of climate
콘텍스트 제공
change on polar bear populations. Specifically,
기후 변화, 북극곰 서식지, 연구 데이터 등의 배경 정보
address the following points:
출처 명시
• The rate of sea ice loss per decade. 2022년 Nature Climate Change 저널
• How sea ice loss affects the hunting and breeding
구체적인 요구사항
habitats of polar bears.
"해빙 손실", "사냥 및 번식 서식지", "새끼 생존율" 등
• The projected habitat loss by 2100.
구체적인 영향을 명시
• The impact on polar bear cub survival rates over the
past decade.

---

## 페이지 31

Chapter 3. 프롬프트엔지니어링심화
RAG 의 두 단계
1. Indexing: Knowledge Base 를 준비하는 단계
2. Query : KB로부터 추출한 컨텍스트를 활용해 LLM에게 질문 하는 단계
1단계 2단계
• 데이터 소스로부터 데이터를 로드 • 생성된 색인으로부터 질의에 맞는 컨텍스트 추출
• 로드한 데이터를 문서(cid:13273)Documents(cid:13274)로 변환 • 추출한 컨텍스트를 포함하여 LLM 쿼리
• 변환한 문서에 대한 색인(cid:13273)Index(cid:13274) 생성 • 쿼리 결과 처리
Image source: https://docs.llamaindex.ai/en/latest/getting_started/concepts/

---

## 페이지 32

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Lewis et al., (2021)
RAG Model Overview
문서 인덱스 (cid:13273)Document Index(cid:13274):
•미리인코딩된문서들의벡터데이터베이스. 각
•문서는질문벡터와의내적연산을통해관련성을평가받음.
생성기 (cid:13273)Generator(cid:13274):
•검색된문서들을입력으로받아최종답변을생성. 여러문서들을기반으로
가장적절한답변을생성하도록훈련됨.
•생성과정에서문서들에따라다양한답변을생성하고, 이를종합하여최종
답변을제공. 이를pθ로나타냄
최종 답변 생성:
•여러문서에대한답변을종합하여최종적으로하나의답변을생성
질문 인코더 (cid:13273)Query Encoder(cid:13274):
•질문qqq을입력받아인코딩
검색기 (cid:13273)Retriever(cid:13274):
•질문인코더가생성한질문벡터q(cid:13273)x(cid:13274)q(cid:13273)x(cid:13274)q(cid:13273)x(cid:13274)을사용하여문서
인덱스에서관련문서를검색. 이과정은최대내적검색(cid:13273)Maximum Inner
Product Search, MIPS(cid:13274)을통해이루어짐.
•검색된상위K개의문서z1,z2,...,zKz(cid:13255)1, z(cid:13255)2, ..., z(cid:13255)Kz1,z2,...,zK를반환.
이문서들은질문과관련이높은문서들.
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented
generation for knowledge-intensive nlptasks.Advances in Neural Information Processing Systems,33, 9459-9474.

---

## 페이지 33

Chapter 3. 프롬프트엔지니어링심화
Fig. 1. Technology tree of RAG research. The stages of involving RAG mainly include pre-training, fine-tuning,
and inference. With the emergence of LLMs, research on RAG initially focused on leveraging the powerful in
context learning abilities of LLMs, primarily concentrating on the inference stage. Subsequent research has
delved deeper, gradually integrating more with the fine-tuning of LLMs. Researchers have also been exploring
ways to enhance language models in the pre-training stage through retrieval-augmented techniques.
Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., ... & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey.arXivpreprint arXiv:2312.10997.

---

## 페이지 34

Chapter 3. 프롬프트엔지니어링심화
ü RAG의 단점
• RAG는 창의성을 제한, 작문 영역에서는 효용성이 낮음
• 비용이 비쌈 (많은 토큰 소모)
• 언어 모델이 문서 포맷을 이해하지 못하면, 할루시네이션 방지 못함
RAG & Prompt Engineering
프롬프트 엔지니어링은 RAG성능을 최적하는 데 중요한 역할
o 질문 구체화
o 컨텍스트 제공
o 모델 지침 (cid:13273)형식 (cid:13704) 스타일(cid:13274)

---

## 페이지 35

Chapter 03.
The Advanced Prompt Engineering Techniques
05. Automatic Prompt Engineer

---

## 페이지 36

Chapter 3. 프롬프트엔지니어링심화
Automatic Prompt Engineer
Research Paper
Large Language Models Are Human-Level Prompt Engineers. Zhou (2022)
o 자동 프롬프트 엔지니어(cid:13273)APE(cid:13274)라는 프레임워크를 제안
o APE는 여러 단계의 평가 과정을 통해 최적의 명령어를 자동으로 생성하고 선택하는 방법
o 각 단계에서 대형 언어 모델을 사용하여 후보 명령어를 생성하고 평가하며, 가장 적절한 명령어를 선택하여 최종적으로 사용
후보 명령어 제안
점수 매기기
여섯 단계
낮은 점수 후보 제거
높은 점수 후보 선정
샘플링 모델 사용 (cid:13273)선택사항(cid:13274)
최종 후보 선정
Zhou, Y., Muresanu, A. I., Han, Z., Paster, K., Pitis, S., Chan, H., & Ba, J. (2022). Large language models are human-level prompt engineers.arXivpreprint arXiv:2211.01910.

---

## 페이지 37

Chapter 3. 프롬프트엔지니어링심화
Automatic Prompt Engineer
Research Paper
Large Language Models Are Human-Level Prompt Engineers. Zhou (2022)
Zhou, Y., Muresanu, A. I., Han, Z., Paster, K., Pitis, S., Chan, H., & Ba, J. (2022). Large language models are human-level prompt engineers.arXivpreprint arXiv:2211.01910.

---

## 페이지 38

Chapter 3. 프롬프트엔지니어링심화
APE Workflow
1. LLMs as Inference Models
시작 지점에서 LLM은 제공된 프롬프트를 바탕으로 다양한 응답을 생성
예시 (cid:13379)write the antonym of the word(cid:13379)라는 입력을 받아 다양한 응답을 생성
2. LLMs as Scoring Models
각 생성된 프롬프트에 대해 LLM은 해당 프롬프트가 얼마나 적합한지 스코어를 매김
여기서 각 프롬프트는 (cid:13379)LIKELIHOOD(cid:13379)에 기반하여 점수를 받음
예를 들어, (cid:13379)write the antonym of the word(cid:13379)가 (cid:13247)0.26의 점수를 받는 식
High Score Candidates (cid:13273)높은 점수 후보군(cid:13274)
스코어링 모델을 통해 높은 점수를 받은 프롬프트는 유지되고,
낮은 점수를 받은 프롬프트는 제거됨
3. LLMs as Resampling Models (cid:13273)Optional(cid:13274)
선택적으로, 이 단계에서는 높은 점수를 받은 프롬프트 중에서 의미를 유지하면서
변형된 프롬프트를 생성.
예를 들어, (cid:13379)write the antonym of the word(cid:13379)라는 프롬프트를 바탕으로 (cid:13379)list antonyms for the
given word(cid:13379)라는 변형된 프롬프트가 생성
4. 최종 선택
최종적으로 가장 높은 점수를 받은 프롬프트가 선택되어 사용
(cid:13379)give the antonym of the word provided(cid:13379)라는 프롬프트가 최종적으로 선택

---

## 페이지 39

Chapter 3. 프롬프트엔지니어링심화
연구 결과
o APE는 인간이 설계한 (cid:13379)단계별로 생각해 보자(cid:13273)Let(cid:13380)s think step by step(cid:13274)(cid:13379) 프롬프트(cid:13273)Kojima et al., 2022(cid:13274)보다
더 나은 제로샷 연쇄적 사고(cid:13273)Chain(cid:13247)of(cid:13247)Thought, CoT(cid:13274) 프롬프트를 발견
o 확실한 정답을 얻기 위해 단계별로 해결해 보자
(cid:13361)Let(cid:13380)s work this out in a step by step way to be sure we have the right answer(cid:13362)라는
프롬프트는 연쇄적 사고를 유도하여 MultiArith 및 GSM8K 벤치마크에서 성능 향상 시킴
• MultiArith는복합산술문제를해결하기위해개발된알고리즘또는모델

---

## 페이지 40

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Large Language Models as Optimizers (Yang at el.,2023)
•OPRO(introduces the idea of using LLMs to optimize prompts:
• Let LLMs "Take a deep breath" improves the performance on math problems.
Optimization-based Prompt Re-optimization
Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q. V., Zhou, D., & Chen, X. (2023). Large language models as optimizers.arXivpreprint arXiv:2309.03409.

---

## 페이지 41

Chapter 3. 프롬프트엔지니어링심화
o Optimization-based Prompt Re-optimization
3. 생성된 해결책
2번 단계에서 생성된 결과
4. 목적 함수 평가자 (Objective Function Evaluator)
각각의 해결책에 점수 부여
5. 점수
6. 최적화 루프 (Optimization Loop)
점수가 부여된 새로운 해결책들은 메타 프롬프트에 추가됨
이 과정을 반복하여, LLM이 계속해서 새로운 해결책을 생성하고,
평가하고, 최적화함
1. 메타 프롬프트 최적화가 완료되면 가장 좋은 해결책들을 반환함
문제 설명 (cid:13249) 해결책 점수 쌍
2. LLM as Optimizer
메타 프롬프트를 입력으로 받아 새로운 해결책 생성

---

## 페이지 42 (OCR)

Chapter 03. 
The Advanced Prompt Engineering Techniques 
06. Active-Prompt 
Fast campus

---

## 페이지 43

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Active Prompting with Chain-of-Thought for Large Language Models (Diao et al., 2023)
o CoT 기법 한계 (cid:13704) 문제점
인간이 만든 예시에 의존함 다양한 작업에 대해 효과적인 예시가 아닐 수 있음
어렵고 모호한 질문에 대한 답을 예시로 LLM에게 주면, 복잡한 질문에도 답을 잘 함
사람이 질문(cid:13247)응답 쌍을 만드는데 한계가 있음
o Active Prompt
인간이 설계한 CoT 추론으로 주석이 달린 다양한 작업별 예시
프롬프트에 LLM 적용시키는 방법
Diao, S., Wang, P., Lin, Y., & Zhang, T. (2023). Active prompting with chain-of-thought for large language models.arXivpreprint arXiv:2302.12246.

---

## 페이지 44

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Active Prompting with Chain-of-Thought for Large Language Models (Diao et al., 2023)
답을 더 잘 찾기 위한 네 단계 과정
(1)Uncertainty Estimation
(2)Selection
(3)Annotation
(4)Inference
o AI가 답을 잘 모를 질문을 찾아낸다
o 가장 불확실한 질문들을 선택한다
o 사람이 그 질문에 답을 달아준다
o AI가 새로 답을 달아준 질문을 바탕으로 새로운 질문에
더 잘 답할 수 있게 된다
Figure 1: Illustrations of our proposed approach. There are four stages. (1) Uncertainty Estimation: with or without
a few human-written chain-of-thoughts, we query the large language model k (k “ 5 in this illustration) times to
generate possible answers with intermediate steps for a set of training questions. Then we calculate the
uncertainty u based on the k answers via an uncertainty metric (we use disagreement in this illustration). (2)
Selection: according to the uncertainty, we select the most uncertain questions for annotation. (3) Annotation:
we involve humans to annotate the selected questions. (4) Inference: infer each question with the new
annotated exemplars.
Diao, S., Wang, P., Lin, Y., & Zhang, T. (2023). Active prompting with chain-of-thought for large language models.arXivpreprint arXiv:2302.12246.

---

## 페이지 45

Chapter 3. 프롬프트엔지니어링심화
Research Paper
Active Prompting with Chain-of-Thought for Large Language Models (Diao et al., 2023)
ü 답변의 Uncertainty 를 어떻게 평가할까?
논문은 Disagreement 사용
모델로부터 동일한 질문에 대해 많은 답변을 내놓게 한다
답변들 중 동일한 답변 제외하고, unique 한 답변의 개수를 센다
그 갯수를 전체 답변 갯수로 나눈다
len(cid:13273)set (cid:13273)답변리스트(cid:13274)(cid:13274)/ len(cid:13273)답변 리스트(cid:13274)
질문: "A robe takes 2 bolts of blue fiber and half that much white fiber. How many
bolts in total does it take?”
답변: [3, 3, 3, 3, 3]
불확실성: 15=0.2\frac{1}{5} = 0.251=0.2
Diao, S., Wang, P., Lin, Y., & Zhang, T. (2023). Active prompting with chain-of-thought for large language models.arXivpreprint arXiv:2302.12246.

---

## 페이지 46

Chapter 03.
The Advanced Prompt Engineering Techniques
07. Directional Stimulus
Prompting

---

## 페이지 47

Chapter 3. 프롬프트엔지니어링심화
Directional Stimulus Prompting
Research Paper
Guiding Large Language Models via Directional Stimulus Prompting Li et al., (2023)
o 정의 : Prompt 에 사용할 힌트를 만드는 모델을 사용하는 방법
LLM을 원하는 출력 방향으로 유도하는 새로운 프레임 워크
o 사용 방법: 작은 튜닝 정책 모델(cid:13273)T5(cid:13274) 사용, 각 입력 값에 대한 보조 프롬프트 생성
생성된 요약에 특정 키워드를 포함시키기
1(cid:13274) Supervised Fine Tuning
2(cid:13274) Reinforcement Learning
Li, Z., Peng, B., He, P., Galley, M., Gao, J., & Yan, X. (2024). Guiding large language models via directional stimulus prompting.Advances in Neural Information Processing Systems,36.

---

## 페이지 48

Chapter 3. 프롬프트엔지니어링심화
1. 기사 입력
Directional Stimulus Prompting
CNN 기사 (cid:13362)The Price Is Right(cid:13362)
2. 정책 모델
기사를 읽고 중요한 키워드 추출
ü Language Model 을 학습시켜 힌트 만드는 모델 (cid:13273)Policy LM(cid:13274) 만들어 사용
(cid:13361)The Price Is Right(cid:13362), (cid:13361)Bob Baker(cid:13362), (cid:13361)2007(cid:13362)
3. 힌트
추출된 키워드는 힌트로 사용
키워드는 다음 단계의 요약에 도움
4. 블랙박스 모델
힌트를 바탕으로 기사 요약
5. 출력
답변에 대한 평가 진행 ROUGE 점수 사용
6. 보상
점수를 reward 로 사용하여 강화학습으로
Policy LM을 학습 시킴
Figure 2: Overview of our proposed framework DSP, where we learn a small tunable policy model to generate the
7. 학습된 정책 모델이 만들어지고,
directional stimulus (keywords in this case) that provide input-specific guidance for the LLM toward the desired target.
The policy model can be trained with SFT and/or RL, where the reward is defined as the downstream task performance 이를 Prompt의 힌트 부분을 만드는 작업에 활용
measure, such as the ROUGE score for the summarization task, or other alignment measures like human preferences.

---

## 페이지 49

Chapter 3. 프롬프트엔지니어링심화
평가결과
o 요약, 대화 응답 생성, 사고 추론
MultiWOZ 데이터셋에서 80개의 대화만을 사용하여, DSP 기법은 ChatGPT의 성능을 41.4% 향상
주요 평가 지표
1.ROUGE(cid:13247)1, ROUGE(cid:13247)2, ROUGE(cid:13247)L:
텍스트 요약의 정확성을 평가하는 지표
2. BLEU: 기계 번역의 품질을 측정하는 지표
3.METEOR: 의미적 일치를 평가하는 지표
4.BERTScore: 문장 임베딩을 사용하여 의미적 유사성을
평가하는 지표

---

## 페이지 50 (OCR)

Chapter 03. 
The Advanced Prompt Engineering Techniques 
08. React 
Fastcampus

---

## 페이지 51

Chapter 3. 프롬프트엔지니어링심화
ReAct Prompting
o Generate both reasoning traces and task(cid:13247)specific actions in an interleaved manner.
o Re (cid:13961) Act (cid:13965) 질문에 답하기 위한 생각(cid:13273)Reason(cid:13274)과 행동(cid:13273)Act(cid:13274)를 교차적으로 사용하는 프롬프팅 방식
1. Reasoning 생성
모델의 행동 계획 유도, 추적 및 업데이트, 예외 사항 처리
2. Action
지식 베이스나 환경과 같은 외부 소스와 상호작용하여 정보를 수집할 수 있도록 함
LLM이 외부 도구와 상호작용을 통해 더 신뢰할 수 있고 사실적인 응답을 생성하기 위해
추가 정보를 검색할 수 있게 함

---

## 페이지 52

Chapter 3. 프롬프트엔지니어링심화
Research Paper
ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022)
o 표준프롬프트: 추가적인 추론이나 행동 없이질문에 답변
o Chain-of-Thought (CoT) 추론만: 추론을 제공하지만행동은 하지 않음
o 행동만 (Act-Only): 추론없이 행동만 실행
o ReAct(Reason + Act): 추론과 행동을 결합하여 작업 수행
Figure 1: (1) Comparison of 4 prompting methods, (a) Standard,
(b) Chain-of-thought (CoT, Reason Only), (c) Act-only, and (d)
ReAct (Reason+Act), solving a HotpotQA (Yang et al., 2018)
question. (2) Comparison of (a) Act-only and (b) ReAct
promptingtosolveanAlfWorld(Shridharetal.,2020b)game.In
bothdomains,weomitin-contextexamplesintheprompt,and
only show task solving trajectories generated by the model
(Act,Thought)andtheenvironment(Obs).
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). React: Synergizing reasoning and acting in language models.arXivpreprint arXiv:2210.03629.

---

## 페이지 53

Chapter 3. 프롬프트엔지니어링심화
(cid:13361)Apple Remote 외에 Apple Remote에서
가능한 상호작용 기능을 할 수 있는 다른 장치는
무엇입니까?(cid:13379) 라는 질문에 대한 답변
Thought와 Action 과정을 추가한 것
(cid:13379)(cid:13973)하기 때문에 이제 (cid:13973)한 행동을 해야겠다(cid:13379)라고
생각하는 과정 (cid:13961) 생각을 통해 행동하는 과정을
단계적으로 수행하는 것

---

## 페이지 54

Chapter 3. 프롬프트엔지니어링심화
Hotpot QA as a Test-Training Set
Q. (cid:13379)Apple Remote 외에 Apple Remote에서 가능한 상호작용 기능을 할 수 있는 다른 장치는 무엇입니까?(cid:13379)
Thought 1: Apple Remote와 관련된 프로그램을 검색해야 한다고 생각합니다.
Act 1: Apple Remote를 검색합니다
.Obs 1: Apple Remote는 2005년에 도입된 장치입니다.
Thought 2: Front Row 프로그램을 제어할 수 있는 장치를 찾아야 한다고 생각합니다.
Act 2: Front Row를 검색합니다.
Obs 2: Front Row를 찾을 수 없습니다.
Thought 3: Front Row 소프트웨어를 검색해야 한다고 생각합니다.
Act 3: Front Row 소프트웨어를 검색합니다.
Obs 3: Front Row 소프트웨어는 Apple Remote로 제어할 수 있습니다.
Thought 4: 답은 키보드 기능 키입니다.
Act 4: 키보드 기능 키로 완료합니다.

---

## 페이지 55

Chapter 3. 프롬프트엔지니어링심화
연구 결과
PaLM-540B is used as the base model for prompting
ReAct outperforms (cid:13967)(cid:13967)(cid:13967) Act
o CoT는 환각 문제 발생
o ReAct 한계: 구조적 제약은 추론 단계를 공식화하는 유연성 감소시킴
o ReAct 는 검색정보에 의존, 정보가 부족한 검색결과는
o 모델의 추론을 방해하고, 생각을 복구하고 재구성하는 데 어려움 초래
• Hotpot QA는복잡한질의응답시스템으로여러출처의정보를통합하여복잡한질문에대한답을찾는것을목표로함
-다중문서이해(Multi-hop Reasoning) & 증거기반추론(Evidence-based Reasoning)
• FEVER(cid:13273)Fact Extraction and VERification(cid:13274) 데이터셋은사실확인(cid:13273)fact(cid:13247)checking(cid:13274) 작업을위해설계된대규모데이터셋입니다.

---

## 페이지 56

Chapter 3. 프롬프트엔지니어링심화
React Prompting 장점
o 문제 해결 능력 향상
질문을 해결하기 위해 필요한 정보를 순차적으로 검색하며, 각 검색 결과를 바탕으로 다음 검색 방향을 결정
o 문제 적응력 향상
생각(cid:13273)Thought(cid:13274)과 행동(cid:13273)Act(cid:13274)을 번갈아가며 수행하여 점진적으로 질문에 대한 답을 찾아감.
o 정보 신뢰성 증가

---

## 페이지 57

Chapter 3. 프롬프트엔지니어링심화
프롬프트 엔지니어링 심화 기법 핵심 포인트
Generate Retrieval
Prompt Tree of
Knowledge Augmented
Chaining Thoughts
Prompting Generation
트리 구조를 이용하여 AI
AI 모델이 스스로 지식을 여러 프롬프트를 연결하여 검색 기능활용하여 AI
모델이 다양한 사고 경로를
생성하도록 유도하는 기법 복잡한 작업 수행 모델이 보다 정확한 답변을
탐색하도록 하는 기법
생성하도록 유도
프롬프트 체인의 개념과
지식 생성의 기본 원리 이해 사고 트리 구조 이해
역할
검색 기반 답변 생성 원리
단계별 프롬프트 설계 및
AI 모델의 지식 생성 능력
연결 방법 트리 기반 문제 해결 방법 검색 결과 활용 방법
향상

---

## 페이지 58

Chapter 3. 프롬프트엔지니어링심화
프롬프트 엔지니어링 심화 기법 핵심 포인트
Directional
Automatic Active(cid:13247)
Stimulus ReAct
Prompt
Prompt Engineer
Prompting
LLM이 스스로 프롬프트를 LLM 이 능동적으로 방향성을 가진 자극을 통해
행동 기반의 프롬프트
설계 하도록 하는 자동화 프롬프트를 생성하고 AI모델이 특정 목표를 향해
기법을 활용하여 AI모델이
기법 수정하는 기법 나아가도록 유도
반응하도록 유도
자동 프롬프트 생성법 능동적 프롬프트의 개념 방향성 자극의 원리
ReAct 원리와 활용 사례
특정 목표 지향적 행동 기반 프롬프트 설계
자동화 도구 사용법
프롬프트 설계 및 적용법

---

## 페이지 59

Chapter 3. 프롬프트엔지니어링심화
Reference
Liu, J., Liu, A., Lu, X., Welleck, S., West, P., Bras, R. L., ... & Hajishirzi, H. (2021). Generated knowledge prompting for commonsense reasoning. arXiv
preprint arXiv:2110.08387.
Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., & Narasimhan, K. (2024). Tree of thoughts: Deliberate problem solving with large language
models. Advances in Neural Information Processing Systems, 36.
Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP
tasks. Advances in Neural Information Processing Systems, 33, 9459-9474.
Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., ... & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey. arXiv
preprint arXiv:2312.10997.
Zhou, Y., Muresanu, A. I., Han, Z., Paster, K., Pitis, S., Chan, H., & Ba, J. (2022). Large language models are human-level prompt engineers. arXiv
preprint arXiv:2211.01910.
Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q. V., Zhou, D., & Chen, X. (2023). Large language models as optimizers. arXiv preprint arXiv:2309.03409.
Diao, S., Wang, P., Lin, Y., & Zhang, T. (2023). Active prompting with chain-of-thought for large language models. arXiv preprint arXiv:2302.12246.
Li, Z., Peng, B., He, P., Galley, M., Gao, J., & Yan, X. (2024). Guiding large language models via directional stimulus prompting. Advances in Neural
Information Processing Systems, 36.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2022). React: Synergizing reasoning and acting in language models. arXiv
preprint arXiv:2210.03629.
Source: https://docs.anthropic.com/claude/docs/chain-prompts
Source: https://www.hani.co.kr/arti/economy/it/1130935.html
Source: https://github.com/dave1010/tree-of-thought-prompting
source: https://docs.llamaindex.ai/en/latest/getting_started/concepts

---

## 페이지 60 (OCR)

Chapter 03. 
Prompt Engineering Applications 
Fast campus

---

## 페이지 61

Table of Contents
01 데이터 생성과 분류하기
02 코드 생성하기
03 Function Calling with LLMs

---

## 페이지 62 (OCR)

Chapter 03. 
Applications 
01. Data Generation 
Fastcampus

---

## 페이지 63

Chapter 3. 프롬프트엔지니어링심화
Generating Data
o LLM은 관련 텍스트(cid:13273)Coherent Text(cid:13274)를 생성하는 우수한 능력을 가짐
o 프롬프트 엔지니어링으로 고품질, 일관적인, 사실에 가까운 답을 생성할 수 있음
o 데이터 테스트 (cid:13704) 평가에 유용
o Sentiment Analysis
프롬프트:
sentiment analysis 를 위해 10개 예시 문장을 생성해. 예시는
＂긍정(cid:13362) 혹은 (cid:13361)부정(cid:13362) 에 해당하는 문장이어야 해.
## 개수:
(cid:13247) 부정: 2개
(cid:13247) 긍정 :8개
### Response Format:
Q: (cid:13968)문장(cid:13967)
A: (cid:13968)sentiment(cid:13967)

---

## 페이지 64

Chapter 3. 프롬프트엔지니어링심화
Generating Data
ü 생성된 내용의 다양성을 높이려면?
o Finetune (cid:13704) RAG 를 사용하지 않고 생성 결과 조정하기
o 프롬프트 엔지니어링만 으로 해결
Research Paper
TinyStories: How Small Can Language Models Be and Still Speak Coherent English? (cid:13273)2023(cid:13274)
(cid:13273)예시(cid:13274) Creative Writing
3(cid:13247)4세 아이가 이해할 만한 수준으로 동화 스토리 생성하기
(cid:13247) Parameter with high temperature
반복적인 단어, 문장 내용 깨짐, 문장 연결성 깨짐
(cid:13247) 1,500 2(cid:13247)3세 유아 수준 단어 준비(cid:13273)동사, 명사, 형용사 구분(cid:13274)
(cid:13247) 데이터 생성시 각각 1개의 품사 활용
(cid:13247) 데이터 생성시 대화, 줄거리 반전, 결말, 도덕적 교훈과 같은 잠재적 이야기 특징 활용
Eldan, R., & Li, Y. (2023). Tinystories: How small can language models be and astillspeak coherent english?.arXivpreprint arXiv:2305.07759.

---

## 페이지 65

Chapter 3. 프롬프트엔지니어링심화
Data Generation
o Prompt: Word List 사용
Write a short story (cid:13273)3(cid:13247)5 paragraphs(cid:13274) which only 3살 어린 아이가 쉽게 이해할 수 있는 아주 쉬운 단어를
uses very simple words that a 3 year old child 사용해서 3(cid:13247)5단락 정도의 이야기를 써줘.
would likely understand. The story should use the 이야기에는 동사 (cid:13275)random.choice(cid:13273)verbs(cid:13255)list(cid:13274)(cid:13276), 명사
verb (cid:13362)(cid:13275)random.choice(cid:13273)verbs(cid:13255)list(cid:13274)(cid:13276)(cid:13362), the noun (cid:13275)random.choice(cid:13273)nouns(cid:13255)list(cid:13274)(cid:13276)
(cid:13362)(cid:13275)random.choice(cid:13273)nouns(cid:13255)list(cid:13274)(cid:13276)(cid:13362) and the adjective 그리고 형용사 (cid:13275)random.choice(cid:13273)adjectives(cid:13255)list(cid:13274)(cid:13276) 를
(cid:13362)(cid:13275)random.choice(cid:13273)adjectives(cid:13255)list(cid:13274)(cid:13276)(cid:13362). The story 사용해야 해.
should have the following features: 다음 특징을 꼭 반영해
(cid:13275)random.choice(cid:13273)features(cid:13255)list(cid:13274)(cid:13276), (cid:13275)random.choice(cid:13273)features(cid:13255)list(cid:13274)(cid:13276).
(cid:13275)random.choice(cid:13273)features(cid:13255)list(cid:13274)(cid:13276). 꼭 쉬운 단어를 사용해야 해.
Remember to only use simple words!
Eldan, R., & Li, Y. (2023). Tinystories: How small can language models be and astillspeak coherent english?.arXivpreprint arXiv:2305.07759.

---

## 페이지 66

Chapter 3. 프롬프트엔지니어링심화
Prompt 사용 결과
Story generated by gpt(cid:13247)3.5
Write a short story (3-5 paragraphs) which only uses very simple words that a 3 year old child would likely
understand. The story should use the verb ”decorate”, the noun ”thunder” and the adjective ”ancient”.
The story should have the following features: the story should contain at least one dialogue, the story has a bad
ending. Remember to only use simple words!
Eldan, R., & Li, Y. (2023). Tinystories: How small can language models be and astillspeak coherent english?.arXivpreprint arXiv:2305.07759.

---

## 페이지 67

Chapter 3. 프롬프트엔지니어링심화
반복적인 합성 데이터 생성
Iterative Synthetic Data Generation
구조 이용하기
Prompt
o Summary: (cid:13275)a short summary generated by LLM(cid:13276)
o Features: (cid:13275)copy the features from the initial prompt(cid:13276)
Entity
o Sentence: (cid:13275)a sentence generated by LLM, which should be present in the story(cid:13276)
사용
o Words: (cid:13275)copy the words from the initial prompt(cid:13276)
o Story:
Eldan, R., & Li, Y. (2023). Tinystories: How small can language models be and astillspeak coherent english?.arXivpreprint arXiv:2305.07759.

---

## 페이지 68

Chapter 3. 프롬프트엔지니어링심화
Prompt 생성 결과
요약 : (cid:13275)LLM이 생성한 짧은 요약을 내용에 포함 (cid:13276)
특징: (cid:13275) 내용에 반전이 있어야 함(cid:13276)
문장: (cid:13275)구어체 (cid:13276)
단어: (cid:13275)한국어 의성어, 의태어 많이 사용(cid:13276)
이야기: (cid:13275)중국으로 간 팬더 푸바오의 하루(cid:13276)
Standard Prompting
Structured Prompting

---

## 페이지 69 (OCR)

Chapter 03. 
Applications 
02. Code Generation 
Fastcampus

---

## 페이지 70

Chapter 3. 프롬프트엔지니어링심화
Code Generation
o LLM은 코드 생성과 수정에 뛰어난 성능을 보임
o System Message 를 사용하여 코드 생성과 수정 연습
Prompt
System
너는 나의 코드작성 도우미야.
나는 주니어 개발자야. 파이썬 언어를 설명해줘.
코드에 대해 설명할 필요없어. 필요한 부분에서
코드 블록을 생성해줘.

---

## 페이지 71

Chapter 3. 프롬프트엔지니어링심화
Code Generation
User message
Prompt
"""1. 영화 리스트 생성
2. 영화리스트의 별점 리스트 생성
System
3. 영화 10개와 별점을 포함한 json 응답형태."""
너는 나의 코드작성 도우미야.
나는 주니어 개발자야. 파이썬 언어를 설명해줘.
코드에 대해 설명 할 필요 없어.
코드 블록만 생성해줘.

---

## 페이지 72 (OCR)

Chapter 03. 
Applications 
03. Function Calling w/h LLM 
Fast campus

---

## 페이지 73

Chapter 3. 프롬프트엔지니어링심화
Function Call
o OpenAI 2023년 6월 발표
o API 사용 시 (cid:13361)functions(cid:13362) 파라미터로 기능 목록 제공하면 GPT가 판단 후 해당 function사용
o 함수와 파라미터를 json 형식으로 응답
o ChatGPT Plugin (cid:13247) Function Call 사용
Image source: https://gradientflow.substack.com/p/expanding-ai-horizons-the-rise-of

---

## 페이지 74

Chapter 3. 프롬프트엔지니어링심화
Function Call
1. Model : 사용 할 모델명 입력
2. Functions: 각 function 별로 다음 key 를 가짐
Key 선택사항 타입 설명
name required string Function 이름. a(cid:13247)z, A(cid:13247)Z, 0(cid:13247)9, (cid:13247) 로 표현 가능 64가 최대 길이
description optional string Function 이 무슨 일을 하는지에 대한 설명
parameters optional object 함수가 허용하는 매개 변수

---

## 페이지 75

Chapter 3. 프롬프트엔지니어링심화
Function Call
3. function_call
모델이 Function calling 에 응답하는 방식을 설정
ü Functions, function(cid:13255)call 은 system message 에 포함, token으로 추가
Key 설명
none Function calling 을 사용하지 않음, function 이 없을 시, 디폴트 값
auto 모델이 function calling 을 선택하도록 함. Function 이 있을 시, 디폴트 값
(cid:13275)(cid:13361)name(cid:13362): (cid:13362)my(cid:13255)function(cid:13362)(cid:13274) 모델이 my(cid:13255)function 이란 함수를 call 하도록 함

---

## 페이지 76

Chapter 3. 프롬프트엔지니어링심화
Open API 사용하기 위한 데이터 정의
Functions 정의
User Input: 서울 날씨는 어때?
Function: get_current_weather
Parameter: location, Unit

---

## 페이지 77

Chapter 3. 프롬프트엔지니어링심화
04. OpenAI의 GPT 모델에 대화와 함수
정보를 전달하고 응답받기

---

## 페이지 78 (OCR)

Chapter 3. 프롬프트 엔지니어링 심화 
05. GPT가 요청한 함수 실행 
함수 
"location": "서울" 
"temperature" : "24" 
"unit": "섭씨" 
"forecast" : [ 
"sunny" 
"windy" 
Fast campus

---

## 페이지 79

Chapter 3. 프롬프트엔지니어링심화
Function Call
User Input: 날씨는 어때?
Response: {
‘role’ : ‘assistant’,
’content’: 어느 도시나 지역의 날씨를 알고 싶으신가요?
}

---

## 페이지 80

Chapter 3. 프롬프트엔지니어링심화
Function Call
User Input: 서울 날씨는 어때?
Response: {
‘role’ : ‘assistant’,
’content’: None,
‘function_call’ : {
‘name’ : ‘get_current_weather’,
‘argument’:
‘{\n "location": "서울",\n “format” : “Celsius” \n}’
}
}
o Argument: 함수가 무엇을 해야하는지 설명하는 부분
o Location: 날씨를 확인하고 싶은 장소

---

## 페이지 81

Chapter 3. 프롬프트엔지니어링심화
Function Call
사용 용도
장점
oQuestion Answering 챗봇
1. 자연어로 JSON 데이터 얻기
o자연어 API호출로 변환
2.더 짧은 프롬프트로 토큰 절약
o텍스트에서 구조화된 데이터 추출
Source: https://platform.openai.com/docs/guides/function-calling

---

## 페이지 82

Chapter 3. 프롬프트엔지니어링심화
Function Call
한계점
o 프롬프트 인젝션
중요한 정보는 파라미터 설정에 넣지 않기, 테스트를 통해 호출 결과 확인
o 호출 오류
응답 결과 확인 필요성
요청하지 않은 함수 호출 발생 (cid:13273)add, delete(cid:13274)
o 내용 정확성 떨어짐
Source: https://platform.openai.com/docs/guides/function-calling

---

## 페이지 83

Chapter 3. 프롬프트엔지니어링심화
Reference
Eldan, R., & Li, Y. (2023). Tinystories: How small can language models be and astill speak coherent english?. arXiv preprint
arXiv:2305.07759.
Source
https://imnews.imbc.com/replay/2024/nwdesk/article/6604899_36515.html
https://techbukket.com/blog/chatgpt-api-guide
https://platform.openai.com/docs/guides/text-generation/function-calling

---
