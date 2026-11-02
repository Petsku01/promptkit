---
category: "model-optimized"
title: "DeepSeek V3: JSON Output"
subcategory: "deepseek"
model: "deepseek-v3"
---
[← Back to Model-Optimized Deepseek](../index.md)

# DeepSeek V3: JSON Output

## Basic Extraction

```
Extract as JSON:

{
  "field1": "string",
  "field2": number,
  "field3": ["array"]
}

Text: [input]

JSON:
```

## Entity Extraction

```
Extract entities:

{
  "people": ["names"],
  "organizations": ["orgs"],
  "locations": ["places"],
  "dates": ["YYYY-MM-DD"]
}

Text: [input]
```

## Sentiment + Analysis

```
Analyze and return JSON:

{
  "sentiment": "positive/negative/neutral",
  "confidence": 0.0-1.0,
  "key_topics": ["topic1", "topic2"],
  "summary": "brief summary"
}

Text: [input]
```

## Structured Data

```
Parse into JSON:

{
  "items": [
    {
      "name": "",
      "quantity": 0,
      "price": 0.0
    }
  ],
  "total": 0.0
}

Input: [invoice/receipt/list]
```

## Classification

```
Classify and format:

{
  "category": "chosen category",
  "subcategory": "if applicable",
  "confidence": "high/medium/low",
  "reasoning": "brief explanation"
}

Categories: [list categories]
Text: [input]
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
