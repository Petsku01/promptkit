# Mixtral (8x7B, 8x22B) Prompting Guide

## Model Characteristics
- **Type:** Mixture of Experts (MoE)
- **Context:** 32K (8x7B), 64K (8x22B)
- **Strengths:** Efficient, fast, good reasoning
- **Best for:** Cost-effective production, balanced tasks

## Chain of Thought

```markdown
## Instructions
Solve step by step, showing your work.

## Steps

**Step 1:** Understand the problem
- What is being asked?

**Step 2:** Plan
- How will you solve it?

**Step 3:** Execute
- Work through it

**Step 4:** Answer
- State your final answer
```

## JSON Output

```
Return JSON matching:
{"result": "string", "details": "string"}

No markdown, no explanation.
```

## Few-Shot (Recommended)

Mixtral benefits from examples:

```markdown
## Examples

Input: "The weather is great today"
Output: {"sentiment": "positive"}

Input: "I hate waiting in line"
Output: {"sentiment": "negative"}

## Task
Analyze this:
Input: "The food was okay"
Output:
```

## Key Tips

- MoE = faster than dense models of similar quality
- 8x22B stronger but 8x7B more cost-effective
- Few-shot examples improve consistency
- Good for high-volume, cost-sensitive workloads
- Use markdown formatting for structure
