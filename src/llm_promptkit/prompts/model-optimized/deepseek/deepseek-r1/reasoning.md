---
category: "model-optimized"
title: "DeepSeek-R1: Zero-Shot Reasoning"
subcategory: "deepseek"
model: "deepseek-r1"
source: "promptkit-authored"
---
# DeepSeek-R1: Zero-Shot Reasoning

## When to Use

Use this template for open-weight DeepSeek-R1 (and R1 distillations) on math, logic, or multi-step scientific questions where the model should reason in `<think>` and then give a short answer. The official card tells operators to avoid system prompts, keep temperature around 0.6, put every instruction in the user turn, and for mathematics include “reason step by step” plus a `\\boxed{}` final. It also warns that some queries skip thinking (`<think>\n\n</think>`); forcing a `<think>\n` prefix is the documented mitigation.

This is not the hosted V4 thinking-mode guide (`reasoning_content`, tool-call replay). Hosted `deepseek-flash` / `deepseek-v4-pro` should use those API fields instead of R1 think-tags. Do not use a chatty system persona, do not ask the model to hide its reasoning if the runtime still emits it, and do not quote the card’s AIME/MATH tables as promptkit measurements.

## The Prompt

System message: **empty**. User message:

```
Problem:
[statement]

Given:
[data, units, definitions that are in evidence]

Find:
[the exact quantity, decision, or proof obligation]

Instructions:
Reason step by step inside your thinking section. Check units, bounds, and
edge cases before you settle. If two interpretations of the wording are
possible, pick the one consistent with the Given block and say so.

After thinking, output only:
- A one-line restatement of what is being asked.
- The worked solution, compact but complete (no omitted algebra on the
  critical step).
- Final answer in \boxed{...} for math, or a single labeled Answer: line
  for non-math.
- A one-line confidence note: which assumption, if wrong, flips the result.

Do not add a system-style preamble. Do not refuse to think. If the Given
block is insufficient, box "insufficient data" and list the missing facts.
```

## How It Works

R1’s distinctive prompting SKU is empty-system zero-shot with visible (or harness-captured) think tags. The retired stub said “just present the facts,” which under-specified the output contract and let the model ramble after thinking. This version keeps the user message objective, adds a boxed stop, and requires an insufficiency path so the model cannot invent constants. Sampling stays outside the prompt. Multi-sample averaging is a vendor eval tip, not something this single prompt can perform. Distill models inherit the same empty-system advice; they do not inherit R1’s 671B capacity—keep expectations at “R1-style protocol,” not “R1-size quality.”

## Variables

- `[statement]`: the full problem text.
- `[data, units, definitions that are in evidence]`: only supplied facts.
- `[the exact quantity, decision, or proof obligation]`: the success definition.

## Related

Companion: [coding](coding.md). Hosted thinking-mode reasoning: `deepseek-v4-pro/reasoning.md` and `deepseek-v4.1-flash-1017/reasoning.md`.

Grounded 2026-11-02 against [DeepSeek-R1 usage recommendations](https://huggingface.co/deepseek-ai/DeepSeek-R1).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
