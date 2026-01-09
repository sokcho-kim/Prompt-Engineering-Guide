# Part 4. 프롬프트 제작의 기초 - 핵심 원리와 방법론 (Chapter 1)

> 파싱 일시: 2026-01-09 17:57:58
> 총 페이지: 70
> 텍스트 추출 성공: 63
> OCR 필요: 7

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering

---

## 페이지 2

Chapter 3. Part 4
프롬프트 테스트 환경 구축 및 최적화
Open AI Playground 사용법

---

## 페이지 3

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Open AI
Playground
1. Chat
2. Assistants
3. Completions

---

## 페이지 4

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Chat
o Chat Completions API 와 연계
o 최신 챗 모델을 사용할 수 있음 (gpt-4o, gpt-4 등)

---

## 페이지 5 (OCR)

Chapter 3. Part 04. 프롬프트 제작의 기초: 핵심 원리 
Assistants 
Playground New in Assistants API ↗ 日 Learn more 
① asst_o6VuHod0Sy9A9lYGplYm5S1Y 0 THREAD Logs □ 
Name 
Enter a user friendly name 
asst_ o6VuHodOSy9A9IYGplYm5S1Y 
Instructions 
You are a helpful assistant. 
Model 
gpt-4o 
TOOLS 
File search ① + Files 
Code interpreter ⓘ + Files 
Functions ① + Functions 
MODEL CONFIGURATION Enter your message... 
Responce form at + Run 36 ← 
Clone Updated 6/9, 4:28 PM 
Playground messages can be viewed by anyone at your organization using the API. 
Fast campus

---

## 페이지 6

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Assistants API 의 기본 요소
o Assistants(cid:13205) 모델(cid:13273)GPT(cid:13258)3.5, GPT(cid:13258)4, etc(cid:13274), instruction(cid:13273)지시문/프롬프트(cid:13274),
tools(cid:13273)도구(cid:13274), files(cid:13273)업로드한 파일(cid:13274)를 캡슐화
o 함수: 외부 API 호출을 추가할 수 있음 어시스턴트는 적절하다고 판단되면 이 함수를
호출함
o 코드 인터프리터: 어시스턴트가 필요에 따라 코드를 작성하고 실행할 수 있게 함
o 검색 및 파일: 업로드된 파일에서 필요한 정보를 검색할 수 있음
o Threads: 대화 채널. 메시지를 담음
o Runs: Assistant (cid:13961) Thread 실행. Run 단계에서 tools(cid:13273)도구(cid:13274) 의 활용 여부 결정
Run 을 수행한 후 Assistant 가 응답한 결과 처리

---

## 페이지 7

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Completions
o Open AI 가 처음 제공한 API, 레거시 컴플리션 모드
o babbage-002, davinci-002, gpt-3.5-turbo-instruct
세 가지 모델만 지원
o 채팅 모드가 아님
o 문장을 입력하면, 모델이 문장을 완성하려고 시도
(cid:13273)예시(cid:13274)

---

## 페이지 8

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Open AI
Playground
1. Temperature
2. Top P
3. Maximum Tokens
4. Frequency Penalty
5. Presence Penalty
6. Stop Sequence

---

## 페이지 9

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
생성 조건 이해하기
Open AI Playground
온도 (cid:13273)temperature(cid:13274) 빈도 패널티 (cid:13273)frequency(cid:13255)penalty(cid:13274)
최대 토큰 수 (cid:13273)max(cid:13255)tokens(cid:13274) 존재 패널티 (cid:13273)presence(cid:13255)penalty(cid:13274)
상위 p (cid:13273)top(cid:13255)p(cid:13274) 중지 시퀀스 (cid:13273)Stop Sequences(cid:13274)

---

## 페이지 10

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
토큰 (Token)
자연어처리에서 기본적으로 처리할 수 있는 언어의 (cid:13363)조각(cid:13380)이나 (cid:13363)단위(cid:13364)
프롬프트를 제작할 때는 토큰 수를 미리 예상 할 수 있어야함
토크 나이저 (Tokenizer) • 토크나이저를 사용하면 텍스트를 언어 모델이 처리할 수 있는 형식으로 변환함.
• 단어, 구두점 또는 단어의 일부를 개별 토큰으로 분할함.
영어 예시

---

## 페이지 11

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
토큰 (Token)
• 한국어와 같은 다른 언어를 처리할 때는 추가적인 토크나이징 과정을 거침
• 영어에서는 공백을 기준으로 단어를 구분하지만,
한국어에서는 음절, 형태소, 단어 등 다양한 기준으로 토큰화 할 수 있음
한국어 예시

---

## 페이지 12 (OCR)

Chapter 3. Part 04. 프롬프트 제작의 기초: 핵심 원리 
Predict the next token 
Input text Tokenize LLM Output Sample 
probabilities 
We 0.001 
ights 0.001 
[1135, 2337, 1222, 
Weights & Biases is 
8436, 1386, 318, & 0.001 machine 
the 
262] 
the 0.001 
machine 0.15 
learning 0.001 
platform 0.2 
Fast campus

---

## 페이지 13

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
온도 (cid:13273)Temperature(cid:13274)
높은 온도:
예시: 한국의 여름 거리를 묘사해줘.
모델에서 출력의 다양성을 조절하기 위해 사용함
값이 높을수록 모델이 더 많은 선택지를 가지고 있으며
결과적으로 더 다양한 텍스트를 생성함
낮은 온도일수록 모델이 더 확신 있게 예측을 한다
일반적으로 더 정확하고 일관된 텍스트를 생성함
낮은 온도:
예시: 한국의 여름 거리를 묘사해줘.

---

## 페이지 14

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
상위 Top P
모델이 다음 단어를 선택할 때 확률이 상위 P(cid:13984)에 해당하는
단어들만 고려하도록 하는 것
확률 분포의 상위 P(cid:13984)에 속하는 단어들만 후보로 선택하여
더 다양한 텍스트를 생성할 수 있음
Temperature를 매우 높게 했을 때
결과가 무너지는 것을 방지하기 위해 추가로 사용 가능
Source: Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration.arXivpreprint arXiv:1904.09751.

---

## 페이지 15

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
o 확률 분포가 넓은 경우 o 확률 분포가 좁은 경우

---

## 페이지 16

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Frequency Penalty
모델이 이전에 선택한 토큰이나 패턴과 비슷한 토큰을
다시 선택하는 것을 억제하는 옵션.
반복되는 패턴을 피하고 다양성을 유지하는 데 도움이 됨.
(cid:13273)예시(cid:13274)
이전 단어가 (cid:13379)사과(cid:13379)였을 때 모델이 다시
(cid:13379)사과(cid:13379)를 선택하지 않도록 하여 단어의 반복을 줄임.

---

## 페이지 17

Chapter 3. Part 04. 프롬프트제작의기초:핵심원리
Presence Penalty
Presence penalty는 특정 토큰 또는
패턴의 등장을 억제하는 데 사용
모델이 특정 토큰이나 패턴을 생성하지 않도록 하여
출력의 다양성을 높이고 원하는 결과를 얻을 수 있음
원하지 않는 단어나 특정 패턴의 등장을 줄이는데 유용

---

## 페이지 18

Chapter 03. Part 04
Prompt Engineering Techniques
Level : Basic (cid:13249) Advanced (cid:13247) Applications

---

## 페이지 19

Chapter 3
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
Active-Prompt, Directional Stimulus
•Self-consistency Prompting, React

---

## 페이지 20 (OCR)

Chapter 3 
Prompt Engineering Techniques 
Basic 
Fast campus

---

## 페이지 21

Course Objectives & Learning Outcomes
학습 목표
ü01
프롬프트 엔지니어링 기초 기법을 이해한다.
02
연구 논문을 통해 각 프롬프트 엔지니어링 기법의 핵심과 한계를 이해한다.
03
실습을 통해 각 프롬프트 엔지니어링 방법을 학습한다.

---

## 페이지 22

Table of Contents
01 Zero-Shot Prompting
02 Few-Shot Prompting
03 Chain-of-Thought Prompting
04 Self-Consistency

---

## 페이지 23

Chapter 3
The Basic Prompt Engineering Techniques
01. Zero(cid:13247)Shot Prompting
o Instruction-Tuning
o RLHF (Reinforcement Learning form Human Feedback)

---

## 페이지 24

Chapter 03. Part04.엔지니어링기법-Basic
Research Paper
Open AI : Language Models are Few-shot Learners (2020)
Figure 2.1: Zero-shot, one-shot and few-shot, contrasted with
traditional fine-tuning. The panels above show four methods for
performing a task with a language model – fine-tuning is the
traditional method, whereas zero-, one-, and few-shot, which we
study in this work, require the model to perform the task with only
forward passes at test time. We typically present the model with a
few dozen examples in the few shot setting.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... & Amodei, D. (2020). Language models are few-shot learners.Advances in neural information processing
systems,33, 1877-1901.

---

## 페이지 25

Chapter 03. Part 04. 엔지니어링기법-Basic
Zero-Shot Prompting
o 언어 모델에게 예제나 시연(cid:13273)Demonstrations(cid:13274) 을 주지 않고 작업을 수행하는 방법
o 언어 모델이 기존 지식을 사용하여 작업을 추론함
o 대량의 데이터를 사전 학습 했기 때문에 가능
제로샷 프롬프트는 언어 모델의 강력한 기능 중 하나
최소한의 정보만으로도 다양한 작업을 수행할 수 있음
이 기술은 특히 데이터가 부족한 상황에서 유용하게 활용됨

---

## 페이지 26

Chapter 03. Part 04. 엔지니어링기법-Basic
Example
o Text Classification o Translation o Closed Question Answering
Prompt: Prompt: Prompt:
다음 텍스트에서 긍정, 부정, 중립 중 다음 한국어 단어를 영어로 번역해줘. 대한민국의 수도는 서울이야?
하나로 분류해.
단어: 인공 눈물
텍스트(cid:13205) 나는 마라탕 맛이 그저 그랬어.
Sentiment:

---

## 페이지 27

Chapter 03. Part 04. 엔지니어링기법-Basic
o 제로샷 프롬프팅의 작동 방식
o 텍스트와 분류 예시를 모델에게 제공하지 않았는데도 정답을 맞춤

---

## 페이지 28

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
FINETUNED LANGUAGE MODELS ARE ZERO-SHOT LEARNERS (2022)
o 연구 개요: 대형 언어 모델의 제로 샷 학습 능력을 개선법 연구
자연어 지시로 60개 이상의 NLP 데이터셋에 대해 137B 파라미터 모델을 미세 조정
o 연구 결과 : 모델 FLAN은 제로샷 성능에서 기본 모델보다 우수함
Instruction Tuning 은 사전 학습 데이터 없이도 NLP 데이터셋에서 모델의 성능을 올림
Instruction Tuning
o 기술 개요
o 기술의 장점
o 언어 모델의 제로 샷 능력을 향상 시키기 위한 기술 o Instruction tuning 은 모델 크기가 충분할 때 효과적
o Instruction Tuning은 대형 언어 모델이 다양한 작업을 수행할 수 있도록 함
o 지시에 따라 모델의 응답을 미세 조정할 수 있음
o 다수의 작업 클러스터에서 Instruction tuning 시 (cid:13278)모델이 해보지 않은
o 챗봇이 더 정확하고 좋은 결과물을 얻어냄
작업에 대한 성능 향상
* 137B 는(cid:13361)B(cid:13362)는billion을의미한다.
Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., ... & Le, Q. V. (2021). Finetuned language models are zero-shot learners.arXivpreprint arXiv:2109.01652.

---

## 페이지 29

Chapter 03. Part 04. 엔지니어링기법-Basic
다양한 NLP 작업에서 우수한 성능을 보여주는 그래프
o FLAN 137B는 Zero(cid:13247)shot prompting 성능에서 다른 대형
언어 모델들보다 전반적으로 더 우수한 성능을 보임.
o 자연어 추론
FLAN 137B는 대부분의 작업에서 다른 모델보다 성능 좋음
o 독해
여러 모델이 유사한 성능을 보이지만, FLAN 137B는 여전히 우수한 성능을 보임
o 폐쇄형 QA
FLAN 137B와 다른 모델들이 유사한 성능을 보이는 작업도
있지만, FLAN 137B가 더 좋은 성능을 보이는 작업도 있음
o 번역
FLAN 137B는 몇 가지 번역 작업에서 다른 모델들보다 성능이 뛰어남
• X축 (cid:13273)가로축(cid:13274): 제로샷 성능, 값이 클수록 성능이 좋음
• Y축 (cid:13273)세로축(cid:13274): 테스트된 작업의 유형
• 작업 유형: 자연어 추론, 독해, 폐쇄형 QA

---

## 페이지 30

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
Deep reinforcement learning from human preferences (2017)
o 인간 피드백을 이용한 강화 학습(cid:13273)RL(cid:13274)
o 인간 선호도 기반 피드백으로 보상 함수 최적화
o 기존 보상 함수 설계 대신, 인간 피드백을 사용하여 더 나은 성능 달성
o 인간 피드백을 통한 RL의 효율성 입증
o 실제 환경에서의 복잡한 작업에 적용 가능성 제시
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human
preferences.Advances in neural information processing systems,30.

---

## 페이지 31

Chapter 03. Part 04. 엔지니어링기법-Basic
RLHF (Reinforcement Learning form Human Feedback)
o 인간의 피드백을 활용하여 모델의 응답을 개선
o Instruction Tuning 과 RLHF 와 함께 모델의 성능 향상
o ChatGPT 의 학습 방법

---

## 페이지 32

Chapter 03.
The Basic Prompt Engineering Techniques
02. Few(cid:13247)Shot Prompting

---

## 페이지 33

Chapter 03. Part 04. 엔지니어링기법-Basic
Few-Shot Prompting
o Zero(cid:13247)shot prompting 은 복잡한 문제 수행에 한계가 있음.
o Few(cid:13247)shot prompting : 언어 모델에게 예제나 시연(cid:13273)Demonstrations(cid:13274) 을 주며 작업을 수행하는 방법
Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., ... & Amodei, D. (2020). Language models are few-shot learners.arXivpreprint arXiv:2005.14165.

---

## 페이지 34

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
Open AI’s Research: Language Models are Few-Shot Learners (Brown et al. 2020)
o Few-shot prompting 은 모델의 파라미터 수가 충분히 클 때 효과가 있음
(Touvron et al. 2023, Kaplan et al., 2020)
X축: 예시의 수 (cid:13273)K(cid:13274)
Y축: 정확도 (cid:13273)(cid:13984)(cid:13274)
Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., ... & Amodei, D. (2020). Language models are few-shot learners.arXivpreprint arXiv:2005.14165.

---

## 페이지 35

Chapter 03. Part 04. 엔지니어링기법-Basic
Example
ü 어렵고 복잡한 과제일수록, 예제를 많이 사용하여 해결 할 수 있다.
Prompt:
A "whatpu" is a small, furry animal native to Tanzania.
An example of a sentence that uses the word whatpu is:
We were traveling in Africaand we saw these very cute whatpus.
To do a "farduddle" means to jump up and down really fast.
An example of a sentence that uses the word farduddle is:
Output:
When we won the game, we all started to farduddle in celebration.
Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., ... & Amodei, D. (2020). Language models are few-shot learners.arXivpreprint arXiv:2005.14165.

---

## 페이지 36

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
o Rethinking the Role of Demonstrations:
What Makes In-Context Learning Work? (2022)
연구 결과
o 예시 사용
예시를 사용하면 모델의 성능을 향상 시킴
o 예시의 품질 중요
정답 라벨 (cid:13273)Gold labels(cid:13274) 가장 좋지만, 랜덤 예시도 모델의 추론에 도움이 됨
o 프롬프트 포맷
올바른 입력(cid:13258)라벨 형식을 유지하는 것이 중요.
Work, W. M. I. C. L. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?.

---

## 페이지 37

Chapter 03. Part 04. 엔지니어링기법-Basic
o 분류 작업 : 예시의 중요성
• No demonstrations (cid:13273)예시없음(cid:13274)
• Demonstrations with gold labels (cid:13273)정답라벨이있는예시(cid:13274)
• Demonstrations with random labels (cid:13273)랜덤라벨이있는예시(cid:13274)
• Demonstrations with no input(cid:13247)label format (cid:13273)입력(cid:13247)라벨형식없음(cid:13274)
X축: 다양한 모델 및 평가 방법 Y축: 모델의 성능을 나타내는 지표
• Gold labels: 정답 라벨이 있는 예시를 사용한 경우 모델 성능이 가장 높음
• Random labels: 랜덤 라벨이 있는 예시를 사용해도 예시가 없는 경우보다는 성능이 좋음
• No input(cid:13247)label format: 입력(cid:13247)라벨 형식을 유지하지 않은 경우 성능이 크게 저하
Work, W. M. I. C. L. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?.

---

## 페이지 38

Chapter 03. Part 04. 엔지니어링기법-Basic
o 멀티 초이스 작업 : 라벨 형식의 중요성
• Gold labels: 정답라벨이있는예시
• Random labels: 랜덤라벨이있는예시
• Format variations without keeping the format:
• 형식을유지하지않은경우
• 입력(cid:13247)라벨 형식을 유지하는 것이 모델 성능을 최적화하는 데 필수적
• 형식을 유지하면 랜덤 라벨을 사용하더라도 좋은 성능을 보일 수 있음
Work, W. M. I. C. L. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?.

---

## 페이지 39

Chapter 03. Part 04. 엔지니어링기법-Basic
Format Example
Random Format
Prompt: Prompt:
부정 이건 정말 굉장해! 이건 정말 굉장해! // 부정
와 정말 나쁘다! 긍정 와 정말 나쁘다! // 긍정
그 영화 진짜 대박이더라. 그 영화 진짜 대박이더라. // 긍정
긍정 아우 정말 끔찍해
아우 정말 끔찍해(cid:13973)(cid:13973)
Output: Output:
부정 부정

---

## 페이지 40

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
Few-shot prompting
Few(cid:13247)shot prompting 기법을 사용해서
(cid:13361)오늘의 일기(cid:13362)를 네 줄 분량으로 작성해보세요
시작 문장의 포맷대로 출력해야 합니다
시작 문장
"나는 오늘 날씨가 좋아서 산책을 했다. 그리고 __."

---

## 페이지 41

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
Few-shot prompting
(cid:13361)(cid:13362)(cid:13362) 오늘의 일기를 작성해줘.
아침, 점심, 저녁, 취침 전 시간에 해당하는 문장을 써줘.
아래 예시를 참고해서 네 줄 만 써줘(cid:13362)(cid:13362)(cid:13362)
예시:
1. 아침: "나는 오늘 날씨가 좋아서 산책을 했다. 그리고 친구를 만났다.”

---

## 페이지 42 (OCR)

Chapter 03. Part 04. 엔지니어링 기법- Basic 
실습 
Chat Presets Save 』 <ノ> 
gpt-3.5-turbo こ Compare Temperature 0.1 
SYSTEM Maximum Tokens 400 
463939 오늘의 일기를 작성해줘. 아침, 점심, 저녁, 취침 전 시간에 해당하는 문장을 써줘. 아래 예시를 참고해서 네 줄 만 써 
줘"." 
Stop sequences 
Enter sequence and press Tab 
1.아침: "나는 오늘 날씨가 좋아서 산책을 했다. 그리고 친구를 만났다." 
USER Top P 1 
점심: 
저녁: 
Frequency penalty 0 
취침 전 : 
Presence penalty 0 
ASSISTANT 
점심: "점심에는 샐러드를 먹었는데 맛있어서 기분이 좋았다." 
저녁: "저녁에는 집에서 간단히 요리를 해먹었는데, 푹신한 침대가 그리웠다." ☑ API and Playground requests will 
취침 전: "취침 전에는 책을 읽으며 차 한 잔을 마시고 하루를 마무리했다." not be used to train our models. 
Learn more 
Fast campus

---

## 페이지 43

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
Few-shot prompting
이 그룹의 홀수들을 더하면 짝수가 됩니다(cid:13205) 4, 8, 9, 15, 12, 2, 1.
답(cid:13205) 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다(cid:13205) 17, 10, 19, 4, 8, 12, 24.
답(cid:13205) 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다(cid:13205) 16, 11, 14, 4, 8, 13, 24.
답(cid:13205) 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다(cid:13205) 17, 9, 10, 12, 13, 4, 2.
답(cid:13205) 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다(cid:13205) 15, 32, 5, 13, 82, 7, 1.
답(cid:13205)
A: 정답입니다. (X)

---

## 페이지 44

Chapter 03. Part 04. 엔지니어링기법-Basic
Few-shot Prompting 의 한계
But is still not a perfect technique,
복잡한 추론(cid:13273)Reasoning(cid:13274) 문제는 잘 하지 못함
ü Zero-shot prompting ü Few-shot prompting
Q: 이 그룹의 홀수를 더하면 짝수가 된다. 이 그룹의 홀수들을 더하면 짝수가 됩니다: 4, 8, 9, 15, 12, 2, 1.
15, 32, 5, 13, 82, 7, 1. 답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 10, 19, 4, 8, 12, 24.
A: 네, 이 그룹의 홀수들을 더하면 107이 되는데, 답: 참입니다.
이는 짝수입니다. 이 그룹의 홀수들을 더하면 짝수가 됩니다: 16, 11, 14, 4, 8, 13, 24.
답: 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 9, 10, 12, 13, 4, 2.
답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 15, 32, 5, 13, 82, 7, 1.
답:
A: 정답입니다.

---

## 페이지 45

Chapter 03.
The Basic Prompt Engineering Techniques
03. Chain(cid:13247)of(cid:13247)Thought
Prompting

---

## 페이지 46

Chapter 03. Part 04. 엔지니어링기법-Basic
Chain-of-Thought Prompting (CoT)
복잡한 과제 수행을 위해, LLM 에게 더 자세한 안내 문구를 작성해주는 것
o
복잡한 Task (cid:13273)Arithmetic, commonsense, and symbolic reasoning tasks(cid:13274)에 사용하면 효율적
o
중간 추론 단계를 거치도록 하는 문장으로 구성
o
답이 나오는 과정에 대해 설명한 예시를 보여주고,
문제를 풀기 위한 답을 생성할 때 예시와 같은
방식으로 LLM 이 설명하도록 하는 방식
Image Source: https://arxiv.org/pdf/2201.11903

---

## 페이지 47

Chapter 03. Part 04. 엔지니어링기법-Basic
Chain-of-Thought Prompting
Chain-of-Thought Prompting
Standard Prompting
모델입력(cid:13273)ModelInput(cid:13274)
Q(cid:13205) Roger는 테니스공 5개를 가지고 있습니다. 그는 테니스공 3개가 들어있는 캔을 2개
모델입력(cid:13273)ModelInput(cid:13274)
더 삽니다.Roger는 이제 테니스공을 몇 개 가지고 있습니까?
Q: Roger는 테니스공 5개를 가지고 있습니다. 그는 테니스공 3개가 들어있는
A(cid:13205)Roger는 5개의 공으로 시작했습니다.테니스공 3개가 들어있는 캔 2개를 더 샀습니다.
캔을 2개 더 삽니다.Roger는 이제 테니스공을 몇 개 가지고 있습니까?
5(cid:13992)6(cid:13996)11개.정답은11입니다.
A:정답은 11입니다.
Q(cid:13205) 카페테리아에 사과가 23개 있었습니다. 그들은 20개를 점심을 만드는 데 사용했고
6개를 더 샀습니다.이제 사과가 몇 개 있습니까?
Q: 카페테리아에 사과가 23개 있었습니다. 그들은 20개를 점심을
만드는 데 사용했고 6개를 더 샀습니다.이제 사과가 몇 개 있습니까?
ModelOutput
A:정답은 27입니다.❌
A(cid:13205) 카페테리아에 원래 사과가 23개 있었습니다. 그들은 20개를 점심을 만드는 데
사용했습니다. 그래서 23 (cid:13258) 20 (cid:13996) 3개가 남았습니다. 그들은 6개를 더 샀기 때문에,
ModelOutput
이제 3(cid:13992)6 (cid:13996)9개가 있습니다.정답은 9입니다.✔
A:정답은 27입니다.❌

---

## 페이지 48

Chapter 03. Part 04. 엔지니어링기법-Basic
Chain-of-Thought Prompting
CoT 를 사용하여 다양한 문제를 해결하는 예시
산술 문제, 상식 추론, 전략적 추론, 스포츠 이해, 날짜
이해, 감정 이해 등
Image Source: https://arxiv.org/pdf/2201.11903

---

## 페이지 49

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
Google Research (2022): Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- Arithmetic, symbolic, and commonsense reasoning 에서 CoT 기법의 성능 좋음
수학 단어 문제를 푸는 성능 비교
Y축(cid:13205) 문제 해결 비율(cid:13273)(cid:13984)(cid:13274)
X축(cid:13205) 모델 및 기법
o 연구 결과
Chain(cid:13247)of(cid:13247)Thought 을 사용했을 때 모델 성능 가장 크게 향상
Fine-tuned GPT-3 175B: 55%
PaLM 540B (standard prompting): 18%
PaLM 540B (chain-of-thought prompting): 57%
§ GSM8K는(cid:13379)Grade School Math 8K(cid:13379)의약자로, 초등학교수준의수학문제를포함하는데이터셋
Figure 2: PaLM 540B uses chain-
ofthought prompting to achieve new
stateof-the-art performance on the
GSM8K benchmark of math word
problems. Finetuned GPT-3 and prior
best are from Cobbe et al. (2021)
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in
large language models.Advances in neural information processing systems,35, 24824-24837.

---

## 페이지 50

Chapter 03. Part 04. 엔지니어링기법-Basic
o Chain(cid:13247)of(cid:13247)thought 은 모델의 파라미터가 클 때 효과적인 기법
ü 일반적인 스케일링 곡선보다 더 높은 성능을 보임.
Figure 7: Chain-of-thought prompting also improves the commonsense reasoning
abilities of language models. The language model shown here is PaLM. Prior best
numbers are from the leaderboards of CSQA (Talmor et al., 2019) and StrategyQA
(Gevaet al., 2021) (single-model only, as of May 5, 2022). Additional results using
various sizes of LaMDA, GPT-3, and PaLMare shown in Table 4.
Figure 4: Chain-of-thought prompting enables large language models to
solve challenging math problems. Notably, chain-of-thought reasoning is an
emergent ability of increasing model scale. Prior best numbers are from
Cobbe et al. (2021) for GSM8K, Jieet al. (2022) for SVAMP, and Lan et al. (2021)
for MAWPS.
(cid:13274)억
(cid:13205)위단
,수터미라파(cid:13273)기크델모
(cid:13205)축X•
(cid:13274)(cid:13984)(cid:13273)율비결해제문
(cid:13205)축Y•

---

## 페이지 51

Chapter 03. Part 04. 엔지니어링기법-Basic
CoT의 한계점
o 모델의 파라미터 수가 적은 모델에서는 기법의 성능이 떨어짐
o (cid:13361)CoT only yields performance gains when used with models of
(cid:13973)100B parameters(cid:13362)
o 사람이 직접 사고의 과정을 문장으로 작성해야 하는 번거로움
o 프롬프트의 완성도가 높지 않으면 결과가 좋지 않음

---

## 페이지 52

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
이 그룹의 홀수들을 더하면 짝수가 됩니다: 4, 8, 9, 15, 12, 2, 1.
답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 10, 19, 4, 8, 12, 24.
답: 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 16, 11, 14, 4, 8, 13, 24.
답: 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 9, 10, 12, 13, 4, 2.
답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 15, 32, 5, 13, 82, 7, 1.
답:
Model Output: 정답입니다. (X)

---

## 페이지 53

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
이 그룹의 홀수의 합이 짝수가 된다: 4, 8, 9, 15, 12, 2, 1.
A: 모든 홀수(cid:13273)9, 15, 1(cid:13274)를 더하면 25입니다.
정답은 (cid:13379)거짓(cid:13379)입니다.
이 그룹의 홀수의 합이 짝수가 된다: 17, 10, 19, 4, 8, 12, 24.
A: 모든 홀수(cid:13273)17, 19(cid:13274)를 더하면 36입니다.
정답은 (cid:13379)참(cid:13379)입니다.
이 그룹의 홀수의 합이 짝수가 된다: 16, 11, 14, 4, 8, 13, 24.
A: 모든 홀수(cid:13273)11, 13(cid:13274)를 더하면 24입니다.
정답은 (cid:13379)참(cid:13379)입니다.
이 그룹의 홀수의 합이 짝수가 된다: 17, 9, 10, 12, 13, 4, 2.
A: 모든 홀수(cid:13273)17, 9, 13(cid:13274)를 더하면 39입니다.
정답은 (cid:13379)거짓(cid:13379)입니다.
이 그룹의 홀수의 합이 짝수가 된다: 15, 32, 5, 13, 82, 7, 1.
A:
Model Output: A: 모든 홀수(cid:13273)15, 5, 13, 7, 1(cid:13274)를 더하면 41입니다. 홀수입니다. 따라서 정답은 (cid:13379)거짓(cid:13379)입니다.

---

## 페이지 54

Chapter 03.
The Basic Prompt Engineering Techniques
04. Zero(cid:13247)Shot
Chain of Thought

---

## 페이지 55

Chapter 03. Part 04. 엔지니어링기법-Basic
Zero Shot-Chain of Thought
Large Language Models are Zero-Shot Reasoners (2022)
- (cid:13361)단계적으로 생각해봐(cid:13362) (cid:13273)(cid:13362)Let(cid:13364)s Think Step by Step(cid:13362)(cid:13274)
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are zero-shot reasoners.Advances in neural information processing systems,35, 22199-22213.

---

## 페이지 56

Chapter 03. Part 04. 엔지니어링기법-Basic
Zero Shot-Chain of Thought
Large Language Models are Zero-Shot Reasoners (2022)
- (cid:13361)단계적으로 생각해봐(cid:13362) (cid:13273)(cid:13362)Let(cid:13364)s Think Step by Step(cid:13362)(cid:13274)
o Zero(cid:13247)shot과 Zero(cid:13247)shot(cid:13247)CoT의 성능 비교 o Benchmark, comparing Zero(cid:13247)shot, Few(cid:13247)shot, and
their CoT counterparts
X축: 모델 크기 (cid:13273)파라미터 수, 단위: 억(cid:13274)
Y축: 문제 해결 비율 (cid:13273)(cid:13984)(cid:13274)
• GSM8K, 또는Grade School Math 8K,는고품질의초등학교수준수학단어문제로구성된데이터셋
• GSM8K는총8,500개의문제를포함하고있으며, 이중7,500개는훈련용, 1,000개는테스트용으로나뉨
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are zero-shot reasoners.Advances in neural information processing systems,35, 22199-22213.

---

## 페이지 57

Chapter 03. Part 04. 엔지니어링기법-Basic
Zero Shot-Chain of Thought
- “단계적으로 생각해봐 (”Let’s Think Step by Step”)
o More trigger examples

---

## 페이지 58

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
o Zero(cid:13247)Shot Chain of Thought 을 사용해서 이 문제의 정답을 맞춰보세요.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 4, 8, 9, 15, 12, 2, 1.
답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 10, 19, 4, 8, 12, 24.
답: 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 16, 11, 14, 4, 8, 13, 24.
답: 참입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 9, 10, 12, 13, 4, 2.
답: 거짓입니다.
이 그룹의 홀수들을 더하면 짝수가 됩니다: 15, 32, 5, 13, 82, 7, 1.
답:
Model Output:

---

## 페이지 59 (OCR)

Chapter 03. Part 04. 엔지니어링 기법- Basic 
실습 
Chat Presets Save ↑ <ノ> 
gpt-3.5-turbo こ ◇ Compare Temperature 0.1 
SYSTEM 
Enter system instructions 
Maximum Tokens 400 
USER 
Stop sequences 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 4, 8, 9, 15, 12, 2, 1. Enter sequence and press Tab 
답: 거짓입니다. 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 10, 19, 4, 8, 12, 24. 
답: 참입니다. 
Top P 1 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 16, 11, 14, 4, 8, 13, 24. 
답: 참입니다. 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 17, 9, 10, 12, 13, 4, 2. Frequency penalty 0 
답: 거짓입니다. 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 15, 32, 5, 13, 82, 7, 1. 
Presence penalty 0 
답: 
== Let's think step by step. 
① API and Playground requests will 
-- Answer in Korean 
not be used to train our models. 
Learn more 
ASSISTANT 
이 그룹의 홀수들을 더하면 짝수가 됩니다: 15, 32, 5, 13, 82, 7, 1. 
답: 거짓입니다. 
Fast campus

---

## 페이지 60 (OCR)

Chapter 03. 
The Basic Prompt Engineering Techniques 
05. Self-Consistency 
Fast campus

---

## 페이지 61

Chapter 03. Part 04. 엔지니어링기법-Basic
Self-Consistency
Simple Idea: 가장 많은 답이 정답일 확률이 높다
수학 문제(cid:13205) 10(cid:13992)2(cid:13258)1
학생 A(cid:13996) 11
학생 B (cid:13996)11
학생 C(cid:13996)12
학생 D(cid:13996) 11
학생 E(cid:13996)11
최종 답 (cid:13205) 11

---

## 페이지 62

Chapter 03. Part 04. 엔지니어링기법-Basic
Self-Consistency
o Chain-of-thought prompting 을 개선한 기법
o 다양한 추론 경로를 만들어 그 중에서 가장 일관된 답변을 선택하는 방식
o 복잡한 산술 문제나 논리 문제에 효과적
1. Chain(cid:13247)of(cid:13247)thought: 문제 제시
2. Sample(cid:13247)a diverse set of reasoning
paths: 다양한 추론 경로 샘플링
3. Marginalize out reasoning paths to
aggregate final answers : 최종답 선택

---

## 페이지 63

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
Self-Consistency Improves Chain-of-Thought Reasoning in Language Models (2022)
세 단계에 걸쳐 진행 o 문제에 대한 여러 추론 경로를 고려하면서, 단일 추론이 갖고 있는 오류가능성을 줄임
o 수학 문제와 같이 정확성을 요구하는 일에서 모델 답변의 정확성을 높일 수 있음
(cid:13968)1단계(cid:13967) CoT 프롬프트 엔지니어링으로 시작한다. 언어
모델에게 문제를 해결하는 과정을 단계별로 설명하도록
하고 있다.
(cid:13273)예시(cid:13274) 주차장에 3대의 차가 있고 2대가 더 들어오면 총 몇
대의 차가 있는지 계산하는 문제가 있다. 모델은 있던 차
3대에 더해진 2대를 더해서 5대가 있다고 답한다. 그리고
새로운 산술 문제를 풀이하라고 모델에게 요구한다.
새로운문제: 재닛의 오리들은 하루에 알을 16개 낳는다.
재닛은 매일 아침 3개의 알을 먹고, 매일 4개의 알을
머핀을 굽는데 사용한다. 나머지 알은 하나에 2달러씩
판매한다. 재닛은 매일 얼마를 벌까?
(cid:13968)2단계(cid:13967) 여러가지경로샘플링: 재닛의 오리들이 하루에
16개의 알을 낳는다를 가정으로, 새로운 문제에 대한 여러
계산 경로를 탐색한다. 매일 재밋이 얼마를 버는지를
맞추기 위한 계산이다.
(cid:13968)3단계(cid:13967) 모델이 일관된 답변을 도출하기 위해 2단계
샘플링을 통해 나온 결과를 종합하여 추론한다. 그리고
가장 많이 생성된 답변인 결과를 내놓는다. (cid:13900)18불이다.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., ... & Zhou, D. (2022). Self-consistency improves chain of thought reasoning in language models.arXivpreprint arXiv:2203.11171.

---

## 페이지 64

Chapter 03. Part 04. 엔지니어링기법-Basic
Self-Consistency 성능
o 수학 문제 정답을 맞춘 확률이 높음
o 다수결 투표 방식의 정확도가 높음
o Greedy decode: 단일 경로를 따라 답을 생성
Method: 사용된모델과기법
o Weighted avg (cid:13273)unnormalized(cid:13274): 가중 평균을 사용하여 답을 도출
o CoT(cid:13247)prompting: Chain(cid:13247)of(cid:13247)Thought 프롬프팅을 사용한 성능
o Weighted sum (cid:13273)normalized(cid:13274): 정규화된 가중 합을 사용하여 답을 도출U
o Self(cid:13247)consistency: Self(cid:13247)Consistency 기법을 사용한 성능
o weighted sum (cid:13273)majority vote(cid:13274): 다수결 투표 방식

---

## 페이지 65

Chapter 03. Part 04. 엔지니어링기법-Basic
Research Paper
ü 복잡한 추론 작업에서 비용 효율적
ü 다양한 추론 경로를 통한 높은 정확도
Figure 2: Self-consistency (blue) significantly improves accuracy over CoT-prompting with greedy decoding (orange) across arithmetic and
commonsense reasoning tasks, over LaMDA-137B. Sampling a higher number of diverse reasoning paths consistently improves reasoning accuracy.
§ Self(cid:13247)Consistency의 한계점
o 복잡한 추론 작업을 해결 할 때 비용이 많이 듦
o 복잡한 추론을 해결하려면, 상당한 양의 훈련 데이터 필요. 모델이 일관된 응답을 효과적으로 생성하기 위해
다양한 추론 패턴을 학습해야 하기 때문
o 프롬프트가 명확하지 않거나 간결하지 않을 때, Self(cid:13247)Consistency의 기법 성능이 저하됨

---

## 페이지 66

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
아래 텍스트는 소프트회사의 보안관련 이메일입니다.
이메일 내용 중에서 비즈니스에 중요한 영향을 미치는 내용과 아닌 내용을
Self(cid:13247)Consistency Prompting 기법을 사용하여 구분해보세요.
이메일 내용
안녕하세요,
귀사의 시스템에서 중요한 보안 취약점을 발견하게 되어 이와 관련된 사항을 공유하고자 합니다.
이 취약점은 악용이 쉽지 않지만, 이를 통해 모든 사용자 데이터에 접근할 수 있는 가능성이
있습니다. 이에 대한 증거로 개념 증명 파일을 첨부했으니 확인해 주시기 바랍니다.
이 문제는 매우 심각하며, 조속한 시일 내에 해결해 주실 것을 요청드립니다.
해당 취약점을 통해 발생할 수 있는 잠재적 위협을 방지하기 위해, 귀사의 보안 팀에서 신속하게
대응해 주시기를 바랍니다. 추가적인 정보가 필요하거나, 제가 더 도울 수 있는 부분이 있다면
언제든지 연락해 주시기 바랍니다.빠른 시일 내에 문제 해결을 부탁드리며, 이러한 문제를 미리
발견하게 되어 다행이라고 생각합니다.
귀사의 보안 강화를 위해 함께 협력할 수 있기를 기대합니다.
감사합니다.

---

## 페이지 67

Chapter 03. Part 04. 엔지니어링기법-Basic
실습
Generated by gpt(cid:13247)3.5(cid:13247)turbo
Temp: 0.3

---

## 페이지 68 (OCR)

Chapter 03. Part 04. 엔지니어링 기법- Basic 
1번 ASSISTANT 
{Important} : { 보안 취약점 발견, 모든 사용자 데이터에 접근 가능성, 증거 첨부, 심각성 강조, 조속한 대응 요청, 보안 팀 대 
응 요청, 잠재적 위협 방지, 협력 요청} 
{Not Important} : { 인사말, 도움 제안, 다행이라는 감사 표현 } 
2번 ASSISTANT 
{Important} : { 보안 취약점 발견, 모든 사용자 데이터에 접근 가능성, 증거 첨부, 문제 심각성 강조, 조속한 대응 요청, 보안 
팀 대응 요청, 잠재적 위협 방지, 보안 강화 협력 요청} 
{Not Important} : { 이메일의 시작 및 인사말, 추가적인 정보 및 도움 제안, 다행이라는 감사 표현} 
3번 ASSISTANT 
{Important} : { 보안 취약점 발견, 모든 사용자 데이터에 접근 가능성, 증거 첨부, 심각한 문제, 조속한 대응 요청, 잠재적 위 
협 방지, 보안 팀 대응 요청, 문제 해결 요청, 보안 강화 협력 요청 } 
{Not Important} : { 개념 증명 파일 첨부, 추가 정보 및 도움 제공 가능 여부, 미리 발견해서 다행이라는 감사 인사} 
Fast campus

---

## 페이지 69

Chapter 03. Part 04. 엔지니어링기법-Basic
학습 목표
ü01
프롬프트 엔지니어링 기초 기법을 이해한다.
02
연구 논문을 통해 각 프롬프트 엔지니어링 기법의 핵심과 한계를 이해한다.
03
실습을 통해 각 프롬프트 엔지니어링 방법을 학습한다.

---

## 페이지 70

Chapter 03. Part 04. 엔지니어링기법-Basic
References
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... & Amodei, D. (2020). Language
models are few-shot learners. Advances in Neural Information Processing Systems, 33, 1877-1 901.
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from
human preferences. Advances in Neural Information Processing Systems, 30.
Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., ... & Amodei, D. (2020). Language
models are few-shot learners. arXiv preprint arXiv:2005.14165.
Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., ... & Zhou, D. (2022). Self-consistency improves chain
of thought reasoning in language models. arXiv preprint arXiv:2203.11171.
Work, W. M. I. C. L. Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting
elicits reasoning in large language models. Advances in Neural Information Processing Systems, 35,
24824-24837.

---
