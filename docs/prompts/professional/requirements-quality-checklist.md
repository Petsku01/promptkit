---
category: "professional"
title: "Requirements Quality Checklist"
source: "github/spec-kit"
license: "MIT"
---
[← Back to Professional Prompts](../index.md)

# Requirements Quality Checklist

**Category:** professional
**Source:** Adapted from https://github.com/github/spec-kit/blob/7370e592f3cd9c06e5b698983957e227c75b30e2/templates/commands/checklist.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Prepare a reviewer-owned checklist for clarity, completeness, consistency and measurability of written requirements. It evaluates the specification, not whether implemented software works, and needs no command framework or prerequisite scripts.

## The Prompt

```text
Create a requirements-quality checklist from the supplied documents.
Documents: [requirements text or readable paths and versions]
Focus and risk: [domain, important failure classes and exclusions]
Audience and rigor: [reviewer role and review depth]
Clarification mode: [none, or up to three questions]

1. Read the actual requirements and identify stable section/requirement anchors.
   If required documents are missing, report the missing inputs instead of
   inventing their contents. Record scope, document versions and exclusions.
2. Focus on the highest-risk relevant domains. If clarification is enabled, ask
   at most three impact-ranked questions about ambiguity that would materially
   change this checklist; do not ask what is already answered. If interaction is
   unavailable or disabled, list unresolved assumptions and proceed only with
   explicitly bounded criteria. Never silently decide product policy.
3. Generate concise, deduplicated questions about what is WRITTEN: completeness,
   clarity, consistency, measurable acceptance criteria, scenario and edge-case
   coverage, non-functional requirements, dependencies and assumptions. Include
   alternate, exception and recovery paths when relevant to the stated scope.
4. Each item must be unchecked and have a stable ID, quality dimension, priority,
   and a document section/requirement link. For absent requirements use [Gap] and
   identify the nearest relevant section or missing topic. For contradictions
   link both sections; quote ambiguous terms where useful. Do not invent anchors.
5. Make each criterion answerable by reviewing the document. For example:
   - [ ] CHK001 [Clarity] [High] Is the timeout duration and its applicable
     operation specified? [document section anchor or Gap: timeout policy]
   Do NOT substitute "test that the API returns 200" or "confirm the button works".
   Ask whether response contracts and interaction requirements are specified.
6. Group by quality dimension, not implementation task. Avoid irrelevant generic
   checklists, duplicate questions or arbitrary quotas. Separate explicit source
   requirements from suggested missing topics; do not promote suggestions into
   agreed requirements. Do not edit the specification or run implementation tests.

Return scope/documents, grouped checklist, unresolved questions and review notes.
All generated boxes remain [ ]. Checkbox state belongs to the reviewer: [x] means
that reviewer judged the requirements-quality criterion satisfied, NOT that code
is implemented or tested. Do not evaluate or mark boxes unless separately asked.
Output the checklist in the response; file writes require separate authorization.
No framework hooks, companion templates or prerequisite scripts are required.
```

## How It Works

Section-linked questions act as checks on requirements writing. Unchecked reviewer ownership prevents generated checklists from becoming false implementation-completion reports; bounded clarification exposes policy gaps rather than filling them silently.

## Variables

- `[requirements text or readable paths and versions]`: documents being reviewed.
- `[domain, important failure classes and exclusions]`: checklist scope and risk priorities.
- `[reviewer role and review depth]`: intended audience and rigor.
- `[none, or up to three questions]`: optional interaction limit; unanswered issues remain explicit.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
