# Claude 3/3.5 Sonnet Prompting Guide

## Model Characteristics
- **Context:** 200K tokens
- **Strengths:** Balance of speed, cost, intelligence
- **Best for:** Production workloads, coding, general tasks

## Chain of Thought

```xml
<instructions>
Think through this systematically:
1. Understand the problem
2. Plan your approach
3. Execute step by step
4. Verify your answer
</instructions>

<thinking>
[Your reasoning here]
</thinking>

<answer>
[Final answer]
</answer>
```

## JSON Output

```xml
<format>
Return only valid JSON matching:
{"key": "type"}
</format>

<constraints>
- No markdown code blocks
- No explanation
- Valid JSON only
</constraints>
```

## Code Generation

Sonnet excels at code:

```xml
<task>
Write a Python function that [description]
</task>

<requirements>
- Include type hints
- Add docstring
- Handle edge cases
- Include example usage
</requirements>
```

## Key Tips

- Best price/performance ratio
- 3.5 Sonnet significantly better than 3 Sonnet
- Great for coding tasks
- XML tags improve consistency
- Good for high-volume production use
