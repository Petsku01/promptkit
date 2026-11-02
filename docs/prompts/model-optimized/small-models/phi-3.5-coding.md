---
category: "model-optimized"
title: "Phi 3.5: Coding"
subcategory: "small-models"
model: "phi-3.5"
---
[← Back to Model-Optimized Small-Models](../index.md)

# Phi 3.5: Coding

## Simple Function

```
Write [language] function:
Input: [type]
Output: [type]
Task: [description]

Code:
```

## Explain Code

```
Explain:
[code]

Answer:
```

## Fix Bug

```
Fix:
Error: [error]
Code: [code]

Fixed:
```

## One-liner

```
[language] one-liner for [task]:
```

## Regex

```
Regex pattern for [description]:
```

## Convert

```
Convert [format A] to [format B]:
[input]
Output:
```

##  Rajoitukset

- Max ~30 lines of code
- Simple functions
- One task at a time
- Provide input/output example if unclear

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
