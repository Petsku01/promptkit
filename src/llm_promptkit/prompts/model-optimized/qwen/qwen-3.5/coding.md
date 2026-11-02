---
category: "model-optimized"
title: "Qwen 3.5: Coding (simplified)"
subcategory: "qwen"
model: "qwen-3.5"
---
# Qwen 3.5: Coding (simplified)

## Koodin selitys

```
What does this code do?

[short code snippet]

Answer:
```

## Pieni funktio

```
Write function:
- Input: [type]
- Output: [type]
- Task: [simple task]

Code:
```

## Virheen korjaus

```
Fix error:

Error: [error]
Code: [code]

Fixed:
```

## Muunnos

```
Convert:
From: [format A]
To: [format B]

Input: [data]
Output:
```

## Regex

```
Regex for: [pattern description]

Pattern:
```

## One-liner

```
Python one-liner for: [task]

Code:
```

##  Rajoitukset

Pienille malleille (< 8B):
- Max 20 lines of code kerralla
- Simple functions
- Ei monimutkaista logiikkaa
- Provide example input/output

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
