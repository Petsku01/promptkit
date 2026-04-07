# Few-Shot with Negatives

**Use case:** Training LLM with positive AND negative examples

**Pattern:** Few-Shot Learning with Contrast

---

## Quick Version (~100 tokens)

```
EXAMPLES:

✓ GOOD: Concise, specific, actionable
✗ BAD: Vague, generic, no clear outcome

✓ GOOD: "Optimize Python loop using list comprehension"
✗ BAD: "Make code better"

Now generate similar output for: [task]
```

---

## Extended Version (~400 tokens)

```
FEW-SHOT LEARNING WITH NEGATIVES:

Learn from both what to do AND what to avoid.

POSITIVE EXAMPLES (✓ DO THIS):

Example 1:
Input: "Summarize quarterly sales report"
Output: "Q3 2026: Revenue $2.4M (+15% YoY), driven by Enterprise segment. Key challenges: churn in SMB. Action items: 1) Retention campaign, 2) Upsell prep for Q4."
Why: Specific numbers, clear structure, actionable

Example 2:
Input: "Explain Python decorators"
Output: "Decorators wrap functions to add behavior without modifying code. Like @login_required checking auth before running view. Example: @timer logs execution time."
Why: Concrete analogy, working example, practical use case

NEGATIVE EXAMPLES (✗ DON'T DO THIS):

Example 1:
Input: "Summarize quarterly sales report"
Output: "The quarter was good with some challenges and opportunities ahead."
Why: Vague, no specifics, no actionable information

Example 2:
Input: "Explain Python decorators"
Output: "Decorators are a powerful Python feature that enables advanced programming patterns through higher-order functions and functional programming concepts."
Why: Jargon-heavy, no concrete example, hard to understand

PATTERN RECOGNITION:

✓ Good outputs are: specific, structured, actionable, example-driven
✗ Bad outputs are: vague, generic, jargon-heavy, lacking examples

TASK:
[Your actual task here]

Apply the patterns. Generate output following positive examples, avoiding negative patterns.
```

---

## Metadata

- **Author:** Based on AI Agent Patterns (2026)
- **Tags:** few-shot, learning, examples, contrast
- **Models:** All
- **Version:** 1.0
