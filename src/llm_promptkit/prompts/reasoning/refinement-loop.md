---
category: "reasoning"
title: "Refinement Loop (Generate-Critique-Revise Until Threshold)"
source: "promptkit-authored"
---
# Refinement Loop (Generate-Critique-Revise Until Threshold)

**Category:** reasoning
**Source:** Grounded in Self-Refine (Madaan et al. 2023, arXiv:2303.17651) and OpenAI agentic/evaluation guidance; authored.

## When to Use

Improve a substantive draft against explicit acceptance criteria within a fixed budget. Use for analysis, specifications, explanations, and proposals with checkable quality dimensions—not endless cosmetic polishing.

## The Prompt

```text
Improve [draft/task] through a bounded generate-critique-revise loop. Evaluate
against [quality criteria], respecting [iterations budget]. Treat critique as
an evidence-based assessment of the artifact, not permission to invent facts.
Return concise findings and decisions, not a transcript of private reasoning.

1. Freeze the contract. Identify audience, required coverage, prohibited changes,
   factual sources, output format, and hard constraints. Convert each quality
   criterion into an observable check. If criteria are underspecified, use these
   declared defaults: factual correctness, requirement coverage, internal logical
   consistency, actionable specificity, and clarity. Mark safety, factual accuracy,
   and explicit user requirements as hard gates. Missing information that changes
   acceptance is a blocker, not an invitation to guess the user's intentions.

2. Set limits before generation. Use three revision attempts as an authored default,
   not an empirical convergence range; an explicit supplied limit takes precedence.
   Count a rejected revision against the limit. Also declare a total token or
   elapsed-time budget supplied by the environment; if none is available, cap
   generated review-and-revision material at 3000 words. Reserve enough capacity
   for one final answer. Never increase the budget silently because a draft feels
   nearly finished. The initial draft and its baseline review precede revisions.

3. Generate an initial candidate, or preserve the supplied draft as candidate zero.
   Save the incumbent artifact separately from proposed edits. Evaluate every
   dimension on a 0–4 scale: zero means absent or contradicted, one means major
   defects, two means partial satisfaction, three means satisfactory with minor
   gaps, and four means fully satisfied by available evidence. Record a concrete
   defect or supporting check for each score. Unknown factual claims cannot earn
   a passing correctness score merely because they sound plausible.

4. Apply the decision rule after every review. PASS requires every hard gate to
   pass and every dimension to score at least three; explicit stricter criteria
   override this default. If PASS, stop as converged immediately. Otherwise select
   the highest-impact unmet criterion. State the defect, affected passage, intended
   correction, and verification check. Distinguish an unsupported assumption from
   a demonstrated error. Do not spend a pass changing tone while correctness or
   required coverage remains deficient.

5. Revise only the selected defects and directly dependent passages. Preserve
   correct details, citations, constraints, and previously satisfied checks. Inspect
   correctness and factual support, coverage, consistency, actionability, and clarity
   on every pass, even when only one dimension drove the edit. Recheck examples,
   boundary cases, calculations using available tools, and exact requested formats.
   Never present an unexecuted tool check as observed evidence.

6. Enforce a regression guard before accepting the revision. Its score must be
   at least the incumbent's score on every dimension, with no newly introduced
   errors or failed hard gates. Require at least one demonstrated substantive
   improvement to replace the incumbent. If any dimension regresses, reject the
   candidate, retain the incumbent, and record the failed change. A higher average
   cannot compensate for losing a mandatory requirement. Self-ratings are fallible:
   prefer external checks or supplied references where available.

7. Continue only if an unmet criterion has a concrete, budget-feasible correction.
   Stop on PASS, exhausted attempts, exhausted resource budget, an unresolvable
   evidence gap, or two attempts without accepted substantive improvement. A mere
   paraphrase is not progress. Never restart the loop under a new label, broaden
   scope to create more work, or alternate stylistic preferences indefinitely.

Deliver the best retained artifact, followed by a short status: CONVERGED,
BUDGET EXHAUSTED, STALLED, or BLOCKED. Include attempts consumed, the final
criterion verdicts, and a residual list of unresolved defects or uncertainties.
Budget exhaustion is not a pass. If there are no residual defects, say so; do
not invent problems to justify another cycle or claim guaranteed perfection.
```

## How It Works

Unlike the short reflection pattern or existing Self-Refinement prompt, this workflow defines a threshold, keeps an incumbent, rejects regressions, and bounds both attempts and resources. Unlike ReAct, the unit of progress is an evaluated artifact revision rather than a tool action; unlike prompt chaining, it revisits the same acceptance contract.

[Self-Refine (Madaan et al., 2023)](https://arxiv.org/abs/2303.17651) describes generating an initial output, giving feedback, and iteratively refining it; that is the methodological basis of this loop. [OpenAI's agentic guidance](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) grounds incremental changes and verification, while [evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) supports explicit criteria, comparisons, and pass/fail thresholds. Numeric defaults and regression rules are authored operational choices, not vendor guarantees or measured self-refinement results.

## Related 2026-era extensions

2026-11-02: [Persistent Skill Evolution Loop](../system/persistent-skill-evolution.md) adds evidence-gated knowledge consolidation and skill promotion across sessions, rather than revising the current draft. [RRSI (2026)](https://arxiv.org/abs/2609.24972) motivates leakage screening for reusable changes; apply the same precaution to critique signals so benchmark-specific answers or scoring shortcuts cannot become apparent improvement evidence.

## Variables

- `[draft/task]`: existing artifact or task to draft, including audience and constraints.
- `[quality criteria]`: observable acceptance checks, hard gates, and any stricter thresholds.
- `[iterations budget]`: maximum revisions plus any token or time cap; defaults are declared in the prompt.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
