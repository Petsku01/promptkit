---
category: "model-optimized"
title: "Claude Opus 4.8: Reasoning"
subcategory: "anthropic"
model: "claude-opus-4.8"
source: "promptkit-authored"
---
[← Back to Model-Optimized Anthropic](../index.md)

# Claude Opus 4.8: Reasoning

## Durable Decision Record
```
Resolve [multi-stage decision] using the supplied project history.

History and earlier decisions: [dated records with IDs]
Current objectives: [objectives]
Non-negotiable constraints: [constraints]
Changed facts since the previous decision: [facts and evidence]
Decision-record limit: [word count]

Reconstruct only the decisions relevant to the current choice. Identify which
assumptions remain valid, which were superseded, and which are merely repeated
without evidence. Apply the stated constraints to every option, including the
status quo. Do not treat an earlier recommendation as a binding instruction.

Produce a durable record containing: decision, alternatives rejected with brief
reasons, supporting evidence IDs, unresolved dependencies, and explicit triggers
for reopening the decision. Include a short handoff listing verified facts,
open questions, and next authorized action so later work need not rediscover
the history. Keep this handoff factual rather than a private reasoning trace.
```

## Specification Ambiguity Resolution
```
Determine whether [proposed solution] satisfies [specification].

Specification: [numbered clauses]
Proposed solution: [design, algorithm, or plan]
Examples and counterexamples: [supplied cases]
Interpretation authority: [explicit precedence, or none]

Check each clause literally before making charitable assumptions. For every
material ambiguity, state the competing readings and a concrete case where
they produce different outcomes. Do not silently extend a requirement from one
item to another; flag scope that must be clarified.

Return a clause-by-clause compliance table with evidence or a counterexample.
For unsatisfied clauses, propose the smallest repair and recheck its effects
on the other clauses. If the outcome depends on an unresolved reading, provide
a conditional verdict and the exact clarification needed. Present concise,
checkable reasoning rather than exhaustive deliberation.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
