# Session Handoff Prompts

**Use case:** Continue a conversation or project in a new AI session — same model, different model, or different person.

**Pattern:** Session Handoff (see `patterns/context/session-handoff.md`)

---

## Quick Handoff (~100 tokens)

```
Before we end, write a handoff prompt I can paste into a new chat with any AI assistant. Include: goal, current status, key decisions, what to avoid, and the very next step. Be concise and structured.
```

---

## Standard Handoff (~300 tokens)

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

---

## Full Continuation Document (~800 tokens)

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

---

## Resume Prompt

After generating a Continuation Document, generate a Resume Prompt — a self-contained message for the next session:

```
Based on the continuation document above, generate a Resume Prompt that works as a standalone message in a brand new conversation. It should instruct the next AI to:

1. Read the continuation document file
2. Confirm understanding of the project state
3. Identify any critical gaps or ambiguities
4. Continue from the exact point where work left off

Include a USER DIRECTIVE section at the bottom:
- If I provide a task there, the next AI should treat it as its immediate first task.
- If I leave it blank, the AI should analyze the project state, propose the best next action, and wait for confirmation before proceeding.
```

---

## Ultra-Compact Summary (80 tokens)

```
Summarize this chat in 80 words: goal, decisions, open tasks, and one sentence on how to continue. Format as bullet points.
```

---

## Auto-Summary (for automated workflows)

```
Summarize the conversation for continuation. Output a short title, one-sentence goal, 3 bullets: decisions, open tasks, blockers, then a 1-2 sentence "how to resume" instruction.
Keep the total summary under 200 tokens.
Format:
Title: ...
Goal: ...
Decisions:
- ...
Open tasks:
- ...
Blockers:
- ...
Resume: ...
```

---

## JD Hodges' One-Liner

*Minimal effort, maximum signal — paste this at the end of any session:*

```
Before we end, write a complete handoff prompt I can paste into a new chat with any AI assistant. Include our goal, current status, key decisions, what to avoid, and the very next step in a short, clear structure so the next AI can continue immediately.
```

---

## Soft Warning (70% context)

```
This chat is getting long. Let's create a handoff checkpoint so we can continue in a fresh session if needed.
```

---

## Hard Warning (85-90% context)

```
We need to wrap up this session soon — context is running low. Please draft a handoff prompt so we can continue in a fresh session immediately.
```

---

## Checkpoint Prompt (LLM-A → LLM-B transfer)

*Two-prompt system: first extracts state from the ending model, second instructs the receiving model.*

**Prompt A (export state):**

```
You are preparing a structured transfer of this conversation so another LLM can continue the task without losing context.
Your job is to export the COMPLETE working state of this conversation.
Do NOT summarize loosely. Extract the operational state precisely.

Output must follow the structure below.

TASK OVERVIEW
The original goal of the conversation
What the user ultimately wants to achieve

CURRENT PROGRESS
What has already been completed
Decisions made
Results generated so far

KEY CONTEXT
Important facts provided by the user
Constraints or requirements
Environment details (tools, frameworks, languages, location if relevant)

USER PREFERENCES
Writing style
Response format preferences
Any behavioral instructions given to the assistant

IMPORTANT INSIGHTS
Reasoning conclusions already reached
Assumptions that were validated or rejected
Tradeoffs already discussed

ACTIVE TASK STATE
The exact step where the process stopped
What the assistant was about to do next

NEXT ACTION PLAN
Provide a clear step-by-step continuation plan so the next LLM can resume immediately.

ARTIFACTS
Include any generated content that is necessary to continue the task:
prompts, code, outlines, drafts, structured data

POTENTIAL RISKS
List areas where hallucination could occur if context is lost.

INSTRUCTIONS FOR THE NEXT LLM
Write a short directive addressed to the next AI explaining:
how to interpret this context, what to continue doing, what to avoid repeating.

IMPORTANT RULES
Preserve technical details exactly. Do not omit decisions already made.
Avoid narrative explanations. Be concise but information-complete.
Format cleanly so another LLM can ingest this directly.

Return everything inside ONE code block so the user can copy it.
This export must allow another AI to continue the conversation with minimal deviation.
```

**Prompt B (import state, for the receiving model):**

```
You are continuing an existing task. Below is a structured conversation state exported from another LLM.
Treat it as the full context of the project.
Do not restart the task.
Do not repeat completed steps.
Continue from the "ACTIVE TASK STATE".
```

---

## Compaction Handoff (OpenAI Codex CLI style)

*Used when context compacts mid-session and a new LLM takes over internally.*

```
You are performing a CONTEXT CHECKPOINT COMPACTION.
Create a handoff summary for another LLM that will resume the task.

Include:
- Current progress and key decisions made
- Important context, constraints, or user preferences
- What remains to be done (clear next steps)
- Any critical data, examples, or references needed to continue

Be concise, structured, and focused on helping the next LLM seamlessly continue the work.
```

**Summary prefix (prepended for the receiving model):**

```
Another language model started to solve this problem and produced a summary of its thinking process.
You also have access to the state of the tools that were used by that language model.
Use this to build on the work that has already been done and avoid duplicating work.
Here is the summary produced by the other language model, use the information in this summary to assist with your own analysis:
```

---

## Session Handoff with Artifact Validation (little-loops style)

*Deep mode: includes git status, todos, discrepancy detection.*

```
Generate a session handoff with these sections:

## Conversation Summary

### Primary Intent
[What was the user trying to accomplish]

### What Happened
1. [Chronological list of major events]

### User Feedback
- [Key user corrections or preferences stated]

### Errors and Resolutions
| Error | How Fixed | User Feedback |
|-------|-----------|---------------|

### Code Changes
| File | Changes Made | Discussion Context |
|------|-------------|-------------------|

## Resume Point

### What Was Being Worked On
[Precise description]

### Direct Quote
> "Exact last relevant user/assistant message about the task"

### Next Step
[The single next action]

## Important Context

### Decisions Made
- **Decision**: Reasoning

### Gotchas Discovered
- Non-obvious traps found

### User-Specified Constraints
- [Hard requirements]

### Patterns Being Followed
- [Code/approach patterns]

## Artifact Validation (Deep mode)

### Current Git Status
[git status --short output]

### Discrepancies
[Any mismatch between conversation claims and actual file state]

### Todo List State
| Status | Task |
|--------|------|

### Plan Files
- Active plan: [path]
```

---

## Ormus Handoff (multi-machine / multi-project)

*Handles the hard cases: SSH across machines, edits in multiple repos.*

```
Create a HANDOFF.md document at an appropriate location. Use this structure:

## Session Type
[Single-project / Multi-machine / Multi-project / Orchestration]

## Scope
- Machines touched: [list]
- Repos edited: [list with absolute paths]
- Primary working directory: [path]

## What We Were Doing
[2-3 sentence summary]

## State
| What | Status | Notes |
|------|--------|-------|
| [task] | done / in-progress / blocked | [context] |

## Next Steps
1. [Most important action first]

## Key Files
- [absolute paths to files that matter]

## Context to Know
- [Non-obvious facts, gotchas, constraints]

## Resume Prompt
[Copy-pasteable one-liner that bootstraps the next session.
Always uses absolute paths so it works on any machine.]
```

---

## RooCode Handoff System (milestone-based)

*For extended projects: handoffs accumulate into milestones.*

**Handoff trigger prompt:**

```
I need to create a handoff document for our current work. Please:

1. Read the handoff instructions
2. Determine the next sequential handoff number
3. Create a properly structured handoff file with that number
```

**Milestone trigger (after 3-5 handoffs):**

```
I need to create a milestone for our completed work. Please:

1. Read the milestone instructions
2. Determine the next sequential milestone number
3. Create the milestone directory with that number
4. Move all numbered handoff documents into this milestone directory
5. Create the milestone summary and lessons-learned files
```

**When to create handoffs:**
- ~30% irrelevant context accumulated
- After 10+ conversation exchanges
- During debugging sessions exceeding 5 exchanges
- After completing significant work

**When to create milestones:**
- 3-5 handoffs accumulated
- Major project phase completed
- Critical problems solved with valuable lessons

---

## Aspy Continuity Enhancement (compaction injection)

*Inject into the compaction prompt to preserve momentum, not just data.*

```
## Continuity Enhancement

For the summary: To help the continuing AI maintain flow, please include:
- **Active Work Tracks:** What features/bugs/tasks are in progress
- **Key Decisions Made:** Important choices that shouldn't be revisited
- **Current Mental Model:** The user's goals and approach being taken

Post-compaction recovery: Include 3-5 searchable keywords so the next AI
can find relevant conversation history if needed.
```

---

## Sources & Further Reading

### Templates & Blogs
- **Don't Sleep On AI** — "AI Handoff Prompt: The Best 8-Section Continuation Template" (2026) — [dontsleeponai.com/handoff-prompt](https://www.dontsleeponai.com/handoff-prompt) — The most comprehensive structured handoff template
- **JD Hodges** — "Claude Session Handoffs: How to Keep Context Across Conversations" (2026) — [jdhodges.com](https://www.jdhodges.com/blog/ai-session-handoffs-keep-context-across-conversations/) — Two-file system + one-liner handoff
- **Nova Elvaris (DEV Community)** — "The Prompt Handoff Pattern" (2025) — [dev.to](https://dev.to/novaelvaris/the-prompt-handoff-pattern-make-ai-work-survive-session-resets-and-team-handoffs-5bf0) — Clean 6-section handoff
- **yWian** — "Automate Claude Chat Summaries" (2026) — [ywian.com](https://www.ywian.com/blog/automate-claude-chat-summaries) — Auto-summary + automation

### GitHub Repos & Skills
- **sidorovanthon/handoff-prompt** — [github.com](https://github.com/sidorovanthon/handoff-prompt) — ~300 token compact handoff skill for Claude Code, Cursor, Aider, Copilot CLI, Gemini CLI
- **simply-Rahul8/LLM--Checkpoint-Prompt** — [github.com](https://github.com/simply-Rahul8/LLM--Checkpoint-Prompt) — Two-prompt A→B transfer system with ARTIFACTS and POTENTIAL RISKS sections
- **HermeticOrmus/ormus-handoff** — [github.com](https://github.com/HermeticOrmus/ormus-handoff) — Multi-machine/multi-project handoff with 4-path classification (A/B/C/D)
- **robertguss/claude-code-toolkit** — [github.com](https://github.com/robertguss/claude-code-toolkit/tree/main/skills/handoff) — Structured handoff skill with compaction hook companion
- **Michaelzag/RooCode-Tips-Tricks** — [github.com](https://github.com/Michaelzag/RooCode-Tips-Tricks) — Milestone-based handoff system with custom modes
- **badlogic/Context Compaction Research** — [gist.github.com](https://gist.github.com/badlogic/cd2ef65b0697c4dbe2d13fbecb0a0a5f) — Cross-tool compaction research (Claude Code, Codex CLI, OpenCode, Amp)

### Tools & Platforms
- **little-loops** — Session Handoff tool for Claude Code (2026) — [docs.little-loops.ai](https://docs.little-loops.ai/guides/SESSION_HANDOFF/) — `/ll:handoff` and `/ll:resume` commands with deep mode
- **Aspy** — Compaction enhancement proxy — [omgpointless.github.io](https://omgpointless.github.io/aspy/blog/2025/12/the-handoff/) — Injects continuity guidance into Anthropic's compaction prompt
- **Claude Code `/compact`** — Anthropic's built-in context compaction (extracted prompt: [gist by sxalexander](https://gist.github.com/sxalexander/8915f30f8bc97a272620a1a6c67a7148))
- **OpenAI Codex CLI `/compact`** — Codex's compaction with summary prefix ([codex-rs/core/templates/compact/prompt.md](https://github.com/openai/codex/blob/main/codex-rs/core/templates/compact/prompt.md))
- **OpenCode `/compact`** — SST's open-source compaction with prune mechanism ([opencode/src/session/compaction.ts](https://github.com/sst/opencode/blob/main/packages/opencode/src/session/compaction.ts))
- **Amp Handoff** — Sourcegraph's manual handoff + thread references approach ([ampcode.com](https://ampcode.com/guides/context-management))
