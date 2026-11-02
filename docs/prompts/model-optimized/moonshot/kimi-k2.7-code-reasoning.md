---
category: "model-optimized"
title: "Kimi K2.7 Code: Reasoning"
subcategory: "moonshot"
model: "kimi-k2.7-code"
source: "promptkit-authored"
---
[← Back to Model-Optimized Moonshot](../index.md)

# Kimi K2.7 Code: Reasoning

## Behavioral Compatibility Contract
```
Determine how to recreate the observable behavior of [program or interface].
Specification: [documentation]
Reference executable or sandbox endpoint: [authorized access]
Forbidden methods: [for example, decompilation or network access]

Develop a behavioral contract from the documentation and permitted black-box observations. Prioritize boundary inputs, error messages, ordering, and serialization details. Use differential tests against the reference where tools permit. Separate documented requirements from behavior observed only on particular examples.

Deliver the contract, a compact discriminating test matrix, and unresolved ambiguities. Do not claim equivalence beyond the tested input domain.
```

## Engineering Experiment Selection
```
Choose the next experiment for this unresolved performance problem.
Current implementation: [files or excerpts]
Measurements already collected: [results with environment]
Candidate causes: [hypotheses]
Experiment budget: [time and compute]

Use the existing investigation state to avoid repeating inconclusive work. Rank experiments by ability to separate the candidate causes, cost, and reversibility. Specify a correctness control for every proposed speedup. Execute only experiments authorized by the supplied tool scope.

Return the chosen experiment, expected observations under each hypothesis, measured results if executed, and a go/no-go criterion for the patch. Keep the rationale short and engineering-focused.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
