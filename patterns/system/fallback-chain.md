# Fallback Chain Pattern

## Description

Automatically switch to alternative providers or methods when primary option fails.

## When to use

Critical operations where availability matters more than using specific provider.

## When to avoid

When provider choice matters (cost, features, compliance requirements).

## Template

```
Use fallback chain for this operation:

Primary: [First option]
Fallback 1: [Second option]
Fallback 2: [Third option]
Fallback 3: [Last resort option]

Trigger fallback when:
- Primary fails after [N] retries
- Response time exceeds [threshold]
- Quality score below [threshold]

Selection criteria for fallback:
- [Criterion 1]
- [Criterion 2]

Circuit breaker: Open circuit to failed provider for [duration] after [threshold] failures.
```

## Example

```
Use fallback chain for LLM completions:

Primary: OpenAI GPT-4
Fallback 1: Anthropic Claude
Fallback 2: Google Gemini
Fallback 3: Local model (fallback)

Trigger fallback when:
- Primary fails after 3 retries
- Response time exceeds 10 seconds
- Error rate exceeds 5%

Selection criteria for fallback:
- Latency: < 2 seconds
- Quality: Passes evaluation checks
- Cost: Within budget threshold

Circuit breaker: Open circuit to failed provider for 60 seconds after 10 consecutive failures.
```

## Tags

fallback, availability, providers, redundancy
