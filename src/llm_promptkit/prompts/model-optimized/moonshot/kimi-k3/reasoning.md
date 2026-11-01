---
category: "model-optimized"
title: "Kimi K3: Reasoning"
subcategory: "moonshot"
model: "kimi-k3"
source: "promptkit-authored"
---
# Kimi K3: Reasoning

## Cross-Document Constraint Resolution
```
Resolve this planning problem using the complete supplied record.
Goal: [goal]
Contracts, requirements, and historical decisions: [ID-labeled materials]
Hard constraints: [constraints]

Identify which requirements remain authoritative and which were replaced. Test the proposed solution against the interactions between constraints across documents. If the requirements are inconsistent, provide a minimal conflicting set and the smallest policy change that would restore feasibility.

Return the recommended plan, a compact justification with source IDs, and a constraint coverage table. Provide decision-relevant reasoning summaries rather than a transcript of private deliberation.
```

## Tool-Grounded Research Decision
```
Investigate whether [hypothesis] is sufficient to justify [action].
Available tools and budget: [tools and limits]
Starting evidence: [sources]
Stopping rule: [evidence threshold or deadline]

Seek the observation most likely to falsify the hypothesis before expanding the search. Use tool results to update an explicit evidence ledger, preserving provenance across the investigation. Distinguish absence of evidence from an unsuccessful retrieval. Do not continue searching once the stopping rule is met.

Conclude with support / reject / insufficient evidence, a brief rationale, the strongest counterexample, and the next discriminating experiment.
```
