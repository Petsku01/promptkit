---
category: "model-optimized"
title: "GLM-5.3: Reasoning"
subcategory: "zhipu"
model: "glm-5.3"
source: "promptkit-authored"
---
# GLM-5.3: Reasoning

## Side-Effect-Aware Tool Plan
```
Choose a tool sequence that achieves [objective] with minimal operational risk.
Available function schemas: [schemas]
Current verified state: [observations]
Authorization boundary: [permitted actions]
Success condition: [condition]

Separate independent reads from dependent writes. For every mutation, identify prerequisites, exact target, idempotency or retry behavior, and the read-back that will establish success. If a required argument is unknown, retrieve it rather than guessing. Pause before actions outside the stated authorization boundary.

Return a compact executable plan with precondition, call, expected evidence, and failure branch columns. If execution is authorized and tools exist, perform the plan and replace expected evidence with observed evidence in the final report.
```

## Acceptance-Criteria Consistency Proof
```
Determine whether this engineering task's acceptance criteria can all hold simultaneously.
Requirements: [numbered criteria]
System invariants: [invariants]
Relevant implementation facts: [text or tool-verified references]

Check the criteria against invariants and against each other. Seek a concrete counterexample to a proposed satisfying design. Use bounded executable checks where possible, while distinguishing finite testing from a general proof. If requirements conflict, isolate the smallest demonstrable conflict rather than discarding a difficult criterion silently.

Return feasible / infeasible / unresolved, a concise supporting argument, and either a witness design or the conflicting criterion IDs. Include the next clarification or verification needed.
```
