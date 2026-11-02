---
category: "model-optimized"
title: "Claude Opus 4.7: Analysis"
subcategory: "anthropic"
model: "claude-opus-4.7"
source: "promptkit-authored"
---
[← Back to Model-Optimized Anthropic](../index.md)

# Claude Opus 4.7: Analysis

## When to Use

Use this template when `claude-opus-4-7` must turn a large evidence pack—documents, diagrams, or screenshots—into a scored, source-linked audit rather than a narrative essay. Anthropic lists Opus 4.7 as an active legacy model (released 2026-04-16, retirement not sooner than 2026-04-16+1y), with a 1M-token context, 128K max output (300K only on the Batch API beta), adaptive thinking, default effort `high`, and text-plus-image input. Knowledge cutoff is January 2026. Anthropic recommends considering a move to Opus 5.5; this file does not claim 4.7 is the current Opus flagship.

Prefer this over the living [reasoning](reasoning.md) file when the job is comparative or visual (system audit, screenshot/diagram extraction, competing-product table) and over [long-horizon](long-horizon.md) when no repository tools will run. Do not use it to invent pixel-level OCR accuracy numbers, health scores out of 100, or “unmatched vision” marketing. If no image is attached, say so; a 1M window is not evidence.

## The Prompt

```
Audit [system or corpus] using only the materials supplied in this request.

Materials: [documents, diagrams, screenshots, or excerpts]
Questions the audit must answer: [questions]
Scope in: [surfaces]
Scope out: [surfaces not to invent findings for]
Audience: [operators / leadership / engineers]
Thinking/effort: set in the API (adaptive thinking, default effort high). Do not
embed a fake thinking parameter in this message.

Work in this order:
1. Inventory every supplied artifact. For images, describe visible elements with
   spatial references and transcribe readable text. Mark blur, crop, and
   unreadable regions instead of guessing.
2. Build an evidence ledger: claim, source location, support (direct / inferred /
   unsupported). Do not promote an inference to a fact.
3. Score only the in-scope surfaces. Use the labels current / partial / missing /
   not evidenced. Risk is critical / high / medium / low, and only when a
   concrete failure mode is stated.
4. Cross-check contradictions across artifacts. Prefer the more specific primary
   source; if they conflict, keep both rows and explain the conflict.
5. Stop when every question is answered or explicitly blocked by missing
   evidence. Do not pad with generic best-practice advice outside scope.

Output:
- Executive summary: at most five bullets a decision-maker can act on.
- Ledger table: surface | finding | evidence pointer | support | risk | gap.
- Unresolved questions: what to collect next. No fabricated screenshots,
  metrics, or scores.
```

## How It Works

Opus 4.7 follows instructions literally, so the prompt names inventory, ledger, scoring, contradiction, and stop as ordered steps rather than a mood. Adaptive thinking and effort stay in request configuration; stuffing “think harder” into the user text is not the documented control. The ledger forces source pointers because a 1M context still drops needles when many facts compete—Anthropic’s own prompting guidance asks for structure and honesty, not silent synthesis. Vision work is allowed because the model card lists image input, but the template requires an actual attachment and an unreadable-region disclosure so the model cannot hallucinate UI copy. Scope-out and “not evidenced” prevent the retired stub’s fake 0–100 health scores. The prompt does not grant tools, deploy, or treat Batch 300K output as the normal cap.

## Variables

- `[system or corpus]`: the named target, not “the codebase in general”.
- `[documents, diagrams, screenshots, or excerpts]`: attach or paste; note what is absent.
- `[questions]`: the audit’s acceptance criteria.
- `[surfaces]` / `[surfaces not to invent findings for]`: hard scope.
- `[operators / leadership / engineers]`: controls summary tone, not evidence depth.

## Related

Living siblings: [reasoning](reasoning.md), [long-horizon](long-horizon.md), and this folder’s [coding](coding.md). Champion Opus prompting: `claude-opus-4.8/analysis.md`.

Grounded 2026-11-02 against the [Opus 4.7 model reference](https://platform.claude.com/docs/en/models/opus-4-7/overview) and [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations). Specs are vendor claims, not promptkit inference results.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
