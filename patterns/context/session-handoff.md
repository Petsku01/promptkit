# Session Handoff Pattern

## Description

Create a structured handoff document that captures the current state of a conversation or project so a fresh AI instance (same or different model) can resume exactly where you left off — no guessing, no hallucinating, no re-discovery.

## When to use

- Before ending a long AI session (context window filling up)
- Before switching AI tools or models mid-project
- Before handing a task to a teammate
- Before pausing until tomorrow
- Any time resuming would take >10 minutes of reconstruction

## When to avoid

- Quick five-minute interactions
- Simple one-shot tasks with no continuity needed
- When the AI already has persistent memory that covers the context

## Core Principles

1. **State, not prose** — Structure beats paragraphs. Bullet lists over narrative.
2. **Decisions lock** — Record *what* was decided and *why*. Prevent re-litigation.
3. **Failures matter** — What didn't work saves more time than what did.
4. **Confidence flags** — Mark what's verified vs. assumed.
5. **Next step is mandatory** — Always give the next AI a clear starting point.
6. **Momentum > data** — Preserve direction (where were we going?) not just position (where were we?). The Aspy project discovered that stats that reset after compaction are useless; guidance that persists is what matters.
7. **Reference, don't duplicate** — Link to files by path instead of inlining them. The sidorovanthon/handoff-prompt approach keeps output ~300 tokens by referencing CLAUDE.md/AGENTS.md paths.
8. **Two-prompt transfer** — Export state with Prompt A, import with Prompt B. The LLM--Checkpoint-Prompt approach: A extracts operational state, B tells the new model "don't restart, continue from ACTIVE TASK STATE".
9. **Milestone accumulation** — For extended projects, handoffs accumulate into milestones. RooCode pattern: 3-5 handoffs → 1 milestone with summary + lessons-learned.
10. **Multi-machine awareness** — Use absolute paths so handoffs work across SSH sessions and different machines (ormus-handoff pattern).

## Template Variants

### Quick Handoff (~100 tokens)

```
Before we end, write a handoff prompt I can paste into a new chat with any AI assistant. Include: goal, current status, key decisions, what to avoid, and the very next step. Be concise and structured.
```

### Standard Handoff (~300 tokens)

```
Create a session handoff document with these sections:

1. GOAL - What we're trying to achieve (1-2 sentences)
2. CURRENT STATE - What exists right now (done / in-progress / not started)
3. DECISIONS MADE - Choices locked in, with brief reasoning
4. WHAT TO AVOID - Failed approaches, out-of-scope items, wrong directions
5. OPEN QUESTIONS - Unresolved issues that need judgment
6. NEXT STEP - The single most important action to take first

Write as if briefing a competent colleague who has never seen this project. Be precise, not verbose.
```

### Full Continuation Document (~800 tokens)

```
Generate a Project Continuation Document for session handoff.

PURPOSE: Create a handoff package so a fresh AI instance with zero prior context
can resume this project exactly where we are leaving off — no guessing,
no hallucinating, and no re-discovery.

Write as if briefing a senior technical colleague who is sharp but has
never seen this project before. Be precise. Be concise. Preserve reasoning.
Skip filler.

Use this structure:

## 1. PROJECT IDENTITY
- Project Name
- What This Project Is (1-2 sentences)
- Primary Objective (measurable goal)
- Hard Constraints (non-negotiable rules)

## 2. WHAT EXISTS RIGHT NOW
- What is built and working
- What is partially built
- What is broken or blocked
- What has NOT been started yet

## 3. ARCHITECTURE & TECHNICAL MAP
- Tech stack / tools / platforms
- Key data structures, files, or repos
- How the system works end-to-end (numbered steps)
- External dependencies

## 4. RECENT WORK — WHAT JUST HAPPENED
- What was worked on this session
- Decisions made and WHY (prevent undoing work)
- What changed in the system
- What was discussed but NOT yet implemented
- Open threads or unresolved questions

## 5. WHAT COULD GO WRONG
- Known bugs or issues
- Edge cases to watch for
- Technical debt or shortcuts taken
- Assumptions that could be wrong

## 6. HOW TO THINK ABOUT THIS PROJECT
1. Core architectural pattern and why it was chosen
2. Most common mistake a newcomer would make
3. What looks like it should be refactored but intentionally should NOT be

## 7. DO NOT TOUCH LIST
- Do NOT refactor stable, working systems without being asked
- Do NOT redesign architecture unless explicitly instructed
- Preserve existing naming conventions
- Maintain previously chosen tradeoffs

## 8. CONFIDENCE & FRESHNESS
Flag each section: ✅ HIGH (verified this session) ⚠️ MEDIUM (carried forward) ❓ LOW (assumed)
```

### Ultra-Compact (80 tokens max)

```
Summarize this chat in 80 words: goal, decisions, open tasks, and one sentence on how to continue. Format as bullet points.
```

## Example — Bug Fix Handoff

```
## GOAL
Prevent duplicate email sends in retry processing.

## CURRENT STATE
- Problem identified in src/services/retry.ts
- Two workers can pick the same job before sent_at is updated
- Existing tests don't cover concurrent processing

## DECISIONS MADE
- Keep fix small — no Redis or queue redesign
- Prefer DB-level locking or atomic update

## WHAT TO AVOID
- Don't add Redis for distributed locking (overkill for this scale)
- Don't refactor the entire retry pipeline

## OPEN QUESTIONS
- Can sent_at act as a safe claim field?
- Do we need SELECT ... FOR UPDATE or a conditional UPDATE?

## NEXT STEP
Prototype atomic claim logic in retry.ts and add one concurrency-focused test.
```

## Example — Writing/Research Handoff

```
## GOAL
Publish a practical article on AI-assisted changelog generation.

## CURRENT STATE
- Outline approved
- Sections 1-4 drafted
- Missing: verifier section + conclusion

## DECISIONS MADE
- Target audience: working developers, not AI enthusiasts
- Tone: practical, not hypey
- Include one JSON example and one workflow checklist

## WHAT TO AVOID
- Don't add a CI example (keeping it tool-agnostic)
- Don't expand into failure cases section (article is already long enough)

## NEXT STEP
Write verifier section, trim repetition, add final checklist.
```

## Tags

context, handoff, continuity, session, checkpoint, compaction