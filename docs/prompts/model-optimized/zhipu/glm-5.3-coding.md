---
category: "model-optimized"
title: "GLM-5.3: Coding"
subcategory: "zhipu"
model: "glm-5.3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Zhipu](../index.md)

# GLM-5.3: Coding

## End-to-End Engineering Ownership
```
Complete this engineering assignment in the provided tool environment.
Assignment: [task]
Repository: [path]
Write scope and prohibited operations: [limits]
Acceptance checklist: [items]

Inspect project conventions and executable checks before editing. Use function calls with arguments grounded in inspected schemas and real paths. Decompose the task into verifiable units, implement them, and exercise the complete user-facing path. After a tool error, diagnose its cause before retrying; do not drift into a different objective just to obtain a passing result.

Report the final artifact, checklist evidence, actual test outcomes, and unresolved work. Stop at permission boundaries; a long-horizon assignment is not authorization for unrelated changes.
```

## Measured Infrastructure Optimization
```
Improve [training, storage, or service bottleneck] without changing required behavior.
Codebase and environment: [details]
Benchmark command and workload: [specification]
Correctness oracle: [tests or reference]
Permitted compute and duration: [budget]

Measure a baseline and identify the bottleneck with available profiling tools. Change one justified factor at a time. Re-run both the correctness oracle and the same benchmark workload, recording hardware and configuration differences. Reject speedups that skip required work or alter the metric definition.

Deliver the patch, baseline and changed measurements, correctness results, and rollback steps. If measurements are too noisy, report an inconclusive result rather than an unearned speedup claim.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
