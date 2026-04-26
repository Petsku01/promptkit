[← Back to Model-Optimized Prompts](../index.md)

# Claude Opus 4.5: Coding

## Architecture Design
```xml
<task>
Design a system architecture for [description].
</task>

<requirements>
- Scale: [expected scale]
- Performance: [requirements]
- Security: [requirements]
- Budget: [constraints]
</requirements>

<deliverables>
1. High-level architecture diagram (mermaid or text)
2. Component breakdown with responsibilities
3. Data flow and API contracts
4. Technology recommendations with rationale
5. Potential bottlenecks and mitigations
6. Security considerations
</deliverables>
```

## Code Review (Thorough)
```xml
<code>
[paste code]
</code>

<review_scope>
Perform a thorough code review covering:
1. **Correctness**: Logic errors, edge cases, race conditions
2. **Security**: Vulnerabilities, input validation, auth issues
3. **Performance**: Inefficiencies, N+1 queries, memory leaks
4. **Maintainability**: Code clarity, documentation, testability
5. **Architecture**: Design patterns, coupling, separation of concerns
</review_scope>

<output_format>
For each issue:
- Location (file:line)
- Severity (critical/high/medium/low)
- Description
- Recommended fix
</output_format>
```

## Complex Refactoring
```xml
<current_code>
[paste code]
</current_code>

<refactoring_goals>
- [goal 1]
- [goal 2]
</refactoring_goals>

<constraints>
- Maintain backward compatibility
- Zero downtime migration path
- Comprehensive test coverage
</constraints>

<request>
Plan and execute this refactoring:
1. Analyze current code structure
2. Identify refactoring opportunities
3. Create step-by-step migration plan
4. Implement changes with explanations
5. Provide test cases for verification
</request>
```

---
**Claude Opus 4.5 Coding Tips:**
- Excellent for architecture and design decisions
- Use for thorough code reviews where depth matters
- Great at explaining complex technical concepts
- XML structure helps with multi-part coding tasks
