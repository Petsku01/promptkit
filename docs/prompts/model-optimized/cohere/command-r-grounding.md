---
category: "model-optimized"
title: "Command R: Grounded Generation"
subcategory: "cohere"
model: "command-r"
---
[← Back to Model-Optimized Cohere](../index.md)

# Command R: Grounded Generation

## Grounded Answer

```
Answer using ONLY the provided context. Cite sources.

Context:
[paste context]

Question: [question]

Rules:
- Use only information from context
- Cite with [Source: ...]
- If not in context, say "Not found in provided sources"

Answer:
```

## Quote with Citation

```
Find relevant quotes for: [topic]

Sources:
[paste sources]

Format:
"[exact quote]" - Source: [source name]
```

## Fact + Source

```
For each claim, provide the source:

Topic: [topic]
Sources: [paste sources]

Claims:
1. [claim] - Source: [which source]
2. ...
```

## Cross-reference

```
Cross-reference these sources on [topic]:

Source A: [content]
Source B: [content]

Agreements:
Disagreements:
Unique to A:
Unique to B:
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
