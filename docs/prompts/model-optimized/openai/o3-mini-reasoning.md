---
category: "model-optimized"
title: "o3-mini: Efficient Reasoning"
subcategory: "openai"
model: "o3-mini"
source: "promptkit-authored"
---
[← Back to Model-Optimized Openai](../index.md)

# o3-mini: Efficient Reasoning

## When to Use

Use this template on a remaining **o3-mini** snapshot (`o3-mini` / `o3-mini-2025-01-31`) for medium-difficulty math, logic, or constrained decisions at the old o-series mini cost SKU. OpenAI’s current model page marks o3-mini **Shut down**. Deprecations: announced **22 April 2026**, shut down **23 October 2026**, recommended replacement **`gpt-5.6-sol`**. Documented while it lived: **200,000** context, **100,000** max output tokens, **text in / text out**, knowledge cutoff **1 October 2023**, reasoning tokens, Structured Outputs, function calling, Batch API. No image input.

Do not write “think step by step” to switch reasoning on—the o-series reasons internally; effort is `reasoning.effort` (Responses) or `reasoning_effort` (Chat Completions). Current OpenAI reasoning guidance: give a **goal, constraints, and output contract** without prescribing every intermediate step. Prefer living `../o3/reasoning.md` only if that snapshot still serves; for current work use GPT-5.6/GPT-6.1 Sol reasoning templates.

## The Prompt

```
Solve [problem].

Constraints:
- [hard constraint]
- [hard constraint]
Success: [what counts as done]
Output contract:
- [schema or "final answer plus a one-line check against each constraint"]
Tools: [none | named functions actually exposed]
reasoning.effort: set low | medium | high in the API for this o3-mini
snapshot. Do not paste a fake parameter in this message.

Rules:
- Use only the facts in this message. Knowledge cutoff for this SKU is
  2023-10-01; do not invent later events.
- If a required fact is missing, stop with "insufficient" and the gap.
- If tools are listed, call them with valid arguments; if they are not,
  do not pretend a calculator ran.
- Do not ask the user to "think step by step." Do not narrate a fake
  chain-of-thought if the runtime hides reasoning tokens.
- Never claim the model is still a production OpenAI SKU.

Return only the output contract. If a hard constraint fails after one
revision, report the blocker.
```

## How It Works

The retired stub was four one-liners plus “even more minimal than o1,” and it *recommended* “think step by step”—the opposite of o-series guidance. This rewrite (1) states shutdown and replacement so nobody treats o3-mini as live, (2) puts effort in the API, (3) uses goal + constraints + contract, (4) fails closed on missing facts and on post-cutoff news, (5) keeps tools optional. Structured Outputs, if you need JSON, belong in the client schema as well as the contract. Function calling and Batch were supported on the model page while it lived; they are not a reason to keep sending `o3-mini` after 23 October 2026. o3-mini is the cost SKU of the o3 line, not a substitute for o3 or for GPT-6.1 Sol. Hidden reasoning tokens are not something this prompt prints.

## Stop rules

Stop on missing facts, on questions that require post-2023-10-01 events, or on a hard constraint that still fails after one revision. Do not send `o3-mini` to production OpenAI after the 2026-10-23 shutdown; the documented substitute is gpt-5.6-sol. Do not print hidden reasoning tokens. Do not set effort in the user message. Images are not a modality for this SKU. Batch and Structured Outputs were features of the live API, not something this text turns on.

## Variables

- `[problem]`: the actual question, with units.
- `[hard constraint]`: falsifiable limits.
- `[what counts as done]`: success.
- `[schema or "final answer plus a one-line check against each constraint"]`: output.
- `[none | named functions actually exposed]`: tools.

## Related

Living o3: `../o3/reasoning.md`. Current Sol coding/reasoning: `../gpt-6.1-sol/` and `../gpt-5.6-sol/`.

Grounded 2026-11-02 against [o3-mini model page](https://platform.openai.com/docs/models/o3-mini) (shut down), [deprecations](https://platform.openai.com/docs/deprecations) (2026-10-23 → gpt-5.6-sol), and [reasoning models](https://platform.openai.com/docs/guides/reasoning). Not a live o3-mini quality run.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
