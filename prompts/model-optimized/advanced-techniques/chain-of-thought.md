# Chain-of-Thought (CoT)

## Perus CoT

```
Let's solve this step by step:

[problem]

Step 1: [first step]
Step 2: [second step]
...
Final answer: [answer]
```

## Zero-shot CoT

```
[problem]

Let's think step by step.
```

## Structured CoT

```
Problem: [problem]

Analysis:
1. What do we know?
2. What do we need to find?
3. What approach should we use?

Solution:
Step 1: [action and reasoning]
Step 2: [action and reasoning]
...

Verification:
- Does this answer make sense?
- Did we address all parts?

Final Answer: [answer]
```

## CoT with Verification

```
Solve: [problem]

First, solve step by step.
Then, verify your answer by working backwards.
If there's a discrepancy, identify the error and correct it.
```

## Expert CoT

```
As an expert in [field], analyze this problem:

[problem]

Apply your expertise:
1. Identify the key concepts involved
2. Recall relevant principles or formulas
3. Apply them systematically
4. Check for edge cases
5. State your conclusion with confidence level
```

## CoT for Code

```
I need to write code for: [task]

Let me think through this:

1. Inputs and outputs:
   - Input: [what the function receives]
   - Output: [what it should return]

2. Algorithm:
   - [step 1]
   - [step 2]
   - ...

3. Edge cases to handle:
   - [edge case 1]
   - [edge case 2]

4. Implementation:
   [code]

5. Test:
   [test cases]
```

## Huomioita

- Toimii parhaiten GPT-4+, Claude, Gemini Pro
- Reasoning-mallit (o1, o3) eivät tarvitse "think step by step"
- Pienet mallit (<7B) hyötyvät vähemmän
