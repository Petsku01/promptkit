# Chain of Thought — Meta (Llama 3, 3.1, 3.2, 3.3)

## Optimizations

- **Simple structure** — Llama prefers straightforward prompts
- **Explicit format** — Show exactly what output should look like
- **Direct language** — Less meta-commentary, more action
- **System prompt** — Use system role for persona, user for task

## The Prompt

```
Solve this problem step by step.

For each step:
- State what you're doing
- Show your work
- Explain your reasoning

After all steps, give your final answer.
```

## System Prompt Version

```
You are a problem solver. When given a question:
1. Break it into steps
2. Solve each step
3. Show your reasoning
4. Give a clear final answer
```

## With Format Example

```
Solve step by step:

Example format:
Step 1: [What you're doing]
[Your work here]

Step 2: [Next action]
[Your work here]

Final Answer: [Your answer]

---

Problem: [Insert problem here]
```

## Notes

- Llama 3.1+ handles longer context (128k tokens)
- Llama 3.2 has multimodal variants — adjust prompts for vision
- Keep instructions under 500 tokens for best results on smaller variants
- For Llama 3.3: improved instruction following, can be more detailed
