[← Back to Model-Optimized Prompts](../index.md)

# Chain-of-Thought (CoT)

> **Research**: Wei et al. 2022 - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
> **Key Finding**: CoT improves performance on math/reasoning by 10-20% on GPT-3+

## When to Use CoT

 **USE CoT for:**
- Math problems
- Multi-step reasoning
- Logic puzzles
- Planning tasks
- Complex analysis

 **DON'T use CoT for:**
- Simple factual questions
- Creative writing
- Reasoning models (o1, o3) - they do it internally
- Very small models (<7B) - limited benefit

## Zero-Shot CoT

```
[problem]

Let's think step by step.
```

**Why it works**: This simple phrase triggers reasoning behavior.
**Limitation**: Less effective than few-shot for complex tasks.

## Structured CoT

```
Problem: [problem]

STEP 1 - Understand:
What do we know?
What do we need to find?

STEP 2 - Plan:
What approach will work?

STEP 3 - Execute:
[Show each calculation/reasoning step]

STEP 4 - Verify:
Does this answer make sense?
Let me check: [verification]

Final Answer: [answer]
```

## CoT with Self-Verification

```
Solve: [problem]

First, solve step by step.
Then, verify by:
1. Checking the math
2. Testing with a simple example
3. Looking for edge cases

If verification fails, identify the error and correct it.

Show your work.
```

## Few-Shot CoT (Most Effective)

```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 balls. How many tennis balls does he have now?

A: Let me solve this step by step.
1. Roger starts with 5 balls
2. He buys 2 cans × 3 balls = 6 new balls
3. Total: 5 + 6 = 11 balls
Answer: 11 tennis balls

Q: [your problem]

A: Let me solve this step by step.
```

## CoT for Code

```
Task: [coding task]

THINK:
1. What are the inputs? [list]
2. What should the output be? [describe]
3. What algorithm fits? [approach]
4. Edge cases? [list]

IMPLEMENT:
[code]

VERIFY:
Test case 1: [input] -> [expected] [x]
Test case 2: [input] -> [expected] [x]
Edge case: [input] -> [expected] [x]
```

## Anti-Patterns (What NOT to Do)

 **Don't use with o1/o3 models:**
```
# BAD - o1 already reasons internally
Let's think step by step about this math problem...
```

 **Don't force steps for simple questions:**
```
# BAD - overkill
Q: What is 2+2?
A: Let me think step by step...
Step 1: Identify the numbers (2 and 2)
Step 2: Apply addition...
```

 **Don't use vague step descriptions:**
```
# BAD - not actual reasoning
Step 1: Think about it
Step 2: Consider options
Step 3: Get answer
```

## Model Compatibility

| Model | CoT Benefit | Notes |
|-------|-------------|-------|
| GPT-4/4o | High | Works great |
| GPT-3.5 | Medium | Simpler problems |
| Claude 3+ | High | XML tags help |
| o1/o3 | None | Built-in reasoning |
| Llama 70B+ | High | Needs clear structure |
| Llama 8B | Low | Limited benefit |
| Gemini Pro | High | Works well |
