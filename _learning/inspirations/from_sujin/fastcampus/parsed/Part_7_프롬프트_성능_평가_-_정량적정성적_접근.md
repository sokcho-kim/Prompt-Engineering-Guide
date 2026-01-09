# Part 7. 프롬프트 성능 평가 - 정량적·정성적 접근

> 파싱 일시: 2026-01-09 17:59:24
> 총 페이지: 24
> 텍스트 추출 성공: 19
> OCR 필요: 5

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering
Chapter 03.
Part 07. 프롬프트 성능 평가: 정량적·정성적 접근

---

## 페이지 2

Prompt EngineeringA to Z
프롬프트 평가의 역할과 중요성
프롬프트 엔지니어링 A to Z
프롬프트 평가 방법론
Chapter 03
정성적 프롬프트 평가 방법: 심층 분석 방법
Part 07. 프롬프트 성능 평가:
정량적·정성적 접근
정량적 프롬프트 평가 전략(cid:13205) 성능 지표 설정 및 측정
파일럿 평가를 통한 프롬프트 최적화

---

## 페이지 3

Chapter 03.프롬프트성능평가: 정량적·정성적접근
• 프롬프트 평가의 역할과 중요성
- 정답이없는프롬프트의경우, 어떤기준을사용할것인가?
- 프롬프트를과연평가할수있을까?
- 답변이텍스트형태이므로텍스트를기준으로평가를해야할까?”
- 답변이질문에얼마나정확하게답했는지를기준으로평가해야할까?”
Performance
Quality Assurance
Optimization
Cost Efficiency User Experience

---

## 페이지 4

Chapter 03.프롬프트성능평가: 정량적·정성적접근
LLM(cid:13247)as(cid:13247)a(cid:13247)judge
where an LLM is used for evaluating the prompts based on the answers it produced
with a certain model, according to predefined criteria.
Image source: https://aws.amazon.com/blogs/machine(cid:13247)learning/evaluating(cid:13247)prompts(cid:13247)at(cid:13247)scale(cid:13247)with(cid:13247)prompt(cid:13247)management(cid:13247)and(cid:13247)prompt(cid:13247)flows(cid:13247)for(cid:13247)amazon(cid:13247)bedrock/

---

## 페이지 5

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Judging LLM-as-a-Judge with MT-Bench and
Research Paper:
Chatbot Arena (2023)
• “LLM as a judge” for automated evaluation
• explores the feasibility and pros/cons of using various LLMs (GPT-4, ClaudeV1, GPT-3.5) as the judge
for tasks in writing, math, and world knowledge.
o 문제점: 기존 평가 기준이 대형 언어 모델의 성능을 충분히 반영하지 못하고 있으며, 특히
인간 선호와의 불일치가 발생함.
o 해결 방안: 인간의 선호에 맞춘 평가를 위해 LLM을 판사로 활용하는 LLM-as-a-Judge 방식을
도입. GPT-4와 같은 모델이 인간 평가와 높은 일치도를 보여줌.
o 평가 방법: 두 가지 새로운 벤치마크, 즉 MT-Bench와 Chatbot Arena를 도입하여 다중 회차
대화 및 지시 수행 능력을 평가하고, 이를 통해 인간 선호에 얼마나 잘 맞추는지 확인.
o 결과: GPT-4 등 강력한 LLM들이 인간 평가와 80% 이상의 일치도를 보이며, 인간 평가자
간의 일치도와 유사함.
o 한계점: 평가 과정에서의 한계점. 안정성, 정확성, 창의성 보완
Reference: Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. and Zhang, H., 2023. Judging llm(cid:13247)as(cid:13247)a(cid:13247)judge with mt(cid:13247)bench and
chatbot arena.Advances in Neural Information Processing Systems,36, pp.46595(cid:13258)46623.

---

## 페이지 6

Chapter 03.프롬프트성능평가: 정량적·정성적접근
o 성능 차이가 클수록 (즉, 한 모델이 더 우수할수록),
GPT-4와 인간 평가자의 일치율이 높아지는 경향
o 성능 차이가 작을 때는 일치율이 약 70%로 나타나지만,
성능 차이가 커질수록 100%에 가까워짐
o GPT-4가 모델 간 큰 성능 차이가 있을 때, 인간 평가자와
매우 유사한 평가를 내린다는 것을 시사
X축: 두 모델 간의 승률 차이.
Y축: GPT-4와 인간 평가자 간의 일치율.
Reference: Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. and Zhang, H., 2023. Judging llm(cid:13247)as(cid:13247)a(cid:13247)judge with mt(cid:13247)bench
and chatbot arena.Advances in Neural Information Processing Systems,36, pp.46595(cid:13247)46623.

---

## 페이지 7

Chapter 03.프롬프트성능평가: 정량적·정성적접근
o 다양한 모델들의 승률을 GPT-4와 인간 평가자가 평가한 데이터를 비교
o GPT-4의 판정이 인간 판정과 유사하게 유지
Reference: Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. and Zhang, H., 2023. Judging llm(cid:13247)as(cid:13247)a(cid:13247)judge with mt(cid:13247)bench
and chatbot arena.Advances in Neural Information Processing Systems,36, pp.46595(cid:13247)46623.

---

## 페이지 8 (OCR)

Chapter 03. 프롬프트 성능 평가: 정량적·정성적 접근 
Chatbot Arena 
Arena (battle) ☆ Arena (side-by-side) Direct Chat Leaderboard About Us 
Chatbot Arena (formerly LMSYS): Free AI Chat to Compare & Test Best AI Chatbots 
Blog I GitHub I Paper I Dataset I Twitter I Discord I Kaggle Competition 
New Launch! Jailbreak models at RedTeam Arena. 
How It Works 
。 Blind Test: Ask any question to two anonymous AI chatbots (ChatGPT, Gemini, Claude, Llama, and more). 
。 Vote for the Best: Choose the best response. You can keep chatting until you find a winner. 
。 Play Fair: If AI identity reveals, your vote won't count. 
NEW Image Support: Upload an image to unlock the multimodal arena! 
Chatbot Arena LLM Leaderboard 
。 Backed by over 1,000,000+ community votes, our platform ranks the best LLM and AI chatbots. Explore the top AI models on our LLM leaderboard! 
Chat now! 
Expand to see the descriptions of 75 models 
ModelA Model B 
Fast campus

---

## 페이지 9 (OCR)

Chapter 03. 프롬프트 성능 평가: 정량적·정성적 접근 
Rank* Arena Knowledge 
Model ▲ ▲ 95% CI ▲ Votes ▲ Organization ▲ License ▲ 
(UB) Score Cutoff 
1 01-preview 1339 +6/-7 9169 OpenAI Proprietary 2023/10 
1 ChatGPT-4o-latest. (2024-09-03) 1337 +4/-4 16685 OpenAI Proprietary 2023/10 
3 o1-mini 1314 +6/-5 9136 OpenAI Proprietary 2023/10 
4 Gemini-1.5-Pro-Exp-0827 1299 +4/-3 31928 Google Proprietary 2023/11 
4 Grok-2-08-13 1293 +4/-3 27731 xAI Proprietary 2024/3 
6 GPT-4o-2024-05-13 1285 +3/-3 93428 OpenAI Proprietary 2023/10 
7 GPT-4o-mini-2024-07-18 1272 +3/-3 33166 OpenAI Proprietary 2023/10 
7 Claude..3..5..Sonnet 1269 +3/-3 67165 Anthropic Proprietary 2024/4 
7 Gemini-1.5-Flash-Exp-0827 1269 +3/ -4 25027 Google Proprietary 2023/ 11 
7 Grok-2-Mini-08-13 1268 +4/-4 24956 xAI Proprietary 2024/3 
Gemini.. Advanced..App.. (2024-05- 
7 1266 +3/-3 52218 Google Proprietary Online 
14). 
MetaiLlama-3.1-495b-Instruct: 
7 1266 +6/-7 8787 Meta Llama 3.1 Community 2023/12 
b.f1.6. 
Meta-Llama-3.1-405b-Instruct: 
7 1266 +4/-4 33654 Meta Llama 3.1 Community 2023/12 
fp8 
8 GPT-4o-2024-08-06 1264 +4/ -3 25215 OpenAI Proprietary 2023/10 
Fast campus

---

## 페이지 10 (OCR)

Chapter 03. 프롬프트 성능 평가: 정량적·정성적 접근 
More Statistics for Chatbot Arena (Overall) 
Figure 2: Average Win Rate Against All Other Models (Assuming Uniform Sampling and No 
Figure 1: Confidence Intervals on Model Strength (via Bootstrapping) 
Ties) 
1340 0.64 
0.64 
0.6 0.60 
0.59 
0.58 
0.56 
1320 0.55 
0.53 
0.52 
0.5 
0.52 
Rate 
0.49 
0.49 
0.48 
0.48 
0.47 
0.47 
0.47 
0.46 
0.46 
0.45 
Rating 
1300 호 + uiM 0.4 0.41 
0.42 
0.40 
호 
호 0.33 
Average 
0.3 0.31 
1280 
호 
王 호 호 호 0.2 
호 
1260 호 · 호 
호 王 호 0.1 
1240 
llama-3.1-405b-instruct-bf16 
llama-3.1-405b-instruct-fp8 
llama-3.1-70b-instruct 
grok-2-2024-08-13 
gpt-4o-2024-08-06 
gpt-4-turbo-2024-04-09 
gpt-4o-mini-2024-07-18 
gpt-4o-2024-05-13 
grok-2-mini-2024-08-13 
gemini-advanced-0514 
qwen2.5-72b-instruct 
gemini-1.5-flash-exp-0827 
chatgpt-4o-latest-20240808 
gpt-4-1106-preview 
gemini-1.5-pro-api-0514 
gemini-1.5-pro-exp-0801 
chatgpt-4o-latest-20240903 
gemini-1.5-pro-api-0409-preview 
01-preview 
o1-mini 
gemini-1.5-pro-exp-0827 
claude-3-5-sonnet-20240620 
deepseek-v2.5 
mistral-large-2407 
athene-70b-0725 
0 llama-3.1-405b-instruct-fp8 
gpt-3.5-turbo-0314 
gpt-4o-2024-05-13 
gpt-4-0314 
grok-2-2024-08-13 
gpt-4o-mini-2024-07-18 
gpt-4-turbo-2024-04-09 
gpt-4-1106-preview 
chatgpt-4o-latest-20240808 
gemini-advanced-0514 
claude-3-opus-20240229 
gemini-1.5-pro-exp-0801 
gemini-1.5-pro-api-0409-preview 
claude-3-5-sonnet-20240620 
chatgpt-4o-latest-20240903 
o1-mini 
yi-large-preview 
gpt-4-0125-preview 
claude-1 
claude-3-sonnet-20240229 
bard-jan-24-gemini-pro 
01-preview 
gemini-1.5-pro-exp-0827 
gemini-1.5-pro-api-0514 
claude-2.0 
Model 
Model 
Fast campus

---

## 페이지 11 (OCR)

Chapter 03. 프롬프트 성능 평가: 정량적·정성적 접근 
More Statistics for Chatbot Arena (Overall) 
Figure 3: Fraction of Model A Wins for All Non-tied A vs. B Battles Figure 4: Battle Count for Each Combination of Models (without Ties) 
Model B Model B 
gemini-1.5-pro-api-0409-preview qwen2.5-72b-instruct gpt-4-turbo-2024-04-09 deepseek-v2.5 mistral-large-2407 
1mm-55mm:5mm 
chatgpt-4o-latest-20240808 gemini-1.5-pro-exp-0827 gemini-1.5-pro-exp-0801 grok-2-2024-08-13 gpt-4o-2024-05-13 gpt-4o-mini-2024-07-18 claude-3-5-sonnet-20240620 gemini-1.5-flash-exp-0827 grok-2-mini-2024-08-13 llama-3.1-405b-instruct-bf16 llama-3.1-405b-instruct-fp8 gemini-1.5-pro-api-0514 
chatgpt-4o-latest-20240903 
chatgpt-4o-latest-20240903 chatgpt-4o-latest-20240808 gemini-1.5-pro-exp-0827 gemini-1.5-pro-exp-0801 grok-2-2024-08-13 gpt-4o-2024-05-13 gpt-4o-mini-2024-07-18 claude-3-5-sonnet-20240620 gemini-1.5-flash-exp-0827 grok-2-mini-2024-08-13 gemini-1.5-pro-api-0514 gemini-1.5-pro-api-0409-preview qwen2.5-72b-instruct gpt-4-turbo-2024-04-09 deepseek-v2.5 mistral-large-2407 gpt-4-1106-preview athene-70b-0725 o1-preview o1-mini 
1mm-150mm 
gemina-canca-153016 
gemina-cancai@-036.g 
lame-13-1507-1001-11 
Ilama-3.1-70b-instruct 
gpt-1-p-90-1-1-46 
gpt-4o-2024-08-06 
gpt-4o-2024-08-06 
athen-10---20-0 
o1-preview o1-mini 
01-preview 1.달 0.52 0.56 0.62 0.63 0.60 0.62 0.66 0.59 0.70 0.65 0.71 4.3% 1.66 0.75 8.70 0.69 4.72 0.76 0.71 01-preview · 242 · 175 160 I 213 136 140 23승 066 15) 8 164 113 139 136 a 188 59 172 134 60 39 122 
chatgpt-4o-latest-20240903 0.48 0.55 0.56 0.5을 0.60  0.30 0:65 0.60 0.69 0.69 146 0.70 0.66 4.33 0.09 0.71 0.74 4,00 0.75 10 chatgpt-4o-latest-20240903 242 a 135 343 343 I 399 251 360 417 343 300 I 10승 365 247 2개 153 167 20kg 363 L34 160 369 
chatgpt-4o-latest-20240808 0.45 0.49 0.54 0.53 0.61 0.65 0.51 0.61 0.61 0.62 0.61 0.71 0.63 161 0.67 0.64 0.55 0.62 chatgpt-4o-latest-20240808 · 126 가입도 623 733 H 936 617 620 LOS 201 663 Hi 3500 
o1-mini 0.47 0.44 0.53 0.61 0.64 0.59 0.5k 0.61 0.63 0.5일 0.61 0.56 0.54 0.64 0.70 1.63 0.54 0.53 DLES 1.63 o1-mini 135 241 177 1.96 127 효과 210 133 153 116 150 60 37 121 
gemini-1.5-pro-exp-0827 168 347 177 애로도 344 614 일에줄 202 270 61 157 201 ssa BOO 
gemini-1.5-pro-exp-0827 0.44 0.41 0.55 0:47 0.56 0.51 0.52 0.62 6.57 0.51 0.56 a 5등 0.55 0.57 0.60 161 ☆ 验 65 0.62 0.5도 0.60 0.7 
gemini-1.5-pro-exp-0801 0.46 용사 0 52 0.53 0.56 0.57 0 54 0.59 0.55 263 0.61 0.61 0.62 0.59 1.62 gemini-1.5-pro-exp-0801 · a 766 415 285 715 SHG 입술 204 294 300 239 233 424 3000 
grok-2-2024-08-13 213 200 그들도 a 도움을 459 653 650 271 LIV 344 497 
grok-2-2024-08-13 0.38 0.40 0.4을 0.39 0.48 0.53 0.55 0.55 a 55 0.53 0.52 0.58 도움 0.57 0.63 
gpt-4o-2024-05-13 136 251 - 625 456 456 156 144 536 620 
gpt-4o-2024-05-13 0.32 6.23 0.39 0.36 a ◀을 6:47 · 도도 0.54 · 요 6.50 0.51 0.47 0.53 0.59 a 54 0.61 0.56 0.60 2.60 
gpt-4o-mini-2024-07-18 140 360 131 L14 635 150 367 274 JN 121 송크림 412 - 419 609 
2500 
gpt-4o-mini-2024-07-18 0.35 0.30 0.35 0.41 0.28 0 제도 Q 51 0.51 0.54 0.50 I 53 0.54 0.52 0.55 0.53 0.56 0.58 0.6 238 417 量59 105 F18 - G48 676 
claude-3-5-sonnet-20240620 
claude-3-5-sonnet-20240620 0.38 0.25 0.39 0:42 0.43 (AI 0 45 50 0. 50 0.51 0 53 0.51 0.54 도둑 a 51 : 세 0.57 4.57 0.51 1.54 gemini-1.5-flash-exp-0827 166 HI 456 367 LLS 그들에 426 
grok-2-mini-2024-08-13 153 309 371 406 374 625 2월3 477 
A gemini-1.5-flash-exp-0827 내 0.21 0.39 0.39 0.48 6.39 · 서도 0.49 · 세종 S4 51 0.49 151 4.51 a 55 2 44 ☆ 도도 16 0.52 4.50 タ 
2000 
grok-2-mini-2024-08-13 0.45 0.31 0.39 0.37 0.44 0.44 0.39 0.50 · 내용 6.50 Q 46 50 1 속도 0.47 0.55 2 52 a 되 a S a 도둑 3.45 0.62 1.51 gemini-advanced-0514 · 300 a 200 796 160 171 
Model 
gemini-advanced-0514 0.45  0.49 a 44 0.51 43 3.제동 0.52 1.53 0.53 4.5) 0.5 Ilama-3.1-405b-instruct-bf16 164 509 167 229 156 121 196 177 ELS 
llama-3.1-405b-instruct-bf16 0.38 0.31 0.28 0.41 0.45 0.42 0.53 a 45 0.세요 a 54 C. 50 52 0.47 5 제5 0.55 ☆ 16 : S& 스터 0.60 0.49 1.49 Model 
llama-3.1-405b-instruct-fp8 113 SOS 
llama-3.1-405b-instruct-fp8 35 0.32 0.39 0.39 0.43 0.AL 0.47 0.47 · 46 0.47 a 4등 0.52 0 53 0.세요 0.50 을 54 0.54 0.52 4.54 0.54 1.46 0.55 1.54 gpt-4o-2024-08-06 139 247 465 322 506 세12 663 443 261 412 699 1500 
gpt-4o-2024-08-06 0.39 0.30 0.39 0.46 0.40 BAG a 서울 도와 0.세요 Q 51 a S4 0.4) 0.52 0.60 0.53 0.56 0.51 1.53 gemini-1.5-pro-api-0514 136 491 670 고도술 473 Sine 
gemini-1.5-pro-api-0514 0.30 0.34 0.38  0.38 42 0.45 4등  0.53 0.52 I 46 0.52 1.54 0.52 0.54 0.4 gemini-1.5-pro-api-0409-preview a E a a a 
gemini-1.5-pro-api-0409-preview 0.51 0.53 qwen2.5-72b-instruct 효율 103 70 150 R3 1000 
qwen2.5-72b-instruct 0.29 4가 소세도 a 46 회계를 46 45 0 46 0.53 그 4) 0.58 0.52 0.43 4의 gpt-4-turbo-2024-04-09 59 15 464 ist 319 251 233 412 
gpt-4-turbo-2024-04-09 0.35 0.31 0.10 6.20 0.42 0.39 0.40 0.40 a 세을 6세일 45 0.49 46 0.44 : 서울 0.49 8 48 0.49 a 43 a 요 0.53 소의 0.52 4.50 deepseek-v2.5 133 309 153 67 152 106 101 편집 503 
deepseek-v2.5 0.30 0.29 0.39  0.45 0.39 0.35 0.40 0.51 0.56 0.45 041 141 0.40 0.54 1 세울 a 세요 0.57 0.50 0.42 4.52 0.3 mistral-large-2407 134 363 소도의 " 346 601 534 516 121 173 336 540 500 
mistral-large-2407 0.35 0.26 0.33 0.36 0.35 0.39 0.42 0.39 0.45 0.43 a 45 0.45 。 서울 0.45 a 46 0.4? 소개를 0.57 0.47 0.43 0.50 0.세요 4.5) gpt-4-1106-preview 60 124 201 仙 201 230 177 606 251 4.19 业 16 451 60 037 44 173 · 158 210 
gpt-4-1106-preview 0.38 0.20 0.35 0.40 0.38 6.27 0.35 0.44 0.43 0.43 0.17 6.51 0.47 0.40 0.51 0.41 1.46 0.47 0.49 4.56 0.50 0.59 4.57 athene-70b-0725 28 261 603 27 SS6 233 344 536 419 546 234 290 160 80 431 322 336 1.58 · 120 
athene-70b-0725 0.34 0.25 0.35 6.35 0.25 EAL 0.43 0.40 0.44 6.49 0.48 0.47 0.51 0.45 0.49 조세를 0.49 2,60 0.52 0.41 4.9 Ilama-3.1-70b-instruct 132 2·6승 943 121 100 434 497 630 609 675 426 477 171 LIS 506 659 되셔 a 13 482 103 도4점 210 338 0 
0 
llama-3.1-70b-instruct 0.39 0.38 0.37 0.40 0.39 0.38 6.40 0.42 0:46 0.43 0.49 0.43 0.51 0.46 0.47 0.46 조제를 0.50 1.43 0.47 1.43 0.47 
Fast campus

---

## 페이지 12

Chapter 03.프롬프트성능평가: 정량적·정성적접근
The original prompt used in the lmsys paper:
Please act as an impartial judge and evaluate the quality of the response provided by
an AI assistant to the user question displayed below. Your evaluation should consider
factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of
detail of the response. Begin your evaluation by providing a short explanation. Be as
objective as possible. After providing your explanation, you must rate the response
on a scale of 1 to 10 by strictly following this format.

---

## 페이지 13

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Prompt Evaluation Template
You're an evaluator for the prompts and answers provided by a generative AI model.
Consider the input prompt in the <input> tags, the output answer in the <output>
tags, the prompt evaluation criteria in the <prompt_criteria> tags, and the answer
evaluation criteria in the <answer_criteria> tags.
<input>
{{input}}
</input>
<output>
{{output}}
</output>
<prompt_criteria> - The prompt should be clear, direct, and detailed. - The question,
task, or goal should be well explained and be grammatically correct. - The prompt is
better if containing examples. - The prompt is better if specifies a role or sets a
context. - The prompt is better if provides details about the format and tone of the
expected answer.
</prompt_criteria>

---

## 페이지 14

Chapter 03.프롬프트성능평가: 정량적·정성적접근
<answer_criteria>
- The answers should be correct, well structured, and technically complete.
- The answers should not have any hallucinations, made up content, or toxic
content.
- The answer should be grammatically correct.
- The answer should be fully aligned with the question or instruction in the
prompt. </answer_criteria>
Evaluate the answer the generative AI model provided in the <output> with a score from 0 to 100 according to
the <answer_criteria> provided; any hallucinations, even if small, should dramatically impact the evaluation
score. Also evaluate the prompt passed to that generative AI model provided in the <input> with a score from 0
to 100 according to the <prompt_criteria> provided. Respond only with a JSON having:
- An 'answer-score' key with the score number you evaluated the answer with.
- A 'prompt-score' key with the score number you evaluated the prompt with.
- - A 'justification' key with a justification for the two evaluations you provided to the answer and the prompt;
make sure to explicitely include any errors or hallucinations in this part.
- An 'input' key with the content of the <input> tags.
- An 'output' key with the content of the <output> tags.
- A 'prompt-recommendations' key with recommendations for improving the prompt based on the
evaluations performed. Skip any preamble or any other text apart from the JSON in your answer.

---

## 페이지 15

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Prompt Evaluation Template_2
JUDGE_PROMPT = """ You will be given a user_question and system_answer couple. Your task is to provide
a 'total rating' scoring how well the system_answer answers the user concerns expressed in the
user_question.
Give your answer as a float on a scale of 0 to 10, where 0 means that the system_answer is not helpful at
all, and 10 means that the answer completely and helpfully addresses the question.
Provide your feedback as follows: Feedback::: Total rating: (your rating, as a float between 0 and 10) Now
here are the question and answer.
Question: {question}
Answer: {answer}
Feedback:::
Total rating:
"""
Reference:https://huggingface.co/learn/cookbook/en/llm_judge

---

## 페이지 16

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Unanswered Questions
1. Alignment w/h human grading : 문서 Q(cid:13704)A 챗봇
2. Accuracy through Examples
3. Appropriate Grade Scales : 서로 다른 프레임워크 Azure (cid:13273)0 to 100 scale(cid:13274),
langchain binary scale (cid:13273)0(cid:13247)1(cid:13274)
4. Applicability Across Use Cases: 동일한 평가 기준 다양한 사용 사례 재사용 가능성

---

## 페이지 17

Chapter 03.프롬프트성능평가: 정량적·정성적접근
• 프롬프트 평가 방법론 : 질적 및 양적 접근의 이해
Mutually
Complementary
Methodology
Qualiatiative
Quantitative
Interactional Linguistics
LLM & Prompt Engineering
Conversation Analysis
17

---

## 페이지 18 (OCR)

Chapter 03. 프롬프트 성능 평가: 정량적·정성적 접근 
Qualitative Analysis Quantitative Analysis 
(1) Linguistic (2) Human (3) LLM Response (4) Satisfaction 
Analysis Evaluation scoring Response 
to establish criteria for Scoring to assess the responses Evaluation 
assessing user to check whether there using the established to determine the most 
satisfaction with is some correlation 12 criteria. preferred response 
responses between LLM scores across five different 
and human judgment. LLMs. 
Fast campus

---

## 페이지 19

Chapter 03.프롬프트성능평가: 정량적·정성적접근
• 벤치마크 평가 방법과 사용자 중심 평가 방법
카테고리 벤치마크 평가 방법 사용자 중심 평가
데이터 소스 합성된 데이터 실제 사용자 데이터
데이터 셋 단일 문장 단일 및 다중 턴을 포함한 연속 턴 사용
인위적 문장
분석 초점 LLM 응답 효율성/추론 • 다양한 사용자 입력값에 대한 LLM응답의
적합성
• 사용자(cid:13247)AI 상호작용의 역동성
평가 방법 • 자동화된 메트릭스(cid:13273)ROUGE, • 대화 분석과 상호작용 분석 프레임
BLUE, METEOR(cid:13274) 워크LLM에 대한 사용자 만족/ 불만족
• 선호도 기반 점수 시스템 환경과 조건
• LLM 평가와 사람 평가의 응답 비교 분석

---

## 페이지 20

Chapter 03.프롬프트성능평가: 정량적·정성적접근
• 정성적 프롬프트 평가 기법: 심층 분석 방법
Linguistic Analysis
Identification of Common Linguistic Features
1.
Analysis of Discourse Contexts
2.
Categorization
3.
Text
Discourse
Culture

---

## 페이지 21

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Findings. 12 Criteria, including 10 Sub-criteria
Text(cid:13247)Level Presentation(cid:13247)Level
Interaction Level
Clarity Natural Language Acknowledgement of
understanding
Politeness
Empathy
Completeness
Confirmation and
Clarification Politeness
Coherence
Adaptability

---

## 페이지 22

Chapter 03.프롬프트성능평가: 정량적·정성적접근
• 정량적 프롬프트 평가 전략: 심층 분석 방법
Enhanced by Prompting
LLM 모델

---

## 페이지 23

Chapter 03.프롬프트성능평가: 정량적·정성적접근
Prompt 예시
Criteria: Acknowledgement
description = "A satisfying response might begin with acknowledging user’s question or input,
showing that the companion understood their request."
questions = [
{
"name": "paraphrasing",
"description": "Does the companion’s response begin by paraphrasing or summarizing the user’s
query to demonstrate understanding?",
},
{
"name": "overlook",
"description": "In cases of complex or multi-part questions, does the companion acknowledge each
component to ensure nothing is overlooked?",
},
{
"name": "clarification",
"description": "If the user’s input is ambiguous, does the companion seek clarification or
provide responses that cover potential interpretations, showing an effort to fully understand?",
},

---

## 페이지 24

Chapter 03.프롬프트성능평가: 정량적·정성적접근
파일럿 평가를 통한 프롬프트 최적화
(cid:13715) 결과 예시
• 결론 도출
(cid:13247) 한 턴에 대한 LLM의 평가 점수를 도출할 수 있다.
(cid:13247) 언어 모델의 답변에 대한 사용자의 만족도를 파악할 수 있다.
(cid:13247) 여러 언어 모델의 장단점 파악 할 수 있다.
(cid:13247) LLM별 프롬프트 제작 전략을 연구 할 수 있다.
• 결과 활용
- 프롬프트 정밀 분석을 통한 프롬프트 자동 생성기
- LLM모델 큐레이션 연구

---
