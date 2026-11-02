---
category: "model-optimized"
title: "Qwen 2.5: Multilingual"
subcategory: "qwen"
model: "qwen-2.5"
---
# Qwen 2.5: Multilingual

## Translation (Any Direction)

```
Translate:

From: [source language]
To: [target language]

Text:
[input]

Translation:
```

## Chinese <-> English

```
Translate to English:

[Chinese text]

---

Translate to Chinese:

[English text]
```

## Language Detection

```
Detect language:

Text: [input]

Language:
Confidence:
```

## Multilingual Summary

```
Summarize in [target language]:

Original language: [source]
Document:
[paste document]

Summary in [target language]:
```

## Cross-lingual QA

```
Answer in [language]:

Context (may be in different language):
[context]

Question: [question in any language]

Answer in [specified language]:
```

## Code Comments Translation

```
Translate code comments:

From: [language]
To: [language]

Keep code unchanged, translate only comments.

[paste code with comments]
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
