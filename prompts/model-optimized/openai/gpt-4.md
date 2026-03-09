# GPT-4 Prompting Guide

## Model Characteristics
- **Context:** 8K (standard) / 32K (gpt-4-32k)
- **Strengths:** Complex reasoning, nuanced instructions
- **Best for:** Analysis, creative writing, code generation

## Chain of Thought

```
Think through this step by step:

1. State what you understand
2. Break into smaller parts
3. Solve each part
4. Combine for final answer

Show your work.
```

## JSON Output

Use with `response_format: {"type": "json_object"}`:

```
Analyze this and return JSON:
{"field": "value"}

Return ONLY valid JSON.
```

## Key Tips

- Detailed instructions work well
- Markdown formatting helps structure
- Can handle multi-step complex tasks
- More reliable than turbo for accuracy-critical tasks
