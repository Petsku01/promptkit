---
category: "reasoning"
title: "STORM Persona Interview Outline Polish"
license: "MIT"
---
# STORM Persona Interview Outline Polish

**Category:** reasoning
**Source:** Adapted from https://github.com/stanford-oval/storm/blob/main/knowledge_storm/storm_wiki/modules/knowledge_curation.py, outline_generation.py, and article_polish.py (MIT, Stanford OVAL)

Copyright (c) 2024 Stanford Open Virtual Assistant Lab. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). This workflow drafts a sourced article outline and polish; it does not publish to Wikipedia or any live encyclopedia.

## When to Use

Build a multi-perspective technical survey by interviewing simulated expert sources through search, then refining an outline and polishing repetition. Use when coverage of viewpoints matters more than a supervisor splitting independent research units.

## The Prompt

```text
Run a persona-interview curation pipeline for [topic] with [personas] under
[turn budget]. Produce a sourced outline and polished draft for a human editor.
Do not publish, upload, or imply that output becomes a Wikipedia page. Without
search tools, return a labeled specification and stop live interviewing.

1. For each persona, run an asker/expert cycle. The asker holds that persona's
   focus and asks one new question at a time about [topic], never repeating a
   prior question. The expert may only answer from gathered search results for
   that question. If the gathered information cannot support an answer, the
   expert must say so and name the gap; do not hallucinate.

2. Convert each question into a short list of search queries, fetch, then
   answer with support from those results. Every informative sentence should
   be attributable. Prefer diverse sources when they are actually retrieved.

3. Stop a persona interview on a typed completion signal, not a thank-you
   utterance. Emit INTERVIEW_COMPLETE when the asker has no further distinct
   question, when [turn budget] (default max_turn) is exhausted, or when the
   question field would be empty. Empty question is a stop, not a prompt to
   improvise. Do not continue after INTERVIEW_COMPLETE.

4. Draft an outline from the topic alone using heading levels (#, ##, ###)
   and nothing else. Do not put the topic name in the outline body. Then
   improve that outline using the conversation history. The previous outline
   is an INPUT named old_outline; do not re-derive it as an output field and
   do not ignore the supplied draft. Keep only heading structure in the
   refined outline.

5. From the refined outline and collected answers, write section drafts with
   inline numeric citations mapped to URLs or document names. Write a lead
   of at most four paragraphs that identifies the topic, context, notability,
   and major disputes, with citations. Then polish: delete repeated passages
   only, keep non-repeated text, keep citations and heading structure.

6. Bound work: one interview thread per persona, one outline refine pass, one
   lead pass, one polish pass unless a supplied extra polish remains in budget.
   Record which persona contributed which outline sections. Conflicts across
   personas stay visible rather than silently merged. Do not treat a polished
   draft as a published encyclopedia article or as permission to edit a live
   wiki.

Return INTERVIEW_COMPLETE per persona with turn counts, the input old_outline
and the refined outline, the lead, the polished draft, the citation map, and
gaps the interviews could not cover. Label unpublished draft status. Search
failures are gaps, not license to invent.
```

## How It Works

Stanford STORM's knowledge-curation signatures run a persona-guided asker against a search-backed expert until a stop utterance or max_turn, then outline generation and article polish. This adaptation replaces the magic thank-you line with INTERVIEW_COMPLETE, treats old_outline as an input rather than copying the upstream OutputField mis-annotation, and states that nothing is published to Wikipedia.

Unlike [Deep Research Supervisor (Brief-Delegate-Compress)](deep-research-supervisor.md), this is persona-interview curation with outline refine and duplicate polish, not a supervisor that delegates non-overlapping research units and reconciles child citations. Unlike [Agent Graph With Cycles](../system/agent-graph-cycle.md), nodes are interviewer/expert/outline/polish stages with a typed interview stop, not worker/reviewer veto cycles. Unlike [LLM Researcher](llm-researcher.md), the loop gathers multi-persona coverage before drafting rather than explaining a single supplied paper.

## Variables

- `[topic]`: subject of the survey and any hard exclusions.
- `[personas]`: named research focuses besides a generic writer identity.
- `[turn budget]`: max_turn per persona; default if unspecified is the supplied executor limit, otherwise 5.

## Tested On

Not model-tested. Curated adaptation; no Wikipedia-quality, citation-accuracy, or live STORM-run evaluation is claimed.
