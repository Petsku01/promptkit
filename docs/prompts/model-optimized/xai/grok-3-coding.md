---
category: "model-optimized"
title: "Grok 3: Coding"
subcategory: "xai"
model: "grok-3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Xai](../index.md)

# Grok 3: Coding

## When to Use

Use this template on a remaining `grok-3` slug or replica. **Grok 3 is archived-era lineage; superseded by grok-4.6.** xAI retired `grok-3` from the API **15 May 2026, 12:00 PT**. After that time, requests to the slug **redirect to `grok-4.3` with `none` reasoning effort** and are billed at 4.3 prices unless you change the model field. The documented way to keep coding quality is to migrate explicitly (xAI’s later recommendation for code workloads is not “stay on grok-3”).

Do not treat redirect behavior as “Grok 3 still exists.” For current coding, use `../grok-4.6/coding.md`. For a still-listed cheap SKU in this tree, see `../grok-3-mini/coding.md`. Direct tone is style, not a capability claim.

## The Prompt

```
Write or repair [language] code for [purpose].

Interface:
- Inputs: [parameters]
- Outputs: [return or side effects]
- Errors: [what must raise or return]
Constraints:
- Edges: [list]
- Style: [conventions]
- Editable surface: [snippet or files]
Existing code or error (optional):
[paste]

Runtime note: if this request still uses the grok-3 slug after
2026-05-15, the vendor redirect is grok-4.3 with none reasoning
effort. Do not pretend a retired Grok 3 thinking stack is running.

Procedure:
1. Restate the interface.
2. If code is present, name the defect in one sentence. Be blunt.
3. Emit one complete, compilable artifact or a unified diff.
4. Tests in [framework]: happy, edge, error. Mark suggested unless a
   harness ran them.
5. If a constraint cannot be met, stop and name it.

No invented pass output. No current-docs claims without search tools.
```

## How It Works

The retired stub mixed “no over-engineering” with architecture hole-poking and no verification slot. This rewrite is one coding contract plus an honest lifecycle line so eval harnesses that still send `grok-3` know they may be talking to grok-4.3-none. Reasoning effort is an API field on later Grok models; it is not something you flip with “think hard” in the user message, and the grok-3 redirect specifically uses **none**. After 15 May 2026, continuing to send the old slug also bills at grok-4.3 rates—the migration page says so; this prompt does not pick your replacement. Search is still not implied by the model name. Stop at the interface. For agentic coding on a current ID, use grok-4.6; for a still-listed cheap SKU, grok-3-mini.

## Stop rules

Stop when the interface cannot be met. Do not assume grok-3 still thinks: after 2026-05-15 the xAI slug redirects to grok-4.3 with none reasoning effort and 4.3 pricing. Do not set effort in the user message. Do not claim search ran. This folder is archived-era lineage, superseded by grok-4.6. For a living cheap coding SKU use grok-3-mini; for current agentic coding use grok-4.6.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges.
- `[conventions]`: style.
- `[snippet or files]`: write scope.
- `[framework]`: tests or none.

## Related

[reasoning](reasoning.md). Champion: `../grok-4.6/coding.md`. Living mini: `../grok-3-mini/coding.md`.

Grounded 2026-11-02 against [Grok model retirement (May 15, 2026)](https://docs.x.ai/developers/migration/may-15-retirement) and [xAI models](https://docs.x.ai/developers/models). Legacy lineage; superseded by grok-4.6.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
