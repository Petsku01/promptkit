---
category: "model-optimized"
title: "Grok 2: Coding"
subcategory: "xai"
model: "grok-2"
source: "promptkit-authored"
---
[← Back to Model-Optimized Xai](../index.md)

# Grok 2: Coding

## When to Use

Use this template on a remaining Grok 2 coding endpoint or eval replica. **Grok 2 is archived-era lineage; superseded by grok-4.6.** It is not in the current xAI catalog (flagship at fetch: grok-4.7). Do not send this as if it were grok-4.6 agentic coding.

Keep the job to a function, fix, or review. Search tools are irrelevant unless the bug depends on a current docs page—then name whether Web Search is actually enabled. Prefer `../grok-4.6/coding.md` and `../grok-3-mini/coding.md` for stacks you still operate.

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

Be blunt about defects. Do not praise working code.

Procedure:
1. Restate the interface.
2. If code is present, name the defect in one sentence. No lecture.
3. Emit one complete, compilable artifact or a unified diff.
4. Tests in [framework]: happy, edge, error. Mark suggested unless a
   harness ran them.
5. If you cannot meet a constraint, stop and name it.

Do not invent passing tests. Do not claim you searched current docs
unless Web Search ran in this runtime.
```

## How It Works

The retired stub was seven casual asks (“keep it simple,” “don’t be boring”) without a contract. Direct style stays; the stop rule is the interface plus honest verification. Grok 2 must not be described as having a live X/docs feed—the current catalog says no SKU has realtime without search tools, and Grok 2 is gone from that catalog. Over-engineering is limited by “editable surface,” not by vibe. Architecture comparisons belong in a separate question with named options; this file is implement-or-fix. If the serving stack still exposes function calling, schemas live in the client, not as a wish in the user text. This is a historical coding SKU for residual harnesses, not a substitute for grok-4.6’s search-backed agent templates. Prefer grok-3-mini if you need a still-listed cheap coding prompt in this tree.

## Stop rules

Stop when the interface cannot be met or when tests did not run. Do not claim Grok 2 searched current library docs. Do not treat this slug as grok-4.6 agentic coding. Direct style does not waive the contract. Function schemas, if any, belong in the client. Context limits are whatever the replica still serves; this file does not invent a 128k figure from the retired README. Prefer grok-4.6 or grok-3-mini on stacks you still operate. Architecture A-vs-B questions belong in a dedicated prompt with named options, not as a side quest inside a fix.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges.
- `[conventions]`: style.
- `[snippet or files]`: write scope.
- `[framework]`: tests or none.

## Related

[analysis](analysis.md), [creative](creative.md), [realtime](realtime.md). Champion: `../grok-4.6/coding.md`.

Grounded 2026-11-02 against [xAI models](https://docs.x.ai/developers/models). Legacy lineage; superseded by grok-4.6.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
