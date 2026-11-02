---
category: "model-optimized"
title: "Grok 3: Reasoning"
subcategory: "xai"
model: "grok-3"
source: "promptkit-authored"
---
# Grok 3: Reasoning

## When to Use

Use this template on a remaining `grok-3` reasoning job that still names that SKU. **Grok 3 is archived-era lineage; superseded by grok-4.6.** Retired from the xAI API **15 May 2026, 12:00 PT**; the slug then **redirects to `grok-4.3` with `none` reasoning effort**. That redirect is the opposite of “keep thinking”: if you needed Grok 3-style deliberation after that date, the vendor path is a current model with an explicit `reasoning_effort`, not the grok-3 name.

Do not ask this prompt to pull “latest developments” unless Web Search / X Search ran. Current catalog: no Grok text model has realtime without those tools. Prefer `../grok-4.6/reasoning.md` and `../grok-3-mini/reasoning.md`.

## The Prompt

```
Problem: [problem]
Domain: [domain]
Known facts: [evidence]
Unknowns: [gaps]
Hard constraints: [list]
Search tools: [web | X | both | none]

This SKU: grok-3 (archived). After 2026-05-15 a grok-3 API slug may be
grok-4.3 at none effort. Do not claim a thinking trace ran unless the
runtime actually exposes one.

Procedure:
1. Restate the problem and list every hard constraint.
2. Drop any approach that violates a hard constraint.
3. Work the surviving approach. Tag each step fact | deduction |
   assumption.
4. If current events are required and search is none, mark that branch
   unsupported-current-facts. Do not invent headlines.
5. Check the draft against every hard constraint. If a check fails,
   revise once; if it still fails, report the blocker.

Output:
- plan
- answer
- checks (one line per hard constraint: pass | fail | untested)
- assumptions
- sources (URLs only if tools returned them; else "none")

Be direct. Do not hedge a sourced fact. Do not present a preference as
a proof.
```

## How It Works

The retired stub promised “real-time information access,” “expert opinions,” and “be bold”—three ways to fabricate. xAI’s live rule is no realtime without search tools; Grok 3’s live rule is that the slug is retired and redirected with **none** effort. The prompt therefore (1) states the lifecycle, (2) requires constraint checks, (3) fails closed on current facts, (4) keeps a blunt voice without treating bluntness as evidence. Contrarian takes belong only as a labeled alternative that still fits the facts. If you need reasoning after the retirement date, set `reasoning_effort` on grok-4.3/4.6/4.7 rather than hoping the grok-3 alias thinks. Family champion reasoning is grok-4.6. grok-3-mini remains the living cheap reasoning file in this tree.

## Stop rules

Stop when a hard constraint fails twice, when current facts are required and search is none, or when the runtime is the post-retirement grok-3 alias (grok-4.3 none) and the job needed deliberation—migrate instead of pretending. Do not invent expert opinions. Do not treat bluntness as proof. Archived-era lineage; superseded by grok-4.6. Living cheap reasoning: grok-3-mini. If the runtime still exposes encrypted reasoning on a later Grok, that is an API include, not a sentence in this user prompt.

## Variables

- `[problem]`: question and success definition.
- `[domain]`: setting.
- `[evidence]`: only material you can point to.
- `[gaps]`: what must not be filled silently.
- `[list]`: hard constraints.
- `[web | X | both | none]`: tools.

## Related

[coding](coding.md). Champion: `../grok-4.6/reasoning.md`. Living mini: `../grok-3-mini/reasoning.md`.

Grounded 2026-11-02 against [May 15, 2026 model retirement](https://docs.x.ai/developers/migration/may-15-retirement) (`grok-3` → grok-4.3 none) and [xAI models](https://docs.x.ai/developers/models). Legacy lineage; superseded by grok-4.6.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
