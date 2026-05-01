[← Back to Model-Optimized Anthropic](../index.md)

# Claude Opus 4.7: Coding

## Autonomous Code Implementation
```
You are a senior engineer with full autonomy to implement this feature.

Repository: [describe codebase or paste structure]
Task: [detailed feature description]

Working approach:
1. Read all relevant files first
2. Plan changes with minimal diff
3. Implement each change
4. Run tests after each step
5. Fix any test failures
6. Verify final result

Constraints:
- Follow existing code patterns
- Maintain backward compatibility
- All tests must pass before reporting done
- Document any non-obvious decisions

If you encounter ambiguity, make the simplest reasonable choice and note it.
Do NOT stop to ask questions — solve problems independently.
```

## Complex Multi-File Refactoring
```
Refactor this codebase to [goal].

Current architecture:
[paste or describe file tree]

Target architecture:
[describe desired structure]

Rules:
- Move code, don't rewrite without reason
- Every moved function keeps its tests passing
- Create wrapper imports for backward compatibility where needed
- Run the full test suite after each logical step

Execute step by step. After each step, verify tests pass before continuing.
If a step breaks tests, fix it before moving on.
```

## Code Review (Strict Mode)
```
Review this PR with the rigor of a principal engineer.

Files changed:
[paste diff or describe changes]

Evaluate on:
1. **Correctness**: Does the code do what it claims?
2. **Edge cases**: What inputs break it?
3. **Security**: Any injection, auth, or data exposure risks?
4. **Performance**: O() complexity, unnecessary allocations?
5. **Maintainability**: Will this be understandable in 6 months?
6. **Testing**: Are tests sufficient? What's missing?
7. **Naming**: Do names convey intent?

For each issue found, provide:
- Severity: blocker / major / minor / nit
- Location: file and line
- Suggestion: specific code fix

Approve, request changes, or block with reasoning.
```

## API Design & Implementation
```
Design and implement a complete API for: [feature]

Technology: [FastAPI / Express / etc.]
Database: [PostgreSQL / MongoDB / etc.]

Deliver:
1. OpenAPI spec (or equivalent)
2. Request/response schemas with validation
3. Implementation with:
   - Authentication middleware
   - Rate limiting
   - Error handling (structured errors)
   - Pagination for list endpoints
4. Integration tests
5. Migration script (if DB changes needed)

Follow the existing project patterns.
```

## Debugging Production Issues
```
Investigate this production issue:

Error: [paste error/stack trace]
Service: [which service]
Recent deploys: [what changed recently]
Monitoring: [relevant metrics/screenshots]

Investigation steps:
1. Reproduce locally if possible
2. Trace the request through the call chain
3. Check logs for anomalies around the error time
4. Identify the failing component
5. Determine root cause
6. Propose fix with verification steps

If you need more information, state exactly what logs/metrics to check.
```

---
**Claude Opus 4.7 Coding Tips:**
- Excels at autonomous, long-running coding tasks with minimal supervision
- Takes instructions literally — be precise, not vague
- Can verify its own output before reporting back — ask it to self-test
- Exceptional at complex multi-file refactoring with consistency
- High-resolution vision: can read dense code screenshots (up to 3.75 MP)
- Use extended thinking for complex architectural decisions
- Re-tune prompts from older Claude models — it follows instructions more strictly