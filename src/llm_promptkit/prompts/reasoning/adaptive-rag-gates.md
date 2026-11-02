---
category: "reasoning"
title: "Adaptive RAG Route-Grade-Generate Gates"
license: "MIT"
---
# Adaptive RAG Route-Grade-Generate Gates

**Category:** reasoning
**Source:** Adapted from https://github.com/langchain-ai/langgraph/blob/23961cff61a42b52525f3b20b4094d8d2fba1744/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb (MIT, LangChain)

Copyright (c) 2024 LangChain, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). Generation instructions in this file are authored; LangSmith Hub answer templates are not copied. Tutorial demo questions and model names are excluded.

## When to Use

Answer mixed-domain questions when some queries belong in a declared corpus and others need web fallback, and when unsupported or unhelpful generations must retry under caps rather than ship.

## The Prompt

```text
Control retrieval-augmented answering for [question] over [corpus] with
optional [web search] under [retry budgets]. Binary graders are fallible
labels, not verified truth. Without retrieval tools, return a labeled
specification. Do not use tutorial demo questions or vendor model names.

Controller (route, grade, generate, gate, retry, escalate):

1. Route the query. Choose corpus_retrieve when [question] falls inside the
   declared coverage of [corpus] (topics, collections, date range, and
   exclusions supplied by the caller). Choose web_search when the question
   is outside that coverage or the corpus is empty. Record the route, the
   coverage rule used, and uncertainty. Do not route by guessing hidden
   tutorial topics.

2. Retrieve, then grade relevance per document. A document is relevant if it
   contains keywords or semantic meaning related to the question; the test
   is a filter for erroneous hits, not a proof of sufficiency. Keep relevant
   documents with locators. If none remain after grading, rewrite the query
   once for the same source, or fall back to web_search when that branch is
   authorized (corrective fallback). Do not loop rewrites without counting.

3. Generate an answer only from the kept documents and their locators. If
   the documents do not contain the answer, say so. Prefer short attributed
   statements over unsourced fluency. Attach citation ids to claims that
   came from retrieved text. Do not pad with three-sentence theater.

4. Gate support (plain wording: is the generation supported by the retrieved
   facts?). This is not a "hallucination yes/no" field. supported=yes means
   each substantial claim is backed by kept documents. supported=no means
   regenerate from the same documents or, if regeneration budget remains,
   stop and escalate. A useful-but-unsupported answer fails this gate.

5. Gate usefulness: does the generation resolve the user's question? useful
   =yes means the asked decision or fact is answered, including an honest
   "not in sources". useful=no with supported=yes triggers a retrieval
   rewrite (different query, same or fallback source). useful=no with
   supported=no counts against regeneration. Invalid grader output (not
   yes/no) is treated as a failed grade and consumes one retry.

6. Bound retries separately. Retrieval-rewrite cap and regeneration cap are
   independent, plus a total tool-call budget in [retry budgets]. Defaults
   if unspecified: 2 rewrites, 2 regenerations, 8 tool calls. Repeated
   identical queries are forbidden; treat a duplicate query as no-progress
   and stop that branch. Never reset counters. Exhaustion yields ESCALATE
   with the best supported partial answer or ABSTAIN if none is supported.

7. Escalate-out is terminal: return ABSTAIN or the last supported draft,
   the route history, kept document ids, grade ledger, retry consumption,
   and why the controller stopped. Do not present an unsupported draft as
   a finished answer.

State to maintain: question, query history, route, kept documents, current
generation, support grade, usefulness grade, rewrite_count, regenerate_count,
tool_count, status. Cite sources in the user-visible answer when status is
ANSWERED.

Return ANSWERED, ABSTAIN, ESCALATE, or SPECIFICATION-ONLY with the ledger
above. Missing corpus coverage rules block routing rather than defaulting
to web search unless [web search] is explicitly authorized as the default.
```

## How It Works

The LangGraph adaptive RAG tutorial routes a question to a vectorstore or web search, grades retrieval relevance, generates, then grades whether the answer is supported by facts and whether it resolves the question, with rewrite/regenerate edges. This authored controller parameterizes [corpus], uses "supported by retrieved facts" instead of the tutorial's inverted hallucination label, adds separate rewrite/regenerate caps and escalate-out, and does not paste Hub generation text or notebook demo calls. Corrective web fallback (from the CRAG-style branch) is the no-relevant-document path, not a second catalog file.

Unlike Command R RAG personas, this is a gated controller with explicit retry accounting. Unlike [Hallucination Reducer](../defensive/hallucination-reducer.md), support and usefulness are separate gates that drive different retries. Unlike [Agent Graph With Cycles](../system/agent-graph-cycle.md), nodes are route/retrieve/grade/generate gates, not worker/reviewer roles. Binary grades remain model labels.

## Variables

- `[question]`: user question and required answer language/format.
- `[corpus]`: coverage topics, collections, date range, exclusions, and retriever handle.
- `[web search]`: whether fallback search is authorized, and its cap.
- `[retry budgets]`: rewrite cap, regeneration cap, total tool calls; defaults 2 / 2 / 8.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
