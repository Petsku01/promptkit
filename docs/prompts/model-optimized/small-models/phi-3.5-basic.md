---
category: "model-optimized"
title: "Phi 3.5: Basic Tasks"
subcategory: "small-models"
model: "phi-3.5"
---
[← Back to Model-Optimized Small-Models](../index.md)

# Phi 3.5: Basic Tasks

## Classification

```
Classify: [categories]

Text: [input]
Category:
```

## Question Answering

```
Q: [question]
A:
```

## Summarization

```
Summarize in 2 sentences:
[text]
Summary:
```

## Math

```
Solve: [problem]
Answer:
```

## Step-by-Step

```
Think step by step:
[problem]

Step 1:
Step 2:
Answer:
```

## Fill-in

```
Complete: [text with blank]
Answer:
```

## Translation

```
Translate to [language]:
[text]
Translation:
```

## Extraction

```
Extract [entity type]:
[text]
Found:
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
