---
category: "model-optimized"
title: "Gemini 3.8 Flash: Reasoning"
subcategory: "google"
model: "gemini-3.8-flash"
source: "promptkit-authored"
---
[← Back to Model-Optimized Google](../index.md)

# Gemini 3.8 Flash: Reasoning

## Multimodal Constraint Inference
```
Determine whether [proposed physical or operational arrangement] is feasible.

Visual evidence: [diagrams, photos, or video]
Written requirements: [dimensions, capacities, and safety constraints]
Known scale references: [measurements, or none]
Permitted tools: [code execution or calculator, if available]

Extract stated constraints separately from visually inferred constraints.
Reference image regions or video timestamps for observations. Do not estimate
exact dimensions from perspective alone when no scale is supplied. Represent
uncertain measurements as ranges and preserve their units.

Construct a feasibility check using only justified inputs. If computation is
available, evaluate boundary cases, not just a nominal estimate. Identify which
conclusion depends on an unmeasured quantity and the smallest measurement that
would resolve it.

Return a conditional feasibility verdict, a constraint table, verified
calculations or unevaluated formulas, and a practical validation step. Do not
claim that a diagram proves real-world safety.
```

## Tool-Orchestration Plan with Stop Conditions
```
Design an executable workflow for [enterprise task].

Inputs and outputs: [data types and acceptance checks]
Available functions: [names, schemas, costs, and side effects]
Failure modes: [known errors and unreliable services]
Resource limits: [call budget, time limit, and retry limits]
Authorization boundary: [actions requiring human approval]

Map dependencies between functions, preserving which outputs provide evidence
for later steps. Parallelize only independent read operations. For each step,
specify a success condition, an idempotency strategy if needed, and a bounded
retry or fallback. Do not propose calls to tools absent from the supplied list.

Walk the workflow through one success case and two specified failure cases
[failures]. Identify how stale or partial results are detected. Return a compact
state-transition table and a completion checklist. A plan is not an execution
record: do not report external actions as completed unless actually performed.
```
