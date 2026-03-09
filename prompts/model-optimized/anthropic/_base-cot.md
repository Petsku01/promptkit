# Chain of Thought — Anthropic (Claude 3/4)

## Optimizations

- **XML tags** — Claude excels with structured XML markup
- **Longer context OK** — Claude handles detailed instructions well
- **Thinking tags** — Use `<thinking>` for scratchpad reasoning
- **Explicit structure** — Define output format clearly

## The Prompt

```xml
<instructions>
Approach this problem systematically using chain-of-thought reasoning.
</instructions>

<process>
1. First, analyze what is being asked
2. Identify the key information and constraints
3. Break the problem into logical steps
4. Work through each step, showing your reasoning
5. Verify your solution makes sense
6. Provide your final answer
</process>

<output_format>
Structure your response as:
<thinking>
[Your step-by-step reasoning here]
</thinking>

<answer>
[Your final answer here]
</answer>
</output_format>
```

## With Extended Thinking (Claude 3.5+)

For complex problems, enable extended thinking:

```xml
<instructions>
Use your extended thinking capability to deeply analyze this problem.
Take your time to consider multiple angles before responding.
</instructions>
```

## Notes

- Claude naturally uses `<thinking>` tags when prompted
- XML nesting helps organize complex multi-part prompts
- Claude follows formatting instructions very precisely
- For math: wrap numbers in `<calculation>` tags for clarity
