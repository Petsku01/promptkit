[← Back to Agentic](./index.md)

# Agentic: Orchestration

## Multi-Agent Coordination

```
You are the orchestrator managing multiple specialized agents:

Agents available:
- Researcher: Finds and synthesizes information
- Coder: Writes and reviews code
- Writer: Creates and edits text
- Critic: Reviews and improves outputs

Task: [complex task]

Orchestration plan:
1. Which agent(s) needed?
2. In what order?
3. What does each agent receive?
4. How to combine outputs?

Execute the plan step by step.
```

## Workflow Execution

```
Workflow definition:

STEP 1: [action]
  -> Output: [what it produces]
  -> Next: STEP 2

STEP 2: [action]  
  -> Input: Output from STEP 1
  -> Output: [what it produces]
  -> Next: STEP 3 or END

Current state: [where we are]
Execute next step and report result.
```

## Pipeline Controller

```
Pipeline stages:
1. INPUT -> Validate and parse
2. PROCESS -> Transform/compute
3. VERIFY -> Check correctness
4. OUTPUT -> Format result

Rules:
- Each stage must complete before next
- If stage fails, stop and report
- Log progress at each stage

Input: [input data]

Execute pipeline:
```

## Parallel Task Management

```
Tasks to complete (can run in parallel):
□ Task A: [description]
□ Task B: [description]
□ Task C: [description]

Identify dependencies:
- Task A depends on: [nothing/other tasks]
- Task B depends on: [nothing/other tasks]
- Task C depends on: [nothing/other tasks]

Execution plan:
- Parallel batch 1: [independent tasks]
- Parallel batch 2: [tasks dependent on batch 1]
...

Execute and report all results.
```

## State Machine

```
Define states for: [task]

STATES:
- INIT: Starting state
- WORKING: Processing
- WAITING: Need input/tool result
- ERROR: Something went wrong
- DONE: Completed successfully

TRANSITIONS:
INIT -> WORKING: Begin task
WORKING -> WAITING: Need external input
WAITING -> WORKING: Received input
WORKING -> ERROR: Failure detected
WORKING -> DONE: Success
ERROR -> WORKING: Retry
ERROR -> DONE: Give up (with explanation)

Current state: INIT
Transition to next state and explain why.
```

## Checkpoint & Resume

```
Long-running task: [task]

After each major step:
1. Save checkpoint: What's been done
2. Current state: Where are we
3. Remaining: What's left

CHECKPOINT:
```yaml
completed:
  - step1: [result]
  - step2: [result]
current_step: step3
remaining:
  - step4
  - step5
context:
  key_info: [important state]
```

If interrupted, resume from last checkpoint.
```
