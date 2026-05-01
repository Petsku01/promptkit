[← Back to Model-Optimized Agentic](../index.md)

# Agentic: Planning

## Task Decomposition

```
Break down this complex task into subtasks:

Task: [complex task]

For each subtask:
1. Description (what needs to be done)
2. Dependencies (what must be done first)
3. Estimated complexity (simple/medium/complex)
4. Success criteria (how to know it's done)

Output as numbered list with dependencies shown.
```

## Goal-Oriented Planning

```
I need to achieve: [goal]

Current state: [current situation]
Constraints: [any limitations]

Create a plan:

## Goal Analysis
What does success look like?

## Gap Analysis
What's missing between current and goal state?

## Action Plan
1. [Step] - [Why this order]
2. [Step] - [Why this order]
...

## Risk Assessment
What could go wrong? Mitigations?

## Checkpoints
How will I measure progress?
```

## Hierarchical Task Planning

```
Main goal: [goal]

Level 1 - Major phases:
├── Phase A: [description]
├── Phase B: [description]
└── Phase C: [description]

Level 2 - Tasks per phase:
Phase A:
├── Task A.1: [description]
├── Task A.2: [description]
...

Level 3 - Subtasks:
Task A.1:
├── A.1.1: [action]
├── A.1.2: [action]
...

Start with Phase A, Task A.1.
```

## Adaptive Planning

```
Initial plan for: [task]

After each step:
1. Execute the step
2. Evaluate: Did it work as expected?
3. Adapt: Modify remaining steps if needed

Plan:
[initial plan]

After Step 1 result: [result]
Adaptation needed? [yes/no and why]
Updated remaining plan: [if changed]
```

## Resource-Aware Planning

```
Task: [task]

Available resources:
- Time: [time available]
- Tools: [available tools]
- Information: [what I have access to]

Create a plan that:
1. Fits within time constraints
2. Uses only available tools
3. Accounts for missing information

Plan with resource allocation:
```

## Contingency Planning

```
Primary plan for: [task]

For each critical step, define:
- What could fail?
- How to detect failure?
- Backup approach?

Plan:
Step 1: [action]
  └─ If fails: [backup]
Step 2: [action]
  └─ If fails: [backup]
...
```
