---
category: "model-optimized"
title: "Grok 2: Analysis"
subcategory: "xai"
model: "grok-2"
source: "promptkit-authored"
---
[← Back to Model-Optimized Xai](../index.md)

# Grok 2: Analysis

## When to Use

Use this template only on a remaining **Grok 2** replica, partner, or historical eval harness. Grok 2 is **archived-era lineage; superseded by grok-4.6** in this catalog (xAI’s live flagship at fetch time is grok-4.7). Grok 2 is **absent** from the current xAI model catalog. Do not treat a `grok-2` string as a live API ID.

Direct tone is an author style choice, not a documented capability. **No Grok SKU has realtime knowledge without search tools.** Current xAI docs: enable Web Search or X Search, or the model has only training-cut data. If your Grok 2 stack never had those tools, this prompt must not pretend it fetched X.

Prefer `../grok-4.6/analysis.md` for current work. Sibling slots in this folder cover coding, creative, and realtime.

## The Prompt

```
Analyze [topic] using only the sources below.

Sources (quotes, links, dates — or "none"):
[paste]

Search tools in this runtime: [web | X | both | none]
If none, you have no current-events access. Do not invent a feed.

Stance: direct. Separate facts from opinion. Do not hedge a sourced
fact; do not present an opinion as a fact.

Cover:
1. What is established in the sources (quote or cite).
2. What is disputed, with each side’s evidence.
3. What is missing. If search is none and the question needs current
   data, answer "unsupported-current-facts" for that part.
4. Strongest contrary case that still fits the sources.
5. Bottom line in one paragraph.

Do not sugarcoat. Do not fabricate citations, timestamps, or “what
people on X are saying.” Stop if sources + tools cannot support a
claim.
```

## How It Works

The retired stub was a pile of “don’t sugarcoat / hot take / devil’s advocate” lines with no evidence rule—the failure mode that made Grok-style prompts look like unconstrained ranting. This rewrite keeps a blunt voice but binds it to sources and an honest search-tool flag, matching current xAI catalog language (realtime requires Web Search / X Search). Contrarian coverage is a structured section, not a dare to ignore facts. Archived Grok 2 must not be described as the 4.6/4.7 product: it is missing from the live catalog entirely, unlike grok-3 which at least has a documented May 2026 redirect. Context length for Grok 2 is not restated here because it is not on the live catalog; use the serving stack’s limit. Optional humor belongs in [creative](creative.md), not in a findings list. Stop when sources plus tools cannot support a claim.

## Stop rules

Stop when sources plus enabled tools cannot support a current-events claim. Do not treat grok-2 as a live xAI ID; it is archived-era lineage, superseded by grok-4.6, and missing from the current catalog. Do not invent X sentiment. Do not mix creative roasting into the findings list. Direct tone is not a substitute for a citation. If search is none, say unsupported-current-facts for the part that needs a feed.

## Variables

- `[topic]`: the question.
- `[paste]`: evidence, or none.
- `[web | X | both | none]`: tools actually enabled.

## Related

[coding](coding.md), [creative](creative.md), [realtime](realtime.md). Champion: `../grok-4.6/analysis.md`. Living cheap SKU: `../grok-3-mini/`.

Grounded 2026-11-02 against [xAI models](https://docs.x.ai/developers/models) (no grok-2; no realtime without search). Legacy lineage; superseded by grok-4.6.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
