# Circuit Breaker Pattern

## Description

Prevent cascading failures by temporarily blocking requests to failing services.

## When to use

Microservices, external APIs, or any service that can become overwhelmed.

## When to avoid

Simple synchronous calls where failure isolation isn't critical.

## Template

```
Implement circuit breaker for this service:

Service: [name/endpoint]

Circuit states:
- CLOSED: Normal operation, requests pass through
- OPEN: Service unhealthy, requests blocked
- HALF-OPEN: Testing if service recovered

Thresholds:
- Failure rate: [percentage] over [time window]
- Consecutive failures: [number]
- Slow responses: [percentage] slower than [threshold]

Timeouts:
- Open duration: [time before testing]
- Half-open requests: [number of test requests]

Success criteria for closing:
- [N] consecutive successful test requests

Fallback when open: [what to do when circuit is open]
```

## Example

```
Implement circuit breaker for LLM API:

Service: https://api.openai.com/v1/chat/completions

Circuit states:
- CLOSED: Normal operation, requests pass through
- OPEN: Service unhealthy, requests blocked
- HALF-OPEN: Testing if service recovered

Thresholds:
- Failure rate: 50% over 30 seconds
- Consecutive failures: 5
- Slow responses: 80% slower than 5 seconds

Timeouts:
- Open duration: 30 seconds before testing
- Half-open requests: 3 test requests

Success criteria for closing:
- 3 consecutive successful test requests

Fallback when open: Queue request for later, return cached response, or use fallback provider
```

## Tags

circuit-breaker, resilience, microservices, reliability
