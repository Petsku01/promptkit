# DeepSeek V4 Pro: Reasoning

## Complex Multi-Step Problem Solving
```
Solve this problem step by step. Show your reasoning.

Problem: [describe the problem]
Domain: [math / engineering / logic / etc.]
Constraints: [any known constraints]

Approach:
1. Restate the problem clearly
2. Identify sub-problems and dependencies
3. Solve each sub-problem
4. Verify each solution before proceeding
5. Combine sub-solutions
6. Verify the combined result
7. Check for edge cases

Take your time. Accuracy over speed.
```

## Architecture Decision Record (Thinking Mode)
```
I need to make an important technical decision.

Decision: [what to decide]
Context: [business/technical context]
Options:
A: [option]
B: [option]

For each option, reason through:
- Implementation complexity
- Operational burden
- Scalability limits
- Failure modes
- Cost (development + operational)
- Migration effort

Recommendation with confidence level.
What would change your mind?
```

## Long-Document Analysis & Reasoning
```
Analyze this document/corpus and reason about its contents.

Document(s): [paste or describe — up to 1M tokens]
Question: [what you need to understand]

Tasks:
1. Extract key claims and data points
2. Identify logical structure and argument flow
3. Check for internal consistency
4. Cross-reference claims against each other
5. Identify unsupported assertions
6. Draw evidence-based conclusions
7. Flag remaining uncertainties

Leverage the full 1M context — no need to summarize first.
```

## Mathematical & Scientific Reasoning
```
Work through this problem rigorously.

Problem: [math/science question]
Given: [assumptions, data, constraints]

Protocol:
1. State the problem formally
2. Identify applicable principles/theorems
3. Develop a solution approach
4. Execute step by step with verification
5. Check the result (units, bounds, edge cases)
6. If the answer seems wrong, re-examine assumptions

Show all intermediate steps.
If you reach a contradiction, backtrack and identify the flawed assumption.
```

---
**DeepSeek V4 Pro Reasoning Tips:**
- Enable thinking mode (`deepseek-reasoner`) for complex reasoning tasks
- Can handle very long reasoning chains with 1M context
- Excellent at mathematical and scientific reasoning
- Strong at agentic coding with extended autonomous execution
- Competitive with GPT-5 / Claude Opus on most benchmarks
- Cost-efficient enough for experimental/exploratory reasoning
- V4 Pro replaces R1 for most use cases (use thinking mode instead)