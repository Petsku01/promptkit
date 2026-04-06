# LLM Integration Pattern

## Description

Structure prompts for multi-model or multi-step LLM workflows with explicit handoffs.

## When to use

Complex tasks requiring multiple LLM calls, model selection, or ensemble approaches.

## When to avoid

Simple single-LLM tasks where orchestration is unnecessary.

## Template

```
Phase 1: [First LLM task]
Output: [Intermediate result]

Phase 2: [Second LLM task using Phase 1 output]
Decision point: [Criteria for proceeding]

Phase 3: [Final LLM task or synthesis]
Output: [Final result]

Handoff rules:
- Phase N+1 uses Phase N output
- Each phase validates before next
- Failed phase: halt with error log
```

## Example

```
Phase 1: Analyze user sentiment from this feedback:
"The app crashes when I try to save."
Output: Sentiment: Negative, Frustration, Key phrases: ["crashes", "save"]

Phase 2: Generate response for negative sentiment with key phrases
Output: Draft response addressing crashes and offering solution

Phase 3: Review for empathy and solution alignment
Output: Final polished response

Handoff rules:
- Phase 2 uses Phase 1 sentiment analysis
- Phase 3 validates response quality
- Failed phase: log and halt
```

## Advanced

- **Parallel phases**: Run Phase 1 with 3 models, pick best Phase 2
- **Human gates**: Stop for human approval between phases
- **Self-correction**: Phase 3 reviews Phase 2, suggests Phase 2.5 if needed

## Tags

multi-model, orchestration, pipelines, handoffs
