---
category: "model-optimized"
title: "Llama 3.3: Analysis"
subcategory: "meta"
model: "llama-3.3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Meta](../index.md)

# Llama 3.3: Analysis

## When to Use

Use this template with **Llama 3.3 70B Instruct** for document analysis, comparison, and grounded Q&A. Meta’s card: text-only 70B, **128k** context, knowledge cutoff **December 2023**, release **6 December 2024**, officially supported languages English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai. It is instruction-tuned only (no pretrained sibling). Vendor text says it improves on Llama 3.1 70B and, for some applications, approaches Llama 3.1 405B—that is Meta’s claim, not a promptkit score; do not paste the card’s MMLU/IFEval table into the prompt.

The chat template is the same as Llama 3.1. Zero-shot function calling may live in the system or user message; builtin Brave Search, Wolfram, and Code Interpreter exist on 3.3 the same way as 3.1, but this analysis prompt does not turn them on unless you list them. Prefer [coding](coding.md) for implementation. Llama 4 living files are the current Meta open-weight line.

## The Prompt

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You analyze only the supplied sources. Label each claim as sourced,
inferred, or unknown. Do not use the web unless a builtin tool is
explicitly listed below (default: none).

<|eot_id|><|start_header_id|>user<|end_header_id|>

Question: [question]
Sources:
[paste documents, tables, or notes]

Constraints:
- Language: [one of the 8 supported, or off-card with that caveat]
- Hard limits: [budget, policy, or "none"]
- If a needed fact is not in the sources, write "not in sources"
  rather than filling from parametric memory.
- Do not invent quotations.

Output:
1. Findings: numbered claims, each tagged sourced | inferred | unknown.
2. Counter-reading: the strongest interpretation that still fits the
   sources.
3. Gaps: what is missing to answer the question fully.
4. Bottom line: one paragraph, or "insufficient sources".

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## How It Works

The retired stub asked for “deep analysis” and “step by step” with no evidence rule. 70B instruct models will complete a narrative from training data unless you forbid it. Tagging sourced vs inferred vs unknown is the stop rule: a polished brief that cannot point at a source is not done. The counter-reading line blocks one-sided summaries. Builtin tools stay off by default so a local 3.3 deployment without Brave/Wolfram does not hallucinate search; if you do enable them, use the 3.1 builtin format and `<|eom_id|>` on tool turns, which this analysis job does not. Zero-shot custom functions may sit in the user message on 3.3—the same flexible format as 3.2—but analysis here is source-grounded text, not a tool loop. 128k holds a long memo, not an unbounded corpus—say so in the sources block if you truncated. December 2023 cutoff means post-cutoff events are unknown unless supplied. Llama 4 analysis templates are the later SKU.

## Variables

- `[question]`: the actual ask.
- `[paste documents, tables, or notes]`: evidence only.
- `[one of the 8 supported, or off-card with that caveat]`: reply language.
- `[budget, policy, or "none"]`: hard limits.

## Related

[coding](coding.md). Llama 3.2: `../llama-3.2/`. Llama 4: `../llama-4/analysis.md`.

Grounded 2026-11-02 against Meta’s [Llama 3.3 prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/) and [Llama 3.3 model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md). Vendor benchmark rows are not promptkit scores.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
