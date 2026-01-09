# Part 8. 프롬프트 기록과 버전 관리

> 파싱 일시: 2026-01-09 17:59:34
> 총 페이지: 16
> 텍스트 추출 성공: 9
> OCR 필요: 7

---

## 페이지 1

국내 공채1호 프롬프트 엔지니어 강수진의
프롬프트 엔지니어링 A to Z
Prompt Engineering
Chapter 03.
Part 08. 프롬프트 기록과 버전 관리

---

## 페이지 2

Prompt EngineeringA to Z
프롬프트 기록의 필요성과 이점
프롬프트 엔지니어링 A to Z
프롬프트 버전 관리: 원칙과 모범 사례
Chapter 03
Part 08. 프롬프트 기록과 버전 관리
프롬프트 기록 실습

---

## 페이지 3

Chapter 03.프롬프트기록과버전관리
• 프롬프트 기록과 관리의 어려움
- 프롬프트수정내역을체계적으로관리하기가어렵다
- 협업이어렵다
- 프롬프트버전관리도구가제한적이다
Git Google Spreadsheet
VS Code Dropbox
Notion Other Tool

---

## 페이지 4 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Anthropic : Prompt Library 
ANTHROP\C English ✓ Q Search... �� Research News Go to claude.ai > ※ 
Welcome User Guides API Reference Prompt Library Release Notes Developer Newsletter 
Prompt Library 
Explore optimized prompts for a breadth of business and personal tasks. 
Q Search... All prompts 
Cosmic keystrokes Corporate clairvoyant 
吉 
Generate an interactive speed typing game in a Extract insights, identify risks, and distill key 
single HTML file, featuring side-scrolling gameplay information from long corporate reports into a 
and Tailwind CSS styling single memo 
Website wizard Excel formula expert 
Create one-page websites based on user Create Excel formulas based on user-described 
specifications calculations or data manipulations 
Google apps scripter Python bug buster 
G Generate Google Apps scripts to complete tasks Detect and fix bugs in Python code 
based on user requirements 
Time travel consultant Storytelling sidekick 
O 
Help the user navigate hypothetical time travel Collaboratively create engaging stories with the 
scenarios and their implications user, offering plot twists and character 
development 
Cite your sources SQL sorcerer 
a 
Get answers to questions about a document's Transform everyday language into SQL queries 
content with relevant citations supporting the 
response 
Dream interpreter Pun-dit 
Offer interpretations and insights into the Generate clever puns and wordplay based on any 
symbolism of the user's dreams given topic 
Fast campus

---

## 페이지 5 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Claude for Sheets: Prompt Examples 
Copy of Claude for SheetsTM: Prompt Examples [PUBLIC ACCESS] 
田 
File Edit View Insert Format Data Tools Extensions Help 
a Menus け さ T 100% ▼ $ % .0 .00 123 Arial - 10 + B I 응 A る。 三 ▼ 点 ▼ |→ ▼ A GD Y 囲 � 
둔 곧 
A1 ▼ I fx 
A B C 
1 This sheet shows Claude's responses to some basic questions 
2 
3 Some rows have been condensed for legibility. To see full responses, copy the response cell into a text editor or expand the row height. 
4 Step 1: Type your prompts in this column Step 2: Select your model Step 3: CLAUDE response 
In one sentence, what is good about the color blue? claude-3-haiku-20240307 ▼ #NAME? 
5 
Suppose you have a table called "Customers" with the following claude-3-haiku-20240307 #NAME? 
column names: 
CustomerlD, CustomerName, ContactName, Address, City, 
PostalCode, Country 
6 Can you write a SQL query that finds all customers in San Francisco 
with a customer ID of greater than 1000? 
Write a python function to determine if a number is prime claude-3-haiku-20240307 #NAME? 
Fast campus

---

## 페이지 6 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Prompt Layer 
PromptLayer Platform V Docs Blog Case Studies Contact Us Log In 
The cleanest way to PromptLayer く G P PromptLa... Home Registry Evaluate 
Search... ◇ Tags 
prompt engineer み Fine-Tune Datasets 
/ Registry / Prompts / sql-buddy / promptlayer-sql 
text-to-sql No Tags 
gpt-3.5-turbo Last Updated: 2 days ago · ID: 17163 · Version 12 of 12 · jinja2 
Edit, evaluate, deploy & repeat. Manage and Prompt: You are a friendly AI personal stylist. Your 
client is not very stylish or wise, and he needs... 
monitor prompts with your whole team, Response: Today' S precipitation probability is 0, Template Versions Hide 
so it's safe to wear suede without worrying abou... 
including non-technical stakeholders. ● Version 12 67 
SYSTEM 
□ daily_ weather 3:25:02 AM 
6 months ago You are a data analyst who is a 
gpt-3.5-turbo D use preamble snippet 
There are A LOT of logs in the 4 
Start for free Prompt: You are a friendly AI personal stylist. Your 
x 50% passing 
keep queries small & fast. 
client is not very stylish or wise, and he needs... 
Response: Today will be warm and partly cloudy, ○ Version 11 20 
reaching around 88°F. Sunset at 7:13 PM Enj... This is the schema for your cor 
6 months ago 
database. 
□ daily_weather 3:25:00 AM ○ add back few-shot, 
increase temp 
An embedding is a request log 
gpt-3.5-turbo x 58% passing 
function_name has "Embedding 
Prompt: You are a friendly AI personal stylist. Your prod 
sqlalchemy. 
client is not very stylish or wise, and he needs... 
Response: Today S precipitation probability is very ○ Version 10 12 
low, only 1%, It seems safe to wear suede today,... 
6 months ago 
□ daily_ weather a day ago ○ remove few-shot Input Variables: question 
example 
gpt-3.5-turbo x 8% passing 
Prompt: You are a friendly AI personal stylist. Your 
client is not very stylish or wise, and he needs... Average Latency Average Score 
4 
Response: Today will be warm with scattered 3.54s 67 
clouds, reaching a high of 87.8°F, Sunset at... 
□ dally... weather a day ago 
Trusted hu companies like UOI I 
Fast campus

---

## 페이지 7 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Sample 
PromptLayer く G P Personal Home Registry Evaluate Analytics ◎ Playground 
JTL Fine-Tune Datasets 
/ Registry / Prompts / Example: page_ title 
Search... ○ Tags 
Example: page_title No Tags 
Requests Traces Last Updated: 4 months ago · ID: 23378 · Version 6 of 6 · f-string Delete Ⓓ Playground 0 Edit 
No requests found 
Template Versions Hide 
USER 
● Version 6 SYSTEM 
Ⓡ Click here to turn off the d 
efault date range limit 4 months ago # Topic 
You are a helpful AI assistant. You work for an online media 
O No quotes, higher temp Travel 
organization called BuzzFeed. 
staging 
# Summary 
Your task is to create catchy article titles based on a summary. The 
Wanderlust calling? Check out our curated list of 10 awe-inspiring 
○ Version 5 titles should be no more than 10 words. The titles should have no 
travel destinations that should be on every adventurer's bucket list. 
4 months ago emojis. 
From tropical paradises to historic cities, these places offer 
○ Remove last line 
unforgettable experiences. Get ready to fuel your wanderlust and start 
production The goal is to write catchy & easy to write blog post titles. These 
planning your next getaway! 
titles should be "clickbait" and encourage users to click on the 
○ Version 4 blog. 
Copy 
4 months ago 
○ More !!! The user will provide a blog post abstract summary as well as a 
topic keyword. You will respond with a title. Don't use quotes in the ASSISTANT 
title. 
○ Version 3 The Ultimate Travel Bucket List: 10 Breathtaking Destinations to Visit 
4 months ago 
Copy 
○ Catchier title 
Copy 
○ Version 2 
4 months ago Variables: article topic Metadata = Parameters 
Input 
曰 No emojis 
Version 1 
Average Latency Average Score Total Cost Total Requests 
◆ ■ II  
Model Name ◇ Input Variables ◇ Request Start Time � Score ◇ Response Preview ◇ 
Fast campus

---

## 페이지 8 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
LangSmith 
& Personal > ④ Prompts > general > c1b8dde7 
18 
general:c1b8dde7 상 Private Make Public 
品 
Prompt Commits Updated 3 months ago 
/ 
@ ChatPromptTemplate Edit in Playground → 
SYSTEM 
You are a chatbot. Help me to provide an accurate information on the given topic. 
HUMAN 
{question} 
C 
ChatOpenAl 
Provider OpenAl Chat Instruct C 
Model gpt-4o-mini 
Temperature 0.4 
Max Output Tokens 1005 
Top P 1 
Presence Penalty 0 
Frequency Penalty 
: 
Fast campus

---

## 페이지 9 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Hub DEVELOPER 
 父 
New Use Cases V 
+ > 
Prompt 
品 Agent simulations 53 
/_ LangChain Hub Agents 507 
Autonomous agents 93 
Explore and contribute prompts to the community hub 
Chatbots 304 
Classification 75 
Search prompts, use cases, models... 
Code understandi... 63 
Code writing 88 
Evaluation 106 
Top Favorited Top Viewed Top Downloaded Recently Updated 
Extraction 171 
Interacting with A... 93 
Multi-modal 20 
ChatPromptTemplate Summarization English openai:gpt-3.5-turbo 
QA over docume... 326 
hardkothari/prompt-maker 
Self-checking 52 
Convert your small and lazy prompt into a detailed and better prompts with this template. 
SQL 25 
{x} Prompt · Updated a year ago · 182 59.2k · 出 19.9k · � 1 
Summarization 250 
Tagging 30 
ChatPromptTemplate QA over documents English <> Type V 
rlm/rag-prompt ChatPromptTe... 3796 
This is a prompt for retrieval-augmented-generation. It is useful for chat, QA, or other applications that StringPromptTe... 1265 
rely on passing context to an LLM. 
StructuredPrompt 188 
(x) Prompt · Updated 4 months ago · 155 · 210k · 出 16.7M · � 3 
Language V 
Chinese 94 
Agents Interacting with APIs ChatPromptTemplate meta:ilama-2-70b-chat 
English 1058 
homanp/superagent French 39 
This prompt ads sequential function calling to models other than GPT-0613 German 31 
: 
{x} Prompt · Updated a year ago · 149 · 73k · 业 36.3k · -○- 11 Russian 18 
Spanish 52 
Fast campus

---

## 페이지 10

Chapter 03.프롬프트기록과버전관리
• 프롬프트 버전 관리: 원칙과 모범 사례: Notion
프롬프트 데이터베이스의 칼럼 설정
Property Type Description
Name Tittle 프롬프트 이름
Status Select 상태 (cid:13273)Draft, In Progress, In Review,
Done(cid:13274)
Version Number 버전 번호
Author Person 작성자
Created at Created Time 생성 날짜
Updated at Last Edited Time 마지막 수정 날짜
Project Multi(cid:13247)Select 관련 프로젝트
Change Log Relation Change Log 데이터베이스와의 관계 설정

---

## 페이지 11

Chapter 03.프롬프트기록과버전관리
• 프롬프트 수정 로그
Property Type Description
Name Tittle 변경 로그 이름
Prompt Relation Prompts 데이터베이스와의 관계 설정
Version Number 버전 번호
Change Summary Text 변경 내용 요약
Change By Person 생성 날짜
Changed at Created Time 변경 날짜

---

## 페이지 12 (OCR)

Chapter 03. 프롬프트 기록과 버전 관리 
Example 
Prompt Fortpolio 
Aa 프롬프트 제목 Status Version Created At Upda1 
sample_prompt In progress V1.0 2024년 8월 16일 오후 11:07 2024년 1 
Prompt Template Not started 2024년 8월 16일 오후 11:48 2024년 1 
+ 새로 만들기 
Fast campus

---

## 페이지 13

Chapter 03.프롬프트기록과버전관리
프롬프트 버전 관리 규칙
● 규칙 1: 주요 기능 변경 시
- 초기 버전은 1.0.
- 1.0에서 프롬프트의 기능이나 목적에 변화가 발생할 경우 주요 버전에 앞 번호를 올린다. (예:
1.0, 2.0, 3.0)
(예시) 새로운 기능 원본에 추가, 프롬프트 메인 구조 변경, 프롬프트 토큰 수 변경
● 규칙 2: 마이너 업데이트 시
- 프롬프트 내용의 일부 수정, 성능 개선, 오류 수정 등 사소한 변경이 있을 때는 뒷 번호를 올린다.
(예: 1.1, 2.1, 3.2)
(예시) 문법 오류 수정, 일부 문장 수정, 기존 기능에서 일부 기능 추가

---

## 페이지 14

Chapter 03.프롬프트기록과버전관리
프롬프트 버전 관리 규칙
● 규칙 3: 버그 수정 시
프롬프트의 버그를 수정하거나 긴급한 문제를 해결한 경우 패치 버전 번호를 올린다. (예: 1.0.1,
1.0.2)
(예시) 오타 수정, 출력 깨짐 수정
● 규칙 4: 피드백 반영 시
사용자나 팀의 피드백을 반영하여 프롬프트를 업데이트할 때는 마이너 버전
또는 패치 버전 번호를 올린다.
(예시)
- 사용자 피드백을 반영한 작은 내용 수정, 기능 개선 등
-아랍어가 결과물에 나오지 않게 하기
- 사칙연산 기호 -, +, /, *가 나오는 이슈 수정

---

## 페이지 15

Chapter 03.프롬프트기록과버전관리
프롬프트 버전 관리 규칙
규칙 5: 주기적 검토 및 업데이트 시
- 정기적으로 프롬프트를 검토하고 최신 상태로 업데이트할 때는 적절한 번호
(주요, 마이너, 패치)를 올린다.
- 판단은 기능의 크기로 결정한다.
(예시) 시스템 프롬프트 개선 작업은 주요 기능을 업데이트하는 것이므로 버전의
앞 번호를 증가시킨다. (예: 1.0 2.0)

---

## 페이지 16

Chapter 03.프롬프트기록과버전관리
Practice : 프롬프트 템플릿에 프롬프트를 기록해보세요.
이때 앞에서 다룬 버전 관리와 규칙을 적용하세요.

---
