---
category: "model-optimized"
title: "GPT-6.1 Sol: Reasoning"
subcategory: "openai"
model: "gpt-6.1-sol"
source: "promptkit-authored"
---
# GPT-6.1 Sol: Reasoning

## Constraint-Sensitive Planning
```
Find a feasible plan for [objective].

Hard constraints: [conditions that must never be violated]
Preferences: [ranked soft goals]
Resources and dependencies: [capacities, dates, and prerequisite relationships]
Permitted computational tools: [available solver or code execution tool]
Decision artifact: [schedule, allocation, or ordered plan]

Translate the inputs into explicit variables and constraints. Resolve conflicting
units or definitions before optimization; mark missing values as assumptions.
Use an available solver or executable enumeration when the search space merits
it. Validate the resulting plan against every hard constraint independently of
the optimization objective. If there is no feasible plan, identify a conflicting
subset and the smallest proposed relaxation; never relax a constraint silently.

Return the plan, objective value if verified, a constraint-check table, and the
assumptions that could change feasibility. Give a concise justification with
checkable equations or witnesses, not a transcript of private deliberation.
```

## Counterfactual Decision Stress Test
```
Stress-test the proposed decision [decision] against [risk or uncertainty].

Available evidence: [documents, images, and measurements]
Baseline assumptions: [assumptions]
Alternatives: [options, including doing nothing]
Loss criteria: [costs, safety limits, and failure conditions]

Identify the smallest change in assumptions that would reverse the ranking of
the alternatives. Separate causal claims from correlations in the evidence.
Construct one plausible adverse scenario and one favorable scenario without
assigning unsupported probabilities. Use a supplied calculation tool for
sensitivity thresholds; otherwise provide formulas and label them unevaluated.

Return a compact comparison, reversal thresholds, a recommendation conditional
on the evidence, and the one observation worth collecting next. Explain only
the decisive reasoning and validation checks. Do not manufacture certainty
because additional reasoning effort was allocated by the caller.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
