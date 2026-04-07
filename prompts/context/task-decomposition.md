# Task Decomposition Context

**Use case:** Breaking complex tasks into steps

**Pattern:** Hierarchical task breakdown

---

## Quick Version (~80 tokens)

```
TASK DECOMPOSITION:

Goal: Build a login system

Steps:
1. Design database schema
2. Create auth endpoints  
3. Implement password hashing
4. Add session management
5. Build frontend form

Execute one step at a time.
```

---

## Extended Version (~400 tokens)

```
HIERARCHICAL TASK DECOMPOSITION:

Complex tasks need structure. Break down before executing.

GOAL: [High-level objective]

DECOMPOSITION:

Phase 1 — Foundation (prerequisites):
□ Step 1.1: [prerequisite task]
□ Step 1.2: [prerequisite task]
□ Step 1.3: [prerequisite task]
Dependencies: None (can run in parallel)

Phase 2 — Core Implementation:
□ Step 2.1: [core task]
  - Sub-step 2.1.1: [detail]
  - Sub-step 2.1.2: [detail]
□ Step 2.2: [core task]
  - Sub-step 2.2.1: [detail]
Dependencies: Phase 1 complete

Phase 3 — Integration:
□ Step 3.1: [integration task]
□ Step 3.2: [integration task]
Dependencies: Phase 2.1 complete

Phase 4 — Validation:
□ Step 4.1: [testing task]
□ Step 4.2: [review task]
Dependencies: All previous phases

EXECUTION RULES:

1. SEQUENTIAL WITHIN PHASE: Complete steps in order within each phase
2. PARALLEL ACROSS PHASES: Don't start Phase N+1 until Phase N complete
3. CHECKPOINT: Save state after each phase
4. BLOCKERS: If step blocked, halt entire phase, report blocker

PROGRESS TRACKING:

Format:
```
[Phase X] Step Y.Z: [STATUS]
- Started: [timestamp]
- Completed: [timestamp] or BLOCKED: [reason]
- Output: [reference to result]
```

WHY DECOMPOSE:

Without decomposition:
- Steps get skipped or forgotten
- Dependencies violated
- Progress hard to track
- Recovery after failure difficult

With decomposition:
- Clear execution order
- Explicit dependencies
- Observable progress
- Resumable after interruption
```

---

## Metadata

- **Author:** Based on project management best practices
- **Tags:** decomposition, planning, steps, organization
- **Models:** All
- **Version:** 1.0
