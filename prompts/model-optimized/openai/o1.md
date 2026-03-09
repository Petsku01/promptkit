# o1 / o1-mini / o3 Prompting Guide

## Model Characteristics
- **Type:** Reasoning models (think internally before responding)
- **Context:** 128K-200K tokens
- **Strengths:** Complex reasoning, math, code, logic, science
- **Best for:** Hard problems requiring deep thinking

---

## ⚠️ CRITICAL: How o1/o3 Works Differently

These models think **internally** before responding. 

**DON'T** say:
- "Think step by step"
- "Show your reasoning"
- "Let's work through this"

**DO** say:
- State the problem directly
- Be clear about what you want
- Specify output format if needed

---

## Prompt 1: Math Problem

❌ Wrong:
```
Think step by step and solve this integral.
```

✅ Correct:
```
Solve: ∫ x² · eˣ dx

Give the final answer in simplified form.
```

---

## Prompt 2: Code Problem

```
Write a Python function that finds the longest palindromic substring in a string.

Requirements:
- O(n²) time complexity or better
- Handle empty strings
- Return the actual substring, not just length

Include the function only, no explanation needed.
```

---

## Prompt 3: Logic Puzzle

```
Five houses in a row are painted different colors. Each house is occupied by a person of different nationality. Each person drinks a different beverage, smokes a different brand, and keeps a different pet.

[State the clues]

Who owns the fish?
```

---

## Prompt 4: Algorithm Design

```
Design an algorithm for [problem description].

Constraints:
- Time: O(n log n) maximum
- Space: O(n) maximum
- Must handle edge cases: [list them]

Provide:
1. The algorithm (pseudocode or real code)
2. Time complexity analysis
3. Space complexity analysis
```

---

## Prompt 5: Scientific Analysis

```
Analyze this experimental data:

[paste data]

Determine:
1. The underlying relationship between variables
2. Statistical significance
3. Potential sources of error
4. Conclusions that can be drawn
```

---

## Prompt 6: Proof

```
Prove that [mathematical statement].

State any assumptions or axioms used.
```

---

## Prompt 7: System Design

```
Design a system for [description].

Requirements:
- Scale: [expected load]
- Latency: [requirements]
- Availability: [requirements]

Cover:
- High-level architecture
- Key components
- Data flow
- Tradeoffs made
```

---

## Prompt 8: Code Debugging (Complex)

```
This code has a subtle bug that causes [symptom].

[paste code]

Find the bug and explain the fix.
```

---

## When to Use o1 vs GPT-4

| Task | Best Model |
|------|------------|
| Complex math proofs | o1 |
| Multi-step logic | o1 |
| PhD-level science | o1 |
| Competitive programming | o1 |
| Creative writing | GPT-4 |
| Simple Q&A | GPT-4o |
| Speed critical | GPT-4o |
| Cost sensitive | GPT-4o-mini |

---

## Key Tips

- **Don't prompt for reasoning** - it's automatic and internal
- **Be direct** - just state what you want
- **Harder = better** - o1 shines on difficult problems
- **Simpler prompts** - less instruction, more problem
- **o1-mini** - faster/cheaper for medium difficulty
- **o1-pro/o3** - hardest problems, highest quality
