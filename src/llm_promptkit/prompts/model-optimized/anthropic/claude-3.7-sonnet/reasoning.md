---
category: "model-optimized"
title: "Claude 3.7 Sonnet: Hybrid Reasoning"
subcategory: "anthropic"
model: "claude-3.7-sonnet"
source: "promptkit-authored"
---
# Claude 3.7 Sonnet: Hybrid Reasoning

## When to Use

Use this template when a remaining Claude 3.7 Sonnet integration must solve a multi-constraint problem that needs an explicit plan, a check against those constraints, and a short final answer. Anthropic's prompting guidance still recommends XML tags to separate task, context, and output contract; 3.7's hybrid-reasoning SKU was designed so that an instruction to think before answering would spend extra internal work on hard cases. Do not use this prompt to re-enable a retired API ID. On Anthropic-operated platforms the snapshot `claude-3-7-sonnet-20250219` is retired (deprecated 2025-10-28, retired 2026-02-19); the documented replacement is `claude-sonnet-5-5`. Keep the template for residual partner, self-hosted, or historical eval harnesses that still name 3.7, and for comparing how a hybrid-thinking prompt differs from later adaptive-thinking models.

Skip this file for ordinary coding (see the living [coding](coding.md) sibling) and for current Opus 4.x / 5.x agent loops. If the runtime no longer accepts 3.7, migrate the same XML skeleton onto an active Sonnet rather than inventing a live 3.7 result.

## The Prompt

```xml
<task>
Solve [problem] under the constraints below. This is a hybrid-reasoning job:
plan first, then answer. Do not skip the plan when the problem has more than
one interacting constraint.
</task>

<context>
Domain: [domain]
Known facts: [facts that are evidence, not guesses]
Unknowns: [what is missing]
Disallowed actions: [side effects the answer must not assume]
</context>

<constraints>
1. [hard constraint]
2. [hard constraint]
3. [soft preference, labeled as preference]
</constraints>

<instructions>
1. Restate the problem in one sentence and list every hard constraint.
2. Sketch two candidate approaches. Drop any approach that violates a hard
   constraint; do not keep it as a "maybe".
3. Work the surviving approach step by step. After each material inference,
   note whether it is a given fact, a deduction, or an assumption.
4. Check the draft answer against every hard constraint. If a check fails,
   revise once. If it still fails, report the blocker instead of forcing a
   solution.
5. Return only the output contract below. Do not add a preamble.
</instructions>

<output>
<plan>[short plan, then discarded alternatives]</plan>
<answer>[final result]</answer>
<checks>[one line per hard constraint: pass / fail / untested]</checks>
<assumptions>[assumptions that remain]</assumptions>
</output>
```

## How It Works

The XML regions keep the problem, the evidence, and the output schema from collapsing into one paragraph—the failure mode that made the retired stub too thin to steer hybrid thinking. Asking for two approaches and an explicit drop-rule counters the habit of defending the first idea. Labeling facts versus assumptions matches Anthropic's honesty guidance and stops the model from treating a missing input as a solved constraint. The final check list is the stop rule: a pretty answer that cannot tick every hard constraint is not done. Extended thinking, if the runtime still exposes it, is an API control (`thinking` / effort), not a sentence inside the user message that pretends to flip a switch. This prompt never claims a tool ran, never invents a passing test, and never treats 3.7 as the current Claude flagship.

## Variables

- `[problem]`: the actual question, including units and success definition.
- `[domain]`: enough setting that jargon is not guessed.
- `[facts that are evidence, not guesses]`: only material you can point to.
- `[what is missing]`: gaps the model must not silently fill.
- `[side effects the answer must not assume]`: writes, spends, deploys, irreversible actions.
- `[hard constraint]`: falsifiable limits; keep preferences in a separate labeled item.

## Related

Living sibling: [coding](coding.md). Current Claude prompting champions live under `claude-opus-4.8/` and later 5.x docs; this file is the 3.7 hybrid-reasoning SKU, not a substitute for those.

Grounded 2026-11-02 against Anthropic [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Capability notes are vendor documentation, not promptkit live scores.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
