# Llama 3.3 Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Size:** 70B
- **Strengths:** Improved instruction following, reasoning
- **Best for:** Production open-source, matches Llama 3.1 405B quality

## Chain of Thought

3.3 handles more detailed instructions:

```
Analyze this problem thoroughly:

1. **Understanding**: State what you need to solve
2. **Approach**: Describe your method
3. **Execution**: Work through step by step
4. **Verification**: Check your work
5. **Conclusion**: Final answer with confidence

Show your reasoning at each step.
```

## JSON Output

```
Respond with valid JSON matching this schema:
{
  "result": "your answer",
  "reasoning": "brief explanation",
  "confidence": 0.0-1.0
}

Return ONLY the JSON object.
```

## Reasoning Tasks

3.3 excels at complex reasoning:

```
Consider this problem carefully:

- What are the key factors?
- What assumptions are you making?
- Are there edge cases?
- What is the most likely answer and why?

Think it through, then answer.
```

## Key Tips

- 70B matches 405B quality at lower cost
- Better instruction following than 3.1
- Improved reasoning capabilities
- Good for complex multi-step tasks
- Strong code generation
