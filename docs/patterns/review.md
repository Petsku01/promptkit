# Review Patterns

Patterns for critical analysis and review tasks.

## Senior Reviewer

Strict, critical code review persona.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .task("Review this architecture proposal")
    .context(proposal)
    .build())
```

**When to use:** Code review, catching edge cases, security audits.

The senior reviewer pattern creates a persona with 15+ years of experience who never says "looks good" unless it's genuinely excellent.