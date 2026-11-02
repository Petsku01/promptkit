---
category: "model-optimized"
title: "Claude Sonnet 4: Reasoning"
subcategory: "anthropic"
model: "claude-sonnet-4"
source: "promptkit-authored"
---
# Claude Sonnet 4: Reasoning

## When to Use

Use this template when a remaining Sonnet 4 runtime must analyze, compare, or solve a constrained problem faster than an Opus-class investigation, with XML structure and an explicit recommendation. The API snapshot `claude-sonnet-4-20250514` is retired on Anthropic-operated platforms as of 2026-06-15 (deprecated 2026-04-14); migrate production traffic to `claude-sonnet-5-5`. This file exists so the catalog still has a Sonnet 4 reasoning SKU: structured analysis, tradeoff comparison, and short problem-solving—not Opus 4.7’s multi-hypothesis RCA and not 3.7’s hybrid-thinking activation ritual.

Do not use it for long-horizon coding, for claiming the model is still the “best balance of speed and capability” as a live 2026 ranking, or for summarization-only jobs that need no decision. If evidence is missing, the output must say so rather than averaging competing sources into a false consensus.

## The Prompt

```xml
<task>
Analyze or decide: [question].
</task>

<context>
[background that is in evidence]
Missing information: [gaps]
</context>

<constraints>
- Hard limits: [limits]
- Success looks like: [decision or artifact]
- Time/depth budget: [short / medium]
</constraints>

<instructions>
Think through the task in this order. Keep the write-up inside the depth
budget; Sonnet 4 is a mid-latency SKU, not an unbounded research agent.

1. Restate the question and the hard limits in one short block.
2. List what is known versus inferred versus missing.
3. If this is a comparison, score each option only on the supplied criteria.
   Do not invent extra criteria to make a favorite win.
4. If this is a problem, propose at most three approaches, drop any that
   violate a hard limit, and work the survivor with a check at the end.
5. Give a recommendation with a confidence label (high / medium / low) and
   the single fact that would reverse it.
6. If missing information blocks the decision, stop and name the next
   measurement. Do not fill gaps with typical-industry defaults.
</instructions>

<output>
<findings>[key observations tied to context]</findings>
<recommendation>[choice or solution]</recommendation>
<tradeoffs>[what you give up]</tradeoffs>
<reversal>[what would change the call]</reversal>
<gaps>[unresolved]</gaps>
</output>
```

## How It Works

Sonnet 4 prompting still benefits from Anthropic’s XML separation of task, context, and output. The retired stub asked for “insights and recommendations” without a reversal test, which produced fluent but unfalsifiable advice. This version caps the number of approaches, forbids extra criteria, and requires a reversal fact so the recommendation is a decision record, not a vibe. Depth budget matches the historical product role (interactive, not overnight). Confidence labels are requested because later Claude docs emphasize calibrated honesty; they are not measured Brier scores. Lifecycle honesty is in When to Use, not in the fenced prompt, so eval harnesses can still feed the XML to a local 4.x replica without the model arguing about deprecation.

## Variables

- `[question]`: the decision or analysis target.
- `[background that is in evidence]`: only text or data in the request.
- `[gaps]`: known unknowns.
- `[limits]`: hard constraints.
- `[decision or artifact]`: what “done” looks like.
- `[short / medium]`: keeps the answer inside an interactive budget.

## Related

Companion: [coding](coding.md). Heavier investigations: `claude-opus-4.7/reasoning.md`. Hybrid-thinking ancestor: `claude-3.7-sonnet/reasoning.md`.

Grounded 2026-11-02 against [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
