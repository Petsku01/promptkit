# Claude 3 Opus Prompting Guide

## Model Characteristics
- **Context:** 200K tokens
- **Strengths:** Highest intelligence, complex reasoning, nuanced tasks
- **Best for:** Research, analysis, creative writing, hard problems

## Chain of Thought

Opus handles sophisticated reasoning well:

```xml
<task>
Analyze this complex problem thoroughly.
</task>

<instructions>
1. Consider multiple perspectives
2. Identify assumptions and edge cases
3. Reason through step by step
4. Critique your own reasoning
5. Provide a well-supported conclusion
</instructions>

<format>
<analysis>
[Your detailed reasoning]
</analysis>

<conclusion>
[Final answer with confidence level]
</conclusion>
</format>
```

## Extended Thinking

Enable for complex problems:

```xml
<instructions>
Take your time to think deeply about this problem.
Use extended thinking to explore multiple solution paths.
Consider edge cases and potential issues.
</instructions>
```

## Key Tips

- Can handle very long, detailed instructions
- XML structuring helps organize complex prompts
- Best for accuracy-critical tasks
- Most expensive Claude - use when quality matters
- Excels at nuanced, multi-part analysis
