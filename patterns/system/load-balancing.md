# Load Balancing Pattern

## Description

Distribute requests across multiple instances to optimize resource use and prevent overload.

## When to use

Multiple service instances, varying capacity, or need to scale horizontally.

## When to avoid

Single instance systems or when request affinity matters.

## Template

```
Distribute load for this service:

Service: [name]

Instances:
- Instance 1: [capacity/weight]
- Instance 2: [capacity/weight]
- Instance 3: [capacity/weight]

Strategy: [round-robin / least-connections / weighted / consistent-hash]

Health checks:
- Interval: [time]
- Timeout: [time]
- Threshold: [failures before marking unhealthy]

Session affinity: [yes/no, stickiness method]

Circuit breaker integration: [yes/no]
```

## Example

```
Distribute load for LLM service:

Service: API Gateway

Instances:
- Instance 1: Weight 3 (high capacity)
- Instance 2: Weight 2 (medium capacity)
- Instance 3: Weight 1 (low capacity)

Strategy: Weighted round-robin

Health checks:
- Interval: 30 seconds
- Timeout: 5 seconds
- Threshold: 3 failures before marking unhealthy

Session affinity: No (stateless requests)

Circuit breaker integration: Yes (per instance)
```

## Tags

load-balancing, scaling, distribution, performance
