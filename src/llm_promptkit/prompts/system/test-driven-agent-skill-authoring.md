---
category: "system"
title: "Test-Driven Agent Skill Authoring"
source: "obra/superpowers"
license: "MIT"
---
# Test-Driven Agent Skill Authoring

**Category:** system
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/SKILL.md (MIT)

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).

## When to Use

Create or revise a reusable agent skill when observable failures suggest that instructions could help. Requires a real model runner with fresh-context execution and a fixed scoring rubric; writing a plausible skill is not behavioral validation.

## The Prompt

```text
Author the smallest reusable skill that improves this observed behavior.
Desired behavior and trigger: [behavior and when the skill should activate]
Pressure scenarios and rubric: [tasks, observable failures, scoring criteria]
Runner: [available API or subagent runner, model/configuration, tool permissions]
Draft location: [authorized reversible draft path and existing version]
Budget: [maximum calls/tokens/cost/time and maximum revision cycles]

Keep this experiment self-contained: no companion skill or harness-specific
announcement is required. Do not install, publish, commit or push anything.

RED — establish the failure before drafting:
1. Freeze task inputs, rubric, realistic surrounding instructions, model settings
   and tool permissions. Include an ordinary task, an edge/missing-input task,
   and a pressure case. For discipline rules combine relevant pressures such as
   urgency, sunk cost and apparent authority without granting unsafe permissions.
2. Execute a no-skill baseline in fresh contexts. Preserve actual prompts,
   responses, tool traces, runner exit/status and exact failure/rationalization
   excerpts. A baseline that follows the desired behavior does not demonstrate a
   need for this skill; report that result instead of inventing a failure.
3. Keep a no-guidance control throughout comparisons. Use at least five fresh
   samples per wording variant for behavior-shaping micro-tests when the budget
   permits. If the budget cannot support that, disclose the smaller sample and
   do not claim robust improvement. Never silently exceed the budget.

GREEN — write and test a minimal draft:
4. Classify the baseline failure. For rule violations use explicit boundaries
   and counters to observed rationalizations. For wrong-shaped output give a
   positive ordered output recipe. For omissions provide a required field. For
   conditional behavior use an observable if/then trigger. Do not add speculative
   prohibitions or loophole-filled exceptions to every kind of failure.
5. Draft a portable skill: searchable name, concise activation-only description,
   core principle, actionable steps, necessary boundaries, output contract and
   one useful example if evidence warrants it. Follow the target runtime's
   actual skill schema and length limits, not an assumed global directory.
   Keep essential methodology inline; do not depend on unavailable references.
6. Re-run the frozen scenarios WITH the skill, using fresh contexts and the same
   model/settings/tools as the no-guidance control. Do not leak earlier answers
   into retests. Score against the unchanged rubric and manually inspect every
   automatically flagged match: quotations and template echoes are not behavior.

REFACTOR — retest without chasing a predetermined result:
7. Make narrow revisions tied to observed failures. Preserve versioned drafts
   and previous results. If a draft predates baseline evidence, quarantine it as
   an unvalidated draft; do not delete existing work. Retest changed wording,
   the original failure and a held-out pressure/variation case. Micro-tests do
   not replace full application/pressure scenarios. Report variance, regressions
   and control outcomes, not just a single favorable completion.
8. Stop at the budget or revision limit. If execution is unavailable, deliver
   only a clearly UNVALIDATED draft and the blocked experiment specification.
   Do not synthesize runs, claim universal compliance or auto-deploy a winner.

Deliver the minimal draft plus an evidence table:
scenario/sample ID | draft/control version | model/settings | observed behavior
and trace | rubric result | runner status | residual uncertainty.
Include baseline failures, control results, retests, held-out results, actual
budget used, changes justified by evidence, and validated/unvalidated status.
```

## How It Works

RED–GREEN–REFACTOR tests instructions as interventions rather than prose. Matched fresh-context controls and repeated samples separate observed improvement from baseline compliance or sampling noise. Reversible drafts and bounded iterations replace destructive cleanup and automatic publication.

## Variables

- `[behavior and when the skill should activate]`: reusable target, not a one-off project narrative.
- `[tasks, observable failures, scoring criteria]`: frozen behavioral acceptance criteria.
- `[available API or subagent runner, model/configuration, tool permissions]`: executable experimental environment.
- `[authorized reversible draft path and existing version]`: safe destination and revision history.
- `[maximum calls/tokens/cost/time and maximum revision cycles]`: hard experimental limits.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
