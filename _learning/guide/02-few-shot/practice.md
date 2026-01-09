# 2단계 실습: Few-Shot 프롬프트 개선

> 목표: ner_validation_v1 → v2 개선

---

## 실습 1: 현재 프롬프트 분석

### v1 예시 현황

| 타입 | 유효 | 무효 |
|------|------|------|
| Biomarker | HER2 | er |
| Disease | 고혈압 | 주사 |
| Drug | ❌ 없음 | ❌ 없음 |
| Procedure | ❌ 없음 | ❌ 없음 |

### 문제점
1. Drug, Procedure 타입 예시 없음
2. 경계 케이스 부족

---

## 실습 2: v2 예시 설계

### 추가할 예시 (직접 작성해보기)

**Drug 유효**:
```
텍스트:
매칭: → Drug
판정: 유효
```

**Drug 무효**:
```
텍스트:
매칭: → Drug
판정: 무효
```

**Procedure 유효**:
```
텍스트:
매칭: → Procedure
판정: 유효
```

**Procedure 무효**:
```
텍스트:
매칭: → Procedure
판정: 무효
```

**경계 케이스**:
```
텍스트:
매칭: →
판정:
이유:
```

---

## 피드백

(Claude 코멘트 예정)

---

## 개선된 v2 프롬프트

(완성 후 experiments/prompts/ner_validation_v2.yaml에 저장)
