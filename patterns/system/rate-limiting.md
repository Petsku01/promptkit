# Rate Limiting Pattern

## Description

Control request rates to prevent abuse and ensure fair resource allocation.

## When to use

Public APIs, resource-constrained systems, or when preventing abuse.

## When to avoid

Internal systems with trusted users where latency matters more.

## Template

```
Apply rate limiting to these requests:

Scope: [per-user / per-IP / global / per-endpoint]

Limits:
- Burst: [max requests in short window]
- Sustained: [requests per longer window]

Window: [time window, e.g., 1 minute, 1 hour]

Algorithm: [token-bucket / sliding-window / fixed-window]

When limit exceeded:
- Response code: [429 or 503]
- Headers: [Retry-After, X-RateLimit-*]
- Message: [user-friendly error]

Exceptions: [whitelisted users, internal services]
```

## Example

```
Apply rate limiting to API requests:

Scope: Per-user (authenticated) / Per-IP (anonymous)

Limits:
- Authenticated: 100 requests per minute
- Anonymous: 10 requests per minute

Window: 60 seconds

Algorithm: Token bucket

When limit exceeded:
- Response code: 429 Too Many Requests
- Headers:
  - Retry-After: 60
  - X-RateLimit-Limit: 100
  - X-RateLimit-Remaining: 0
  - X-RateLimit-Reset: [timestamp]
- Message: "Rate limit exceeded. Please try again in 60 seconds."

Exceptions: Internal services (bypass rate limiting)
```

## Tags

rate-limiting, throttling, protection, fair-use
