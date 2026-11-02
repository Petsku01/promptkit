---
category: "model-optimized"
title: "Grok 2: Creative"
subcategory: "xai"
model: "grok-2"
source: "promptkit-authored"
---
[← Back to Model-Optimized Xai](../index.md)

# Grok 2: Creative

## When to Use

Use this template on a remaining Grok 2 replica when the user wants satire, a witty reply, or a short story **and** has named the target and the harm boundary. Grok 2 is **archived-era lineage; superseded by grok-4.6**. Humor is an author-selected style instruction, not a documented Grok 2 capability claim, and it is not a license to produce harassment. Current xAI docs still apply in spirit: no live X/current-events access without search tools—do not “quote the timeline” unless X Search actually ran.

Skip this file for analysis, coding, or news. Those are sibling templates. Do not use it on grok-4.6 (that folder has no creative slot on purpose).

## The Prompt

```
Write [form: witty reply | satire | short story | explainer-with-humor]
about [subject].

Audience: [who]
Tone: clever, not cruel. No slurs. No real-person humiliation.
Length: [limit]
Must include: [devices, e.g. one twist / one accurate analogy]
Must not include: [off-limits topics, names, or claims]

Factual bits: if the piece asserts a current event, that assertion is
only allowed when search tools ran and a source URL is listed in a
trailing "facts" line. Otherwise keep the piece clearly fictional or
evergreen. Search tools this runtime: [web | X | both | none].

Output:
1. The piece only, in the requested form.
2. After a blank line, a one-line "facts:" note — "none" or URLs.

Stop at the length limit. Do not add a lecture about humor.
```

## How It Works

The retired Finnish “Luova” stub mixed roast, Onion-style satire, alien explainers, and social posts with “keep it light” as the only brake. That is how creative Grok prompts become mean or fake-news. This rewrite keeps one form, a harm boundary, a length cap, and a facts trailer so jokes cannot smuggle unsourced current events—the same realtime limitation the live catalog documents for every Grok text model. Direct voice stays in the piece; the facts line is dry. Archived Grok 2 is not grok-4.6, and the 4.6 folder has no creative slot, so this file is the lineage’s humor template rather than a live product claim. Roasts of real private individuals are out of scope even if the old stub invited them. If the runtime refuses the subject, report the refusal rather than laundering it as irony.

## Stop rules

Stop at the length limit, at the harm boundary, or when a current-event joke would need search that did not run. Do not roast private people. Do not present fiction as news. Grok 2 is archived-era lineage, superseded by grok-4.6; humor is an author style, not a vendor capability row. The facts trailer is mandatory even when it says “none.” If the host refuses the subject, report the refusal.

## Variables

- `[form: witty reply | satire | short story | explainer-with-humor]`: one form.
- `[subject]`: topic.
- `[who]`: audience.
- `[limit]`: length.
- `[devices, e.g. one twist / one accurate analogy]`: required craft.
- `[off-limits topics, names, or claims]`: hard no.
- `[web | X | both | none]`: search tools.

## Related

[analysis](analysis.md), [coding](coding.md), [realtime](realtime.md). Champion: `../grok-4.6/`.

Grounded 2026-11-02 against [xAI models](https://docs.x.ai/developers/models) (no grok-2; no realtime without search). Legacy lineage; superseded by grok-4.6.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
