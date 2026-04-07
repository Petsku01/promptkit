# Context Window Management

**Use case:** Managing long-running agent sessions

**Pattern:** Context Window Management

---

## Quick Version (~100 tokens)

```
CONTEXT RULES:

KEEP (always):
- Current task goal
- Output schema
- List of completed items

SUMMARIZE:
- Replace processed data with summaries
- Compress old conversation to key points

DISCARD:
- Raw HTML/XML after extraction
- Debug output from completed steps
- Duplicate information
```

---

## Extended Version (~400 tokens)

```
CONTEXT MANAGEMENT PROTOCOL:

Your context window is finite. Manage it actively to maintain reasoning quality.

TIER 1 — ALWAYS RETAIN (highest priority):
- Current task goal and success criteria
- Output schema/format requirements
- List of sources/items already processed (avoid duplication)
- Active HALT-level errors (don't lose critical failures)
- Guard rails and hard constraints

TIER 2 — SUMMARIZE WHEN LONG:
After processing each major item, replace with compact summary:

BEFORE:
"Raw article text: 500 words about AI safety..."

AFTER:
"Article: [title] | Source: [url] | Relevance: 8/10 | Status: processed"

When context exceeds ~50K tokens, aggressively compress Tier 2 items.

TIER 3 — DISCARD IMMEDIATELY AFTER USE:
- Raw HTML from web fetches (keep extracted content only)
- Full RSS/XML feeds after parsing
- Debug/trace output from successful tool calls
- Temporary calculation results (keep final only)
- Example code that has been executed

COMPRESSION STRATEGIES:

1. Rolling Summary: After every 5 items, compress individual summaries into aggregate: "Processed 5 sources, found 3 relevant, 0 failed."

2. Reference by ID: Instead of repeating full content, reference by ID: "See item #12 above."

3. Key-Value Extraction: For structured data, keep only relevant fields:
   FROM: Full JSON object with 20 fields
   TO: {id: X, status: Y, result: Z}

COMPACTION TRIGGERS:
- Context exceeds 75% of limit
- Processing slows noticeably
- Model responses become less coherent

When triggered: pause, compact all Tier 2/3 items, resume.
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** context, memory, optimization, long-running
- **Models:** All
- **Version:** 1.0
