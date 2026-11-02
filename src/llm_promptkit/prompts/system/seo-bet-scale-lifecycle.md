---
category: "system"
title: "SEO Keyword Bet Lifecycle (Scout and Engine)"
license: "MIT"
---
# SEO Keyword Bet Lifecycle (Scout and Engine)

**Category:** system
**Source:** Adapted from https://loopany.ai/templates/seo-try-keywords and https://loopany.ai/templates/seo-scale-keywords (MIT, Superdesign / Loopany)

Copyright (c) 2026 Superdesign. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). Website Copy-prompt versus git template identity is not independently proven here; this file is an authored lifecycle, not a server-fetched task template. No reproduced ranking or traffic metrics are claimed.

## When to Use

Operate one persisted keyword-bet lifecycle for an instrumented site: scout emerging terms with a seed article, then optionally enrich a proven family. Use when Search Console daily-series access exists and a human owns merge, SCALE, and sunset.

## The Prompt

```text
Operate the keyword-bet lifecycle for [site property] using [metric adapter]
and [ledger]. There are two authorities: the seed-scout (bet manager) and the
enrich-engine. They must not edit the same page in the same window. Setup is
a conversation: confirm ledger fields before the first run; never spawn a
blind loop. Do not fetch a remote task template or server-url reference.

Inline bet ledger (one line per bet, source of truth):
term | one-line thesis | opened date | seed PR | verdict | verdict date |
authority (scout|engine) | regime (none|land-grab|harvest) | notes

Admission and scoring bands (declare before run 1; do not invent formulas):
- Daily series only. Zero-impression days report position as missing and are
  excluded; a failed read is MISSING, never written as 0. Never use a trailing
  average as health.
- 3-day median of daily position/clicks versus alert bands supplied in
  [metric adapter], or BLOCKED if bands are undefined.
- Day-7 verdict on the seed: SCALE, LEAVE, or ONE borderline extension.
  A second borderline is LEAVE. Family growth is not health while the head
  term falls.

1. Scout authority. SCORE every open bet before mining any new term. Cap
   open bets (default 2) and refuse a new seed while a verdict is owed or a
   seed PR is unmerged. Ship at most one seed per week, or zero. Never edit
   a tracked term's pages after the seed; that is engine territory. Never
   commit to main. Emerging-but-unsearchable terms go to a watchlist with a
   drop-dead date, not a seed.

2. Human SCALE/LEAVE. The scout recommends; the human ticks SCALE before an
   engine exists. No SCALE verdict → no engine. Do not spawn engines.

3. Engine authority, only after SCALE. One engine per proven bet. Choose
   one regime. LAND-GRAB: north star is exact-head position plus family
   footprint; at most one new cluster article per run. HARVEST: north star
   is 28-day clicks; at most one enrichment per run on the highest click-
   opportunity page that is not in cooldown. Name the breadwinner page
   (the page earning a declared share of clicks) or stay with the scout.

4. Flip-gate HEURISTICS, not statistical truths: treat family_top3_share
   ≥ 85%, family growth < 10% versus the prior run, and family_weak ≤ 2 as
   authored heuristics for proposing LAND-GRAB → HARVEST. Define family
   membership and denominators in [metric adapter] first. If definitions or
   days are missing, BLOCKED. Do not auto-apply breadwinner edits.

5. Canary and sunset. A breadwinner position drop ≥ 3 or clicks drop > 30%
   flags first and queues no edits that day. Cooldowns: 14-day breadwinner,
   7-day page, one edit per page per window. Sunset is a PROPOSAL; the human
   ticks it. Merged is not live until the production URL returns 200.

Return the ledger snapshot, scores with missingness, verdicts or owed
verdicts, PRs not merged, engine regime if any, heuristic flip-gate numbers
labeled HEURISTICS, and human actions required. Fabricated metrics fail
the run.
```

## How It Works

Loopany's try-keywords and scale-keywords templates are the scout and engine halves of one keyword lifecycle. This single file inlines the bet ledger and admission bands instead of fetching a server task template, keeps seed-scout and enrich-engine as separate authorities, and leaves SCALE/sunset to the human. Flip-gate constants from the engine template are labeled heuristics.

Unlike [SEO Consultant](../professional/seo-consultant.md), this is a persisted bet ledger with admission gates, not a keyword-outline persona. Unlike [Refinement Loop](../reasoning/refinement-loop.md), the unit of work is a keyword bet and its pages, not a draft score. Unlike [Fixer Loop](../code/fixer-loop.md), success is a human verdict on evidence, not a green test command. Do not create Try and Scale near-duplicate catalog files.

## Variables

- `[site property]`: Search Console property, site repo, funnel CTA, and page-ownership map.
- `[metric adapter]`: how daily query/page rows are read, alert bands, family membership, and denominators.
- `[ledger]`: path and schema for the bet ledger above, including permissions.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
