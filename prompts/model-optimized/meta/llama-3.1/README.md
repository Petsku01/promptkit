# Llama 3.1 Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Sizes:** 8B, 70B, 405B
- **Strengths:** Long context, tool use, multilingual
- **Best for:** Open-source deployments, fine-tuning

## Chain of Thought

```
Solve this problem step by step.

Step 1: Understand
[What is being asked?]

Step 2: Plan
[How will you solve it?]

Step 3: Execute
[Work through it]

Step 4: Verify
[Check your answer]

Final Answer:
```

## Tool Use

Llama 3.1 supports native tool calling:

```
You have access to these tools:
- search(query): Search the web
- calculate(expression): Do math

Use tools when helpful. Format:
<tool_call>{"name": "tool", "args": {}}</tool_call>
```

## JSON Output

```
Return your answer as JSON:
{
  "answer": "string",
  "confidence": "high|medium|low"
}

JSON only, no other text.
```

## Key Tips

- 128K context - can handle long documents
- 405B rivals GPT-4 quality
- Native tool use support
- Good for fine-tuning (open weights)
- System prompt for persona, user for task
