# Error Recovery Protocol Pattern

## Description

Define recoverable vs. unrecoverable errors and explicit actions for each.

## When to use

Every agent with tool access that runs autonomously.

## When to avoid

Interactive agents where human can handle errors in real-time.

## Template

```
Error handling protocol:

RECOVERABLE (handle automatically):
- [Error type 1]: [Action to take]
- [Error type 2]: [Action to take]
- [Error type 3]: [Action to take]

UNRECOVERABLE (stop immediately, notify):
- [Critical error 1]: [Stop action]
- [Critical error 2]: [Stop action]

When stopping, write to [LOG FILE]:
- timestamp
- exact error
- last action attempted
- what you were trying to accomplish
```

## Example

```
Error handling protocol:

RECOVERABLE (handle automatically):
- HTTP 429/503: wait 60s, retry up to 3 times, then skip
- File not found: log path and continue
- JSON parse error: log raw output to errors.log, skip item

UNRECOVERABLE (stop immediately, write to HALT.txt):
- Missing API credentials
- Output directory not writable
- >3 sources failing simultaneously

When stopping, write to HALT.txt:
- timestamp
- exact error
- last action attempted
- what you were trying to accomplish
```

## Tags

error-handling, recovery, resilience, reliability
