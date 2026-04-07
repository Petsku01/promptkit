# Memory Integration Pattern

**Use case:** Persistent state across agent sessions

**Pattern:** Memory Integration

---

## Quick Version (~100 tokens)

```
MEMORY PROTOCOL:

START:
Read /memory/state.json for context from previous runs

DURING:
- Avoid repeating topics in /memory/used-topics.json
- Skip sources with reliability < 0.5
- Learn from /memory/failed-approaches.json

END:
Append new topics, update reliability scores, log failures
```

---

## Extended Version (~450 tokens)

```
MEMORY SYSTEM:

Your context resets between runs. Use persistent memory files to maintain continuity.

READ AT START (before any action):

1. /memory/session-state.json
   Contains: task queue, partial progress, interrupted actions
   Purpose: Resume from where previous run left off

2. /memory/topic-history.json
   Contains: Topics covered in last 30 sessions
   Purpose: Avoid repetition
   Rule: If current topic in this list, check recency. If < 7 days, skip or find new angle.

3. /memory/source-reliability.json
   Contains: Scores (0.0-1.0) for each data source
   Purpose: Prioritize reliable sources
   Rule: Skip sources with score < 0.5

4. /memory/failed-approaches.json
   Contains: Recent failures with context
   Purpose: Don't repeat failed strategies
   Rule: If current approach matches failed entry within 7 days, try alternative

WRITE AT END (after successful completion):

1. Update topic-history.json with main topics from this run

2. Update source-reliability.json:
   - If source provided usable data: +0.1 (max 1.0)
   - If source failed or provided 0 usable items: -0.1 (min 0.0)

3. If run encountered failures:
   Append to failed-approaches.json with:
   {
     "timestamp": "ISO8601",
     "approach": "what was tried",
     "failure": "what went wrong",
     "context": "relevant conditions"
   }

4. Update session-state.json:
   - Clear completed items
   - Preserve incomplete items for next run
   - Save current timestamp

MEMORY FILE CORRUPTION:

If any memory file is missing or unreadable:
- Create blank version with minimal structure
- Log "memory_rebuilt: [filename]" 
- Continue with empty state
- Never halt due to memory issues

MEMORY ISolation:

- Read memory files ONCE at start
- Write memory files ONCE at end
- Do NOT re-read during execution (stale data is acceptable within a run)
- Do NOT update memory incrementally (causes race conditions)
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** memory, persistence, state, multi-session
- **Models:** All
- **Version:** 1.0
