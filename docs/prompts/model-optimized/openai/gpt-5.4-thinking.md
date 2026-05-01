[← Back to Model-Optimized Openai](../index.md)

# GPT-5.4: Thinking Mode

## Deep Problem Solving
```
Think through this problem step by step. Show your reasoning process.

Problem: [describe the problem]

Approach:
1. First, restate the problem in your own words
2. Identify key constraints and assumptions
3. Consider multiple solution approaches
4. Evaluate trade-offs for each approach
5. Select the best approach with justification
6. Work through implementation details
7. Verify the solution addresses the original problem
8. Identify edge cases or potential failures

Take your time. It's better to be thorough than fast.
```

## Complex Debugging (Thinking Mode)
```
I have a complex bug that requires systematic investigation.

Symptoms: [what's happening]
Expected: [what should happen]
Environment: [OS, runtime, versions]
Recent changes: [what changed recently]

Steps taken so far:
- [step 1]
- [step 2]

Think through this methodically:
1. Generate at least 3 hypotheses for the root cause
2. For each hypothesis, what evidence would confirm or deny it?
3. What's the most efficient order to test these hypotheses?
4. After testing, what's your conclusion?

Use extended reasoning. Consider edge cases.
```

## Architecture Decision Record
```
I need to make an architecture decision. Think through it carefully.

Decision: [what needs to be decided]
Context: [why this matters]

Options I'm considering:
A: [option description]
B: [option description]
C: [option description]

For each option, reason through:
- Complexity (implementation & operational)
- Performance characteristics
- Scalability limits
- Team expertise required
- Migration effort
- Failure modes

Then make a recommendation with:
- Confidence level (high/medium/low)
- Conditions under which you'd recommend differently
- What to validate before committing
```

## Math & Logic Verification
```
Verify this mathematical/logical derivation:

Claim: [state the claim]
Given: [list assumptions/premises]
Derivation: [paste or describe the reasoning]

Check for:
1. Are all assumptions stated explicitly?
2. Is each logical step valid?
3. Are there hidden assumptions?
4. Could the conclusion follow from weaker premises?
5. What would falsify this conclusion?
6. Is this the simplest possible proof?

Provide a confidence score (0-100%) and explain what would increase it.
```

---
**GPT-5.4 Thinking Mode Tips:**
- Use for problems requiring deep multi-step reasoning
- Benefits from explicit "think step by step" instructions
- Can maintain reasoning across very long chains
- Ask it to generate and evaluate multiple hypotheses
- It will naturally show its work — no need to force structured output
- Best results when you provide context and constraints explicitly
- Avoid rushing — give it room to explore dead ends and backtrack