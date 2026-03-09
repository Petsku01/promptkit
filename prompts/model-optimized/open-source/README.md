# Chain of Thought — Open Source Models

Covers: Qwen, DeepSeek, Yi, Phi, Command-R, and similar models.

## General Optimizations

- **Simpler is better** — Less meta-instruction, more direct
- **Explicit format** — Show the exact output structure you want
- **Shorter prompts** — Many open-source models have smaller context
- **Few-shot helps** — Examples improve consistency significantly

## Universal Prompt (Works Across Models)

```
Think step by step to solve this problem.

Step 1: [Understand the problem]
Step 2: [Plan your approach]  
Step 3: [Execute the plan]
Step 4: [Check your answer]

Show your work for each step, then give your final answer.
```

## Model-Specific Notes

### Qwen (2, 2.5)
- Handles Chinese and English well
- Good with structured output
- Supports longer context (Qwen2.5: 128k)

```
按步骤思考 / Think step by step:
1. 理解问题 / Understand
2. 分析关键点 / Analyze  
3. 逐步解决 / Solve
4. 验证答案 / Verify
```

### DeepSeek (V2, V3, Coder)
- Strong at code and math
- Benefits from explicit reasoning markers

```
Let me solve this step by step:

[Step 1] First, I'll analyze...
[Step 2] Next, I'll...
[Step 3] Then...
[Result] Therefore...
```

### Yi (6B, 34B)
- Keep prompts concise
- Works well with numbered lists

```
Solve step by step:
1. 
2.
3.
Answer:
```

### Phi (3, 3.5)
- Very efficient with short prompts
- Good for simple CoT tasks

```
Think through this:
- What's the question?
- What do I know?
- How do I solve it?
- What's the answer?
```

### Command-R (Cohere)
- Good at following instructions
- Supports grounded generation

```
Reason through this problem:

UNDERSTANDING:
[What the problem asks]

APPROACH:
[How you'll solve it]

SOLUTION:
[Step-by-step work]

ANSWER:
[Final answer]
```

## Notes

- Test with your specific model — behavior varies significantly
- Smaller models (< 7B) need simpler prompts
- Larger models (> 30B) can handle more complex instructions
- Always include format examples for consistency
