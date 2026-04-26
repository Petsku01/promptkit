[← Back to Anthropic](./index.md)

# Claude 3.7 Sonnet: Coding

## Code Generation with Planning
```xml
<task>
Write a [language] implementation for [feature].
</task>

<requirements>
- [requirement 1]
- [requirement 2]
</requirements>

<instructions>
1. First, outline your approach and key design decisions.
2. Consider edge cases before implementing.
3. Write clean, well-documented code.
4. Include error handling.
</instructions>
```

## Code Review
```xml
<task>
Review the following code as a senior engineer.
</task>

<code>
[paste code]
</code>

<review_criteria>
- Security vulnerabilities
- Performance issues
- Code clarity and maintainability
- Test coverage gaps
</review_criteria>

Provide specific, actionable feedback with line references.
```

## Debugging with Extended Thinking
```xml
<context>
I'm seeing this error:
[error message]

In this code:
[paste code]
</context>

<instructions>
Take your time to analyze this systematically:
1. Understand what the code is trying to do
2. Identify where the error originates
3. Trace the execution path
4. Propose a fix with explanation
</instructions>
```

---
**Claude 3.7 Sonnet Coding Tips:**
- Use XML tags to structure context and instructions
- Ask for planning/thinking before implementation
- Specify review criteria explicitly
- Request line-number references in reviews
