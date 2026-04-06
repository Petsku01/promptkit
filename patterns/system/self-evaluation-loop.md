# Self-Evaluation Loop Pattern

## Description

Evaluate output quality with explicit criteria and rewrite if below threshold.

## When to use

Quality-critical outputs where bad output is worse than cost of rewriting.

## When to avoid

Speed-critical situations where evaluation overhead is prohibitive.

## Template

```
[Output content]

EVALUATION RUBRIC (1-5 scale):
1. [Criterion 1]: [Score] - [Reasoning]
2. [Criterion 2]: [Score] - [Reasoning]
3. [Criterion 3]: [Score] - [Reasoning]
4. [Criterion 4]: [Score] - [Reasoning]

DECISION:
If ANY score < 3: rewrite failing sections
If ALL scores >= 3: ACCEPT OUTPUT

Only rewrite twice. If still < 3 after rewrite: SKIP with warning.
```

## Example

```
Evaluate the following newsletter section:

"The new feature boosts productivity by 40% through AI-powered automation."

EVALUATION RUBRIC (1-5 scale):
1. Clarity: 4 - Clear and specific claim
2. Relevance: 3 - Somewhat relevant to AI
3. Specificity: 2 - "AI-powered" is vague
4. Sourceability: 1 - No source cited

DECISION:
Score 2.5 average. Rewrite with more specific claims and citations.

REWRITTEN:
"The new feature reduces manual data entry by 40% (source: internal analytics Q1 2025) through ML-based field extraction."

RE-EVALUATION RUBRIC:
1. Clarity: 4 - Clear and specific claim
2. Relevance: 4 - Core topic
3. Specificity: 4 - Specific technology named
4. Sourceability: 3 - Internal analytics cited

DECISION:
All scores >= 3. ACCEPT OUTPUT
```

## Tags

evaluation, quality-gate, rubric-based, iterative
