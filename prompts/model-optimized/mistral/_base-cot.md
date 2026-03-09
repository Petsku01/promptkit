# Chain of Thought — Mistral (Mistral, Mixtral, Large)

## Optimizations

- **Clear sections** — Use markdown headers to separate concerns
- **Explicit format** — Mistral benefits from format examples
- **Worded scales** — Use words instead of numbers for ratings
- **Few-shot friendly** — Include examples when possible

## The Prompt

```markdown
## Task
Solve the following problem using step-by-step reasoning.

## Process
Follow these steps in order:

### Step 1: Understand
- What is the question asking?
- What information is provided?

### Step 2: Plan
- What approach will you use?
- What sub-problems need solving?

### Step 3: Execute
- Work through each sub-problem
- Show calculations or reasoning

### Step 4: Verify
- Does the answer make sense?
- Did you address all parts?

### Step 5: Answer
- State your final answer clearly
```

## With Few-Shot Example

```markdown
## Example

**Problem:** What is 15% of 80?

**Step 1:** I need to find 15% of 80
**Step 2:** Convert 15% to decimal: 0.15
**Step 3:** Multiply: 0.15 × 80 = 12
**Step 4:** Check: 12/80 = 0.15 ✓
**Answer:** 12

---

Now solve this problem:
```

## Notes

- Mistral responds well to explicit section headers
- Avoid vague instructions like "think carefully" — be specific
- For Mixtral: can handle longer context than base Mistral
