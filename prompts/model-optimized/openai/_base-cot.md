# Chain of Thought — OpenAI (GPT-4, GPT-4o)

## Optimizations

- **Concise instructions** — GPT models prefer shorter, direct prompts
- **Markdown structure** — Use headers and lists for clarity
- **Developer role** — Place core instructions in developer/system message
- **Step numbering** — Explicit numbered steps work well

## The Prompt

```
Think step by step:

1. State what you understand about the problem
2. Break it into smaller parts
3. Solve each part
4. Combine for final answer

Show your work at each step.
```

## System Message Version

```
You solve problems methodically. For each question:
1. Restate the problem
2. Identify key components
3. Work through each component
4. Synthesize the solution

Always show reasoning before conclusions.
```

## Notes

- GPT-4o is faster but may skip steps — use "show each step" explicitly
- For math: add "double-check your arithmetic"
- For code: add "trace through with an example"
