# Part 9. 생성형 AI 프롬프트 - 프로젝트

> 파싱 일시: 2026-01-09 17:59:38
> 총 페이지: 17
> 텍스트 추출 성공: 14
> OCR 필요: 3

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering
Chapter 04. 프롬프트 엔지니어링 파이널 프로젝트

---

## 페이지 2

Prompt EngineeringA to Z
생성형 AI 프로젝트의 범위와 목표 설정
프롬프트 엔지니어링 A to Z
교육 분야: AI 기반 교과서 활동 툴 및 챗봇 개발 : 실습
Chapter 04. 프롬프트 엔지니어링
사용자 경험 분석: AI 상호작용 만족도 연구 : Turn Chunking
파이널 프로젝트
고객 서비스: AI 상담 지원 시스템 구축 : Topic Modeling

---

## 페이지 3 (OCR)

Chapter 04. 프롬프트 엔지니어링 파이널 프로젝트 
생성형 AI 프로젝트의 범위와 목표 설정 
교육 분야 : AI 기반 영어 화자를 위한 
교과서 활동 툴 및 챗봇 개발 한국어 학습용 툴/챗봇 
사용자 경험 분석 → 
사용자 만족도 
AI 상호작용 만족도 연구 
분류 
고객 서비스 AI 지원 
고객 불만 데이터 기반 
시스템 구축 Topic 모델링 
Fast campus

---

## 페이지 4

Chapter 04. 프롬프트엔지니어링파이널프로젝트
(cid:13967) 교육 분야: AI 기반 교과서 활동 툴 및 챗봇 개발
대상: 영어 모어 화자를 위한 한국어 학습용 툴/챗봇
●
대상 레벨: Novice Level
●
구현 방법: 100% 프롬프트 엔지니어링
●

---

## 페이지 5

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Prompt 프로젝트 실습 #1
Lesson 2. 어때요?
세 개의 형용사를 Novice 레벨 학습자의 수준에 맞춰,
＂어때요?” 문장을 학습하도록 하는 “툴”을 프롬프트로 제작해보세요.
형용사: 맛있다, 많다, 좋다
선생님: 학교 식당 커피가 _______?
학생: 맛있어요.
선생님: 한국어 수업이 ______?
학생: 좋아요.
선생님: 오늘 날씨가 ______?
학생: 좋아요.

---

## 페이지 6

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Prompt:
(cid:13361)(cid:13362)(cid:13362)You are an expert Korean language teacher. Your task is to generate
extremely simple questions based on the (cid:13275)(cid:13275)형용사(cid:13276)(cid:13276) inputted by the user.
Limit your response to less than 6 words. Respond in Korean.
Include the English translation at the end of your response.
(cid:13273)Example(cid:13274)
U(cid:13205) 맛있다.
A(cid:13205) 학교 식당 커피가 어때요? 맛있어요.
How is the school coffee? Delicious.
###
U(cid:13205) 많다.
A(cid:13205) 한국어 수업 숙제가 어때요? 재미있어요.
How is your Korean homework? Fun.
### U(cid:13205) 좋다. A(cid:13205) 요즘 기분이 어때요? 좋아요.
How are you feeling? Good.
###

---

## 페이지 7

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Prompt 프로젝트 실습 #
Lesson 2. Describing People” Practice Bot
아래 단어들을 조합하여 학습하는 챗봇을 만드세요.
문법이나 철자 오류가 있다면, 친절하게 알려줘야해요.
이름: 제니퍼
학년: 4학년
국적: 캐나다 사람
전공: 문학
관계: 친구
출신: 토론토
제니퍼는 4학년이에요. 캐나다 사람이에요. 문학을
전공해요. 제 친구는 토론토에서 왔어요.

---

## 페이지 8

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Prompt 프로젝트 실습 #
Lesson 2. Describing People” Prac:ce Bot

---

## 페이지 9

Chapter 04. 프롬프트엔지니어링파이널프로젝트
(cid:13967) 사용자 경험 만족도 : 데이터 Chunking
프롬프트 기능: Raw Data 를 Single Turn과 Multi-Turn으로 구분하기
●
목적: 분류된 턴을 평가 메트릭스에 넣고 LLM에 의한 자동 스코어링
●
구현 방법: Pythonic Prompting
●

---

## 페이지 10

Chapter 04. 프롬프트엔지니어링파이널프로젝트
실습:
Turn을 Single(cid:13247)Turn 과 Multi(cid:13247)Turn을 자르는 프롬프트를 제작하세요.
*실습을 위한 데이터를 사용하세요.

---

## 페이지 11

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Pythonic Promp-ng
We have found that using code prompts
instead of natural language prompts
for LLMs reduces ambiguity and
misinterpretation, which significantly
reduces LLM hallucination
during plan generation and refinement.
Source: https://proceedings.neurips.cc/paper_files/paper/2023/hash/b5c8c1c117618267944b2617add0a766-Abstract-Conference.html

---

## 페이지 12 (OCR)

Prompting with Pseudo-Code Instructions 
Chapter 04. 프롬프트 엔지니어링 파이널 프로젝트 
A.2.2 Prompting with Pseudo-code 
Listing 3 Code instructions (2-shot prompt) for 
instructions 
sentiment classification task 
def generate_sentiment (sentence: str) - > str: 
Listing 2 Code instructions (0-shot prompt) for 
"""For the given sentence, the task is to 
sentiment classification task predict the sentiment. For positive sentiment 
def generate_sentiment (sentence: str) str: return "positive" else return "negative" 
"""For the given sentence, the task is to 
Parameters: 
predict the sentiment. For positive sentiment 
return "positive" else return "negative" sentence (str) : input sentence 
Returns: 
str: sentiment of the input 
Parameters: 
··· 
sentence (str): input sentence 
Returns: 
# predict the sentiment 
str: sentiment of the input 
if sentiment_is_positive(sentence) : 
··· 
return "positive" 
else: 
# predict the sentiment 
return "negative" 
if sentiment_is_positive(sentence) : 
return "positive" >>> generate_sentiment( 
else: " tormented by the quickened blood of the " 
return "negative" "roots" 
) 
>>> generate_sentiment( negative" 
"that has a charmingly bourbon air ■ 
) >>> generate_sentiment( 
"radiant as moses from the mount, he stood" 
) 
"positive" 
>>> generate_sentiment( 
"that has a charmingly bourbon air " 
Source: https:/ / arxiv.org/pdf/2305.11790 
Fast campus

---

## 페이지 13

Chapter 04. 프롬프트엔지니어링파이널프로젝트
Pythonic Prompting Example
context (cid:13965) (cid:13379)(cid:13379)(cid:13379)You are tasked with recognizing dramatic context change between adjacent turns.
(cid:13247)(cid:13247)(cid:13247)
(cid:13277)Instructions(cid:13278)
Start by comparing turn 0 and turn 1. Continue this process until the end.
for each turn comparison,
if two turns share common context:
continue
if the user has a common shared intent between two turns:
continue
if the two turns share the same keyword:
continue
else:
list the number of the latter turn
Answer format should be list of numbers.
(cid:13247)(cid:13247)(cid:13247)
Now analyze the given dialog and provide your answer.(cid:13379)(cid:13379)(cid:13379)

---

## 페이지 14 (OCR)

Chapter 04. 프롬프트 엔지니어링 파이널 프로젝트 
Single Turn 
Multi Turn 
Turn-Chunking 
Multi Turn 
Single Turn 
Single Turn 
Fast campus

---

## 페이지 15

Chapter 04. 프롬프트엔지니어링파이널프로젝트
(cid:13967)
고객 불만 데이터 기반 Topic 모델링

---

## 페이지 16

Chapter 04. 프롬프트엔지니어링파이널프로젝트
(cid:13967) Sample Conversation Script
[00:00] Agent: 네~~XX 상담원 XXX 입니다.
[00:03] Customer: 네 저 지금 드릴집 듣고 있는데요 네 네 이거 혹시 환불하게 되면 얼마정도 받을 수
있는지 궁금해서요
[00:10] Agent: 아 네 회원님 성함 말씀해 주시겠습니까? 네 본인 맞으십니까? 네네 네 확인 감사합니다
회원님 혹시 수강이 불편함을 느끼셔서 환불 말씀하시는 걸까요?
[00:23] Customer: 네 그냥 시험을 좀 안보이게 될 거 같아서 네 그래서
[00:28] Agent: 아 그러세요 아니시면 다른 과정으로 저희가 워낙 많은 카테고리가 있어서 네네
다른 과정으로도 원래 사실 결제일로부터 이 주 이내에만 가능하신데
선생님께서 환불 원치 않으시고 다른 과정을 원하시면 변경도 저희가 해드리고 있거든요
[00:44] Customer: 아 근데 이게 그러면 시험대비 말고 혹시 뭐 네 평생 수강이나 이렇게도 좀 변경이 되나요?
[00:51] Agent: 네 저희가 맞물려도 평생교육 평생 영업패스나 이렇게 변경하신다 하더라도
((생략))

---

## 페이지 17

Chapter 04. 프롬프트엔지니어링파이널프로젝트
실습 : 아래 데이터를 기반으로 Topic(cid:13247)Modeling 프롬프트를 제작해보세요.
[00:00] Agent: 네~~XX 상담원 XXX 입니다.
[00:03] Customer: 네 저 지금 드릴집 듣고 있는데요 네 네 이거 혹시 환불하게 되면 얼마정도 받을 수
있는지 궁금해서요
[00:10] Agent: 아 네 회원님 성함 말씀해 주시겠습니까? 네 본인 맞으십니까? 네네 네 확인 감사합니다
회원님 혹시 수강이 불편함을 느끼셔서 환불 말씀하시는 걸까요?
[00:23] Customer: 네 그냥 시험을 좀 안보이게 될 거 같아서 네 그래서
[00:28] Agent: 아 그러세요 아니시면 다른 과정으로 저희가 워낙 많은 카테고리가 있어서 네네
다른 과정으로도 원래 사실 결제일로부터 이 주 이내에만 가능하신데
선생님께서 환불 원치 않으시고 다른 과정을 원하시면 변경도 저희가 해드리고 있거든요
[00:44] Customer: 아 근데 이게 그러면 시험대비 말고 혹시 뭐 네 평생 수강이나 이렇게도 좀 변경이
되나요?
[00:51] Agent: 네 저희가 맞물려도 평생교육 평생 영업패스나 이렇게 변경하신다 하더라도
((생략))

---
