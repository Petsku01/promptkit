# Self-Consistency

## When to Use

- Math problems where a single answer might be wrong
- Complex reasoning where you want higher confidence
- When accuracy matters more than speed
- Verifying important decisions or calculations

## How It Works

Self-consistency exploits the fact that complex reasoning problems often have multiple valid reasoning paths to the same answer. By sampling multiple independent reasoning chains and taking the majority answer, you reduce the impact of individual reasoning errors.

The key insight: **if three different reasoning paths arrive at the same answer, it's probably correct.**

## The Prompt

```
Solve this problem using three different approaches.
For each approach, show your complete reasoning.
Then compare your answers and give the most likely correct one.

Problem: [PROBLEM_DESCRIPTION]

Approach 1: [METHOD_1]
[reasoning]

Approach 2: [METHOD_2]
[reasoning]

Approach 3: [METHOD_3]
[reasoning]

Comparison:
- Approach 1 got: [answer]
- Approach 2 got: [answer]
- Approach 3 got: [answer]

Final Answer: [most common answer, or explain discrepancy]
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[PROBLEM_DESCRIPTION]` | The problem to solve | `What is 15% of 240?` |
| `[METHOD_1]` | First approach | `Direct calculation` |
| `[METHOD_2]` | Second approach | `Breaking into steps` |
| `[METHOD_3]` | Third approach | `Estimation then refine` |

## Example

**Input:**
```
Solve this problem using three different approaches.
Show your complete reasoning for each, then compare.

Problem: A train travels 120 km in 1.5 hours. 
What is its average speed in km/h?

Approach 1: Direct formula
Approach 2: Unit conversion
Approach 3: Proportional reasoning
```

**Output:**
```
Approach 1: Direct formula
Speed = Distance / Time
Speed = 120 km / 1.5 hours
Speed = 80 km/h

Approach 2: Unit conversion
1.5 hours = 90 minutes
120 km in 90 minutes
= 120/90 km per minute
= 1.33 km/minute
= 1.33 × 60 km/hour
= 80 km/h

Approach 3: Proportional reasoning
In 1.5 hours: 120 km
In 1 hour: 120 / 1.5 = 80 km
Therefore: 80 km/h

Comparison:
- Approach 1: 80 km/h
- Approach 2: 80 km/h
- Approach 3: 80 km/h

All three approaches agree.

Final Answer: 80 km/h
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent, genuinely uses different methods |
| Claude 3.5 | Yes | Very thorough, good at spotting discrepancies |
| Llama 3 70B | Yes | Works well, sometimes similar approaches |
| Gemini Pro | Yes | Good results |

## Variations

- **Voting:** Run the same prompt 5 times, take majority answer
- **Confidence-weighted:** Ask model to rate confidence in each approach
- **Adversarial:** Have one approach try to find flaws in the others

## Common Mistakes

- No: Using only one approach renamed three times
- No: Skipping the comparison step
- No: Not asking for complete reasoning (just answers)

## Related Patterns

- [Chain-of-Thought](./chain-of-thought.md) - The base reasoning pattern
- [Tree-of-Thought](./tree-of-thought.md) - Explore branches, prune bad ones

---

*Last tested: 2026-03-10*
