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

## Sources & Further Reading

- **Don't Sleep On AI** — "AI Handoff Prompt: The Best 8-Section Continuation Template" (2026) — The most comprehensive structured handoff template
- **JD Hodges** — "Claude Session Handoffs: How to Keep Context Across Conversations" (2026) — Two-file system (CLAUDE.md + HANDOVER.md) + handoff prompts
- **Nova Elvaris (DEV Community)** — "The Prompt Handoff Pattern" (2025) — Clean 6-section handoff structure
- **yWian** — "Automate Claude Chat Summaries for Seamless Conversation Continuity" (2026) — Auto-summary + new chat automation
- **little-loops** — Session Handoff tool for Claude Code (2026) — `/ll:handoff` and `/ll:resume` commands
- **Claude Code `/compact`** — Anthropic's built-in context compaction system (source: GitHub Gist by sxalexander)
