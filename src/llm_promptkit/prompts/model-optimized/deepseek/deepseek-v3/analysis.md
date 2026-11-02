---
category: "model-optimized"
title: "DeepSeek V3: Analysis"
subcategory: "deepseek"
model: "deepseek-v3"
source: "promptkit-authored"
---
# DeepSeek V3: Analysis

## When to Use

Use this template with open-weight DeepSeek-V3 (671B total / 37B active, 128K context per the model card) when you need structured document analysis, comparison, or critical evaluation without R1’s empty-system ritual and without V4’s 1M hosted window. V3’s card describes a general MoE chat model that distilled some R1 reasoning patterns into ordinary assistant turns, with vendor-reported strength on English, code, math, and Chinese evals. Hosted DeepSeek traffic in 2026 is `deepseek-flash` and `deepseek-v4-pro`; keep this file for local V3, residual `deepseek-chat`-era replicas, and catalog completeness beside the living [json-output](json-output.md) sibling.

Do not dump entire 1M-token corpora here—the documented window is 128K. Do not paste fabricated MMLU numbers into the user prompt. Prefer [coding](coding.md) / [math](math.md) for those aspects.

## The Prompt

```
Analyze the materials below. Stay inside what they actually contain.

Materials:
[documents or excerpts, clearly delimited]

Question:
[what the analysis must decide or extract]

Output contract:
1. Inventory: one line per document (title/id, length, what it is).
2. Findings: bullet list, each bullet a claim plus a pointer (document id +
   section or quote span). Mark support as direct / inferred / not present.
3. Comparison table only if two or more items were supplied:
   aspect | item A | item B | winner for [use case] | evidence
4. Critique: strongest argument, weakest argument, missing evidence.
5. Conclusion: at most five sentences, plus a residual-uncertainty line.

Rules:
- If the materials do not contain the answer, write "not in materials"
  rather than filling from world knowledge.
- Do not invent citations, page numbers, or statistics.
- Keep the chain of thought short and visible as numbered steps, then the
  contract. This is V3 instruct, not R1 think-tags.
```

## How It Works

V3 is an instruct MoE, so a system or user preamble is allowed (unlike R1). The prompt still forces pointers and a “not in materials” stop because 128K NIAH charts on the card are vendor retrieval tests, not a license to hallucinate a missing PDF. Numbered steps give the distilled-reasoning behavior something to latch onto without asking for R1 `<think>` tags that V3 may not emit. Comparison is gated on actually having two items so the model does not invent a competitor. JSON extraction remains the other living file; this analysis template stays prose-plus-table so the two SKUs do not duplicate.

## Variables

- `[documents or excerpts, clearly delimited]`: labeled blocks; do not merge sources.
- `[what the analysis must decide or extract]`: the question.
- `[use case]`: the criterion for any “winner” column.

## Related

Living leftover: [json-output](json-output.md). This batch also restores [coding](coding.md) and [math](math.md). Later hosted analysis: `deepseek-v4-flash/analysis.md`.

Grounded 2026-11-02 against [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) (128K context, instruct chat model). Card benchmarks are vendor-reported.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
