# Tree-of-Thoughts (ToT)

Explore multiple thought paths, evaluate and select the best.

## Basic ToT

```
Problem: [problem]

Generate 3 initial approaches:

Approach A: [brief description]
Approach B: [brief description]
Approach C: [brief description]

Evaluate each (1-10):
A: [score] - [reason]
B: [score] - [reason]
C: [score] - [reason]

Pursue the highest-scoring approach:
[detailed solution using best approach]
```

## ToT with Backtracking

```
Solve: [problem]

I will explore multiple paths and backtrack if needed.

Path 1:
- Step 1.1: [action]
- Evaluation: [is this promising? continue or backtrack?]
- Step 1.2: [action]
- Evaluation: [is this promising?]
[continue or backtrack]

Path 2 (if Path 1 failed):
- Step 2.1: [different action]
...

Best path found: [describe winning path]
Solution: [final answer]
```

## ToT for Creative Tasks

```
Task: [creative task]

Generate 5 different concepts:
1. [concept 1 - brief]
2. [concept 2 - brief]
3. [concept 3 - brief]
4. [concept 4 - brief]
5. [concept 5 - brief]

Score each on: originality, feasibility, impact

| Concept | Originality | Feasibility | Impact | Total |
|---------|-------------|-------------|--------|-------|
| 1       |             |             |        |       |
...

Develop top 2 concepts further:

Concept [X] detailed:
[expand on the concept]

Concept [Y] detailed:
[expand on the concept]

Final selection: [chosen concept with justification]
```

## ToT for Debugging

```
Bug: [bug description]

Hypothesis tree:

H1: [first hypothesis]
├── Evidence for: [evidence]
├── Evidence against: [evidence]
└── Test: [how to verify]

H2: [second hypothesis]
├── Evidence for: [evidence]
├── Evidence against: [evidence]
└── Test: [how to verify]

H3: [third hypothesis]
...

Most likely hypothesis: [H#]
Reason: [why this is most likely]
Fix: [proposed solution]
```

## ToT for Design

```
Design challenge: [challenge]

Option A: [design approach 1]
- Pros: [list]
- Cons: [list]
- Complexity: [low/medium/high]

Option B: [design approach 2]
- Pros: [list]
- Cons: [list]
- Complexity: [low/medium/high]

Option C: [design approach 3]
- Pros: [list]
- Cons: [list]
- Complexity: [low/medium/high]

Decision matrix:
| Criteria     | Weight | A | B | C |
|--------------|--------|---|---|---|
| Performance  | 3      |   |   |   |
| Simplicity   | 2      |   |   |   |
| Scalability  | 2      |   |   |   |
| Weighted Sum |        |   |   |   |

Recommended: [option] because [reason]
```
