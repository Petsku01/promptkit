# Retry with Backoff Pattern

## Description

Automatically retry failed requests with exponential backoff for transient errors.

## When to use

Network requests, API calls, or any operation that can fail temporarily.

## When to avoid

Non-idempotent operations where retry could cause side effects.

## Template

```
Retry this operation with exponential backoff:

Operation: [description]

Retry configuration:
- Max retries: [number]
- Base delay: [time]
- Max delay: [time]
- Jitter: [yes/no]

Retry on errors:
- 429: Rate limited
- 500: Server error
- 502: Bad gateway
- 503: Service unavailable
- 504: Gateway timeout

Do NOT retry:
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found

Success criteria: [what defines success]
```

## Example

```
Retry this LLM API call with exponential backoff:

Operation: POST /v1/chat/completions

Retry configuration:
- Max retries: 3
- Base delay: 1 second
- Max delay: 30 seconds
- Jitter: yes (add randomness)

Retry on errors:
- 429: Rate limited
- 500: Server error
- 502: Bad gateway
- 503: Service unavailable
- 504: Gateway timeout

Do NOT retry:
- 400: Bad request (client error)
- 401: Unauthorized (auth issue)
- 403: Forbidden (permission issue)
- 404: Not found (endpoint issue)

Success criteria: HTTP 200 with valid JSON response
```

## Tags

retry, backoff, resilience, error-handling
