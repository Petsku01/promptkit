# GPT-5.4: Coding

## Agentic Code Implementation
```
You are implementing a feature in an existing codebase.

Repository context:
- Language: [Python/TypeScript/etc]
- Framework: [Django/Next.js/etc]
- Test runner: [pytest/jest/etc]

Task: [describe the feature]

Working files:
- [file1]: [brief description]
- [file2]: [brief description]

Constraints:
- Follow existing patterns in the codebase
- Maintain backward compatibility
- Add tests for new code
- Update relevant documentation

Implement the feature, then verify with tests.
```

## Multi-File Refactoring
```
Refactor the following module structure:

Current structure:
[paste file tree or describe]

Problems:
- [problem 1]
- [problem 2]

Goals:
- [goal 1]
- [goal 2]

Constraints:
- No breaking API changes
- All existing tests must pass
- Minimize diff size

Produce a plan first, then implement each step.
Run tests after each step.
```

## Architecture Review
```
Review this system architecture for a [type] application:

Architecture:
[paste or describe: components, data flow, tech stack]

Evaluate:
1. Scalability: Can it handle 10x current load?
2. Reliability: Single points of failure?
3. Security: Attack surface and mitigations?
4. Maintainability: Complexity and coupling?
5. Cost: Resource efficiency?

Provide specific recommendations with priority levels (critical/important/nice-to-have).
```

## Debug Chain Analysis
```
Investigate this production issue systematically:

Symptoms: [describe what's happening]
Error logs: [paste relevant logs]
Recent changes: [deployments, config changes, etc.]
System components: [list relevant services/databases]

Trace the issue through:
1. Request flow (where does it enter, where does it fail?)
2. Data flow (what data is corrupted or missing?)
3. Infrastructure (any resource bottlenecks?)
4. Timing (correlations with deployments/events?)

For each hypothesis, state what evidence supports or refutes it.
End with the most likely root cause and fix.
```

## API & SDK Design
```
Design a [REST/GraphQL/gRPC] API for [system/feature].

Requirements:
- [requirement 1]
- [requirement 2]

Provide:
1. Endpoint/method specifications
2. Request/response schemas (with types)
3. Authentication & authorization model
4. Rate limiting & caching strategy
5. Error response format
6. SDK client interface (TypeScript or Python)
7. Migration strategy from v0 if applicable
```

---
**GPT-5.4 Coding Tips:**
- Excels at multi-file coordination and agentic workflows
- Can autonomously run test-verify-fix cycles
- Strong at maintaining architectural consistency across changes
- Use `developer` role with explicit constraints for best results
- Supports tool use — provide function schemas when applicable