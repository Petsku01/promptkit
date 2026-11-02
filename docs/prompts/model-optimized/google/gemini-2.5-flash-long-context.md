---
category: "model-optimized"
title: "Gemini 2.5 Flash: Long Context"
subcategory: "google"
model: "gemini-2.5-flash"
source: "promptkit-authored"
---
[← Back to Model-Optimized Google](../index.md)

# Gemini 2.5 Flash: Long Context

## When to Use

Use this template when `gemini-2.5-flash` must answer questions over many documents, a transcript, or a multi-file snapshot that fits in the 1,048,576 input-token window. Google’s long-context guide (updated 2026-10-15) still applies to 2.5: place the query **after** the corpus, delimit documents, expect higher time-to-first-token on huge prompts, and use context caching when the same pack is reused. 2.5 Flash uses **separate** 1M input and 64K output budgets; do not treat them as Gemini 4’s shared 1M window. The model is not deprecated but is gated to prior users; new apps should prefer 3.8 Flash.

Good fits: corpus Q&A with citations, meeting-transcript extraction, batch classification of many items in one call. Bad fits: claiming 99% needle accuracy on multi-needle hunts (the guide warns accuracy drops with many needles), or using this instead of [coding](coding.md) when you need a patch.

## The Prompt

```
You will answer from the corpus below. Do not use outside facts unless the
question explicitly allows them.

--- corpus start ---
Document 1 — id=[id] title=[title]
[text]

Document 2 — id=[id] title=[title]
[text]
--- corpus end ---

Question: [question]

Instructions:
1. If the answer is not in the corpus, say "not in corpus" and list what is
   missing. Do not fill from general knowledge.
2. Quote or paraphrase with an id and a short span (section heading or
   nearby sentence). Multiple needles: list each hit; do not merge them
   into one confident sentence if they conflict.
3. For transcripts, separate decisions, action items (owner + due if
   stated), and unresolved issues.
4. For code trees, cite path and symbol, not a vibe summary.
5. Keep the final answer inside a 64K output budget. Prefer a table or
   bullets over an essay.
6. If this pack will be reused, the application should set a cache;
   this prompt does not create one.

Output:
- Answer
- Evidence: id | span | support (direct / inferred)
- Conflicts
- Gaps
```

## How It Works

Flash’s 1M window invites packing many items, but Google’s own FAQ says performance is best with the question last and that multi-needle retrieval is weaker than single-needle demos. Delimiters and ids make citations checkable. “Not in corpus” is the stop rule the retired stub lacked. Caching is an API feature (`context caching`) billed per hour; mentioning it reminds operators without pretending the prompt allocated a cache. Audio/video may be attached as native media on 2.5 Flash; if you only paste a lossy transcript, say so. Output is capped at 65,536 tokens—ask for tables so the model does not spend the budget on recap.

## Variables

- `[id]` / `[title]` / `[text]`: one delimited document each.
- `[question]`: always after the corpus.

## Related

[coding](coding.md), [quick-tasks](quick-tasks.md). Family README already indexes these three. Deeper reasoning: `../gemini-2.5-pro/reasoning.md`.

Grounded 2026-11-02 against [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) and [Long context](https://ai.google.dev/gemini-api/docs/long-context).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
