---
category: "model-optimized"
title: "DeepSeek V4 Pro: Reasoning"
subcategory: "deepseek"
model: "deepseek-v4-pro"
source: "promptkit-authored"
---
# DeepSeek V4 Pro: Reasoning

## When to Use

Use this template when `deepseek-v4-pro` must solve a multi-step technical, mathematical, or architectural question with thinking mode on, optionally over a long document pack inside the 1M context. Hosted version DeepSeek-V4-Pro-0813: 1M context, 384K max output, thinking default `high`, no vision, tools legal if the client sends schemas. Effort mapping (OpenAI-format): `low`/`high`/`max`; several aliases collapse (`medium`→`high`, `xhigh`→`high`). In thinking mode, temperature/presence/frequency do nothing; `top_p` is ignored (fixed 0.95 with tools, else 1.0).

Prefer R1 empty-system prompts only on open R1 weights. Prefer Flash analysis for high-volume extraction. Do not claim Pro “replaces R1” as a universal fact; it is a different API with `reasoning_content`, not `<think>` tags.

## The Prompt

```
Solve or decide: [problem]

Domain: [math / systems / policy]
Given (evidence only):
[data, excerpts, constraints]

Question:
[the decision or quantity]

API: thinking enabled, effort high or max set in the request. Do not put
reasoning_effort in this text. If tools are attached, the client must replay
reasoning_content every turn.

Protocol:
1. Restate the problem and list hard constraints.
2. Separate givens, inferences, and gaps.
3. Decompose into sub-questions. Solve each; verify before combining.
4. For architecture choices, compare at most three options on complexity,
   failure modes, and reversibility. Drop any option that violates a hard
   constraint.
5. If a long corpus is attached, point to locations rather than summarizing
   first and then discarding the source.
6. If evidence is insufficient, stop. Name the measurement that would unblock.

Output after thinking:
- Answer or recommendation
- Evidence pointers
- Checks performed (substitution, bounds, contradiction scan)
- Reversal condition
- Gaps

No invented citations. No vision. No fake tool traces.
```

## How It Works

Pro’s thinking mode returns `reasoning_content` beside `content`. Without tools, prior CoT is ignored on the next turn; with tools, it must be replayed. The prompt therefore keeps the user-visible contract short and puts verification in the visible answer, because the next non-tool turn will not see the hidden CoT. Long-context guidance is “point, don’t pre-summarize away the source,” matching DeepSeek’s 1M envelope without claiming needle-perfect retrieval. Effort belongs in `reasoning_effort` / Anthropic `output_config.effort` / Responses `reasoning.effort`, not in prose. The reversal condition replaces the stub’s unearned confidence.

## Variables

- `[problem]`: the question.
- `[math / systems / policy]`: domain label.
- `[data, excerpts, constraints]`: evidence pack.
- `[the decision or quantity]`: success definition.

## Related

[coding](coding.md). Open-weight CoT: `deepseek-r1/reasoning.md`. Flash analysis: `deepseek-v4-flash/analysis.md`.

Grounded 2026-11-02 against [pricing](https://api-docs.deepseek.com/quick_start/pricing/) and [thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: insufficient placeholder input |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: insufficient placeholder input |
