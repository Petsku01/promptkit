# Chain-of-Thought (CoT)

## When to Use

- Complex reasoning problems (math, logic, multi-step analysis)
- When you need to see the model's reasoning process
- Debugging why a model gives wrong answers
- Any task where "thinking out loud" helps

## How It Works

LLMs are autoregressive—they predict the next token based on previous tokens. By forcing the model to output intermediate reasoning steps, you give it "working memory" in its own output. This dramatically improves accuracy on complex tasks.

The key insight: **the model can use its own output as context for further reasoning.**

## The Prompt

```
[TASK_DESCRIPTION]

Think through this step-by-step:
1. First, identify [WHAT_TO_IDENTIFY]
2. Then, analyze [WHAT_TO_ANALYZE]
3. Finally, conclude [WHAT_TO_CONCLUDE]

Show your reasoning at each step before giving your final answer.
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[TASK_DESCRIPTION]` | The problem to solve | `Calculate the total cost including 20% tax` |
| `[WHAT_TO_IDENTIFY]` | First step focus | `the base prices` |
| `[WHAT_TO_ANALYZE]` | Middle step focus | `the tax calculation` |
| `[WHAT_TO_CONCLUDE]` | Final output | `the total amount` |

## Example

**Input:**
```
A store sells apples for $2 each and oranges for $3 each. 
If I buy 5 apples and 3 oranges, and there's a 10% discount 
for purchases over $15, what's my total?

Think through this step-by-step:
1. First, calculate the subtotal
2. Then, check if discount applies
3. Finally, calculate the final total

Show your reasoning at each step.
```

**Output:**
```
Step 1: Calculate subtotal
- Apples: 5 × $2 = $10
- Oranges: 3 × $3 = $9
- Subtotal: $10 + $9 = $19

Step 2: Check discount eligibility
- Subtotal ($19) > $15 threshold
- Discount applies: 10%

Step 3: Calculate final total
- Discount amount: $19 × 0.10 = $1.90
- Final total: $19 - $1.90 = $17.10

**Final Answer: $17.10**
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | ✅ | Excellent, follows structure well |
| Claude 3.5 | ✅ | Very thorough reasoning |
| Llama 3 70B | ✅ | Works well |
| Gemini Pro | ✅ | Good results |

## Variations

- **Zero-shot CoT:** Simply add "Let's think step by step" without specifying steps
- **Structured CoT:** Use XML tags `<thinking>...</thinking>` then `<answer>...</answer>`
- **Verbose CoT:** Ask for "detailed reasoning with all intermediate calculations"

## Common Mistakes

- ❌ Asking for "just the answer" — defeats the purpose
- ❌ Too vague steps — be specific about what each step should analyze
- ❌ Skipping verification — add "double-check your work" for math

## Related Patterns

- [Self-Consistency](./self-consistency.md) — Run CoT multiple times, take majority answer
- [Tree-of-Thought](./tree-of-thought.md) — Explore multiple reasoning branches

---

*Last tested: 2026-03-08*
