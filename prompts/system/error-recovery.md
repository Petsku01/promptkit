# Error Recovery Protocol

**Use case:** Defining how agents handle failures

**Pattern:** Error Recovery Instructions

---

## Quick Version (~120 tokens)

```
ERROR HANDLING:

RECOVERABLE (auto-fix):
- Rate limit: wait 60s, retry 3x
- Timeout: skip, log, continue
- Parse error: log raw output, skip

UNRECOVERABLE (halt):
- Auth failure
- Permission denied  
- Cost would exceed limit

On halt: write ERROR.txt with details.
```

---

## Extended Version (~450 tokens)

```
ERROR HANDLING PROTOCOL:

Classify every error immediately as RECOVERABLE or UNRECOVERABLE. Never guess.

RECOVERABLE ERRORS (handle automatically):

HTTP 429 (Rate Limited):
Action: Wait 60 seconds. Retry up to 3 times with exponential backoff.
If still failing: Log "rate_limited: [service]" and skip this operation.
Continue with remaining tasks.

HTTP 503 (Service Unavailable):
Action: Wait 30 seconds. Retry once.
If still failing: Mark service as unavailable for this run. Continue.

Timeout:
Action: Log "timeout: [operation] after [duration]". Skip and continue.
Do not retry timeouts immediately - may indicate infinite loop.

Parse Error (invalid JSON/XML from tool):
Action: Log raw output to /errors/parse-fail-[timestamp].log.
Skip this item and continue.

File Not Found:
Action: Verify path is correct. If path is valid, log "missing: [path]".
Continue with available resources.

UNRECOVERABLE ERRORS (halt immediately):

Authentication Failure:
- Missing or invalid API credentials
- Token expired
- Permission denied (403)
Action: Write to HALT.txt, stop all operations.

Resource Exhaustion:
- Disk full
- Out of memory
- Would exceed $0.50 cost limit
Action: Write to HALT.txt, preserve partial state.

Safety Violation:
- Attempted operation outside allowed directory
- PII detected in unauthorized context
- Attempted external communication not on allowlist
Action: Write to HALT.txt, do not retry.

HALT.txt FORMAT:

```
TIMESTAMP: 2026-01-15T10:30:00Z
ERROR_TYPE: [unrecoverable category]
ERROR_MESSAGE: [exact error]
LAST_ACTION: [what you were attempting]
CONTEXT: [relevant task context]
```

After writing HALT.txt, stop. Do not continue.
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** error, recovery, safety, resilience
- **Models:** All
- **Version:** 1.0
