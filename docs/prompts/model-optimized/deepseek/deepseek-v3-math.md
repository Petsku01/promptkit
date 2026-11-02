---
category: "model-optimized"
title: "DeepSeek V3: Math"
subcategory: "deepseek"
model: "deepseek-v3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Deepseek](../index.md)

# DeepSeek V3: Math

## When to Use

Use this template when DeepSeek-V3 must solve or check a mathematics problem (algebra, calculus, word problems, discrete proof sketches, simple optimization) as an instruct model rather than as R1. The V3 card reports strong vendor numbers on GSM8K, MATH, AIME-style sets relative to other open instruct models; treat those as the reason the SKU exists, not as a guaranteed score for this prompt. Context is 128K. For contest problems that need long hidden CoT and boxed-only output, prefer [deepseek-r1/reasoning](../deepseek-r1/reasoning.md). For JSON numeric extraction, use [json-output](json-output.md).

The retired Finnish “Matematiikka” stub mixed seven mini-templates and no verification step. This file is English (catalog language of the living siblings) and one protocol.

## The Prompt

```
Solve the following problem. Show the algebra; do not jump to an answer.

Problem:
[problem statement]

Given:
[quantities, units, diagrams described in text]

Assumptions you may use:
[theorems or conventions, or "standard real numbers only"]

Required:
- Exact answer when possible (fractions, radicals, exact trig). Decimal
  approximations only if asked, with the rounding rule.
- If this is a word problem, define variables before equations.
- If this is a proof, use a numbered implication chain ending in QED or a
  clear counterexample.

Procedure:
1. Identify unknowns and the goal.
2. Write the governing equations or theorem names.
3. Solve, checking each line for algebraic reversibility.
4. Verify by substitution, derivative sign, dimensional analysis, or a
   numeric special case.
5. If verification fails, backtrack once. If it still fails, say so.

Final block:
Answer: [exact form]
Check: [the verification you actually did]
Caveat: [assumption that would change the answer, or "none"]
```

## How It Works

V3 is not required to emit `<think>` tags; asking for numbered steps plus an explicit check uses the distilled-reasoning behavior without R1 protocol. Exact-before-decimal stops sloppy rounding. The verify-or-backtrack rule is the stop condition the stub lacked. Units and “standard real numbers only” keep the model from mixing degrees/radians or silently moving to complexes. Nothing in this prompt is a calculator guarantee: if the runtime has no tool, the check is symbolic or a hand numeric special case, labeled as such.

## Variables

- `[problem statement]`: full text, including figure descriptions.
- `[quantities, units, diagrams described in text]`: given data.
- `[theorems or conventions, or "standard real numbers only"]`: legal tools.

## Related

[analysis](analysis.md), [coding](coding.md), [json-output](json-output.md). Heavier CoT: `deepseek-r1/reasoning.md`.

Grounded 2026-11-02 against [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) (math called out on the card; numbers not reproduced as ours).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
