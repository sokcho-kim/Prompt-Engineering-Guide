# 비용 추적

## 구조

```
cost/
├── daily/              # 일별 비용 로그
│   └── 2026-01-09.json
├── pricing.yaml        # 모델별 가격 설정
└── aggregate.py        # 비용 집계 스크립트
```

## 사용법

```bash
# runs/ 폴더에서 비용 자동 집계
python aggregate.py

# 특정 날짜 집계
python aggregate.py --date 2026-01-09

# 월간 리포트
python aggregate.py --month 2026-01
```

## 일별 로그 형식

```json
{
  "date": "2026-01-09",
  "runs": [
    {
      "prompt": "ner_validation_v2",
      "items": 22,
      "tokens": {"prompt": 15158, "completion": 44, "total": 15202},
      "cost_usd": 0.002301
    }
  ],
  "total_cost_usd": 0.004602
}
```
