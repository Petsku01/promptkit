---
category: "model-optimized"
title: "Qwen 3.5: JSON (simplified)"
subcategory: "qwen"
model: "qwen-3.5"
---
# Qwen 3.5: JSON (simplified)

## Perus JSON

```
Return JSON only:
{"key": "value"}

Input: [text]
JSON:
```

## Lista

```
Extract as JSON array:
["item1", "item2"]

Input: [text]
JSON:
```

## Avain-arvo

```
Parse to JSON:
{"name": "", "value": ""}

Input: [text]
JSON:
```

## Luokittelu JSON

```
Classify and return:
{"category": "", "confidence": "high/low"}

Text: [input]
JSON:
```

## Yksinkertainen schema

```
Extract:
{
  "title": "",
  "date": "",
  "author": ""
}

From: [text]
JSON:
```

##  Small mallit

- Max 3-5 fields
- Simple types (string, number)
- No deep nested structures
- Always provide example output
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
