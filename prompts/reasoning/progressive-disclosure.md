# Progressive Disclosure Pattern

**Use case:** Complex multi-phase workflows

**Pattern:** Progressive Disclosure

---

## Quick Version (~100 tokens)

```
PHASED EXECUTION:

Phase 1 — TRIAGE: Quick scan and prioritize
Phase 2 — DEEP: Detailed analysis of top items only
Phase 3 — OUTPUT: Finalize selected items

Complete each phase before starting next.
```

---

## Extended Version (~400 tokens)

```
PROGRESSIVE DISCLOSURE PROTOCOL:

Break complex tasks into phases. Complete Phase N before reading Phase N+1 instructions.

PHASE 1 — TRIAGE:
Objective: Quick sorting to identify worthiest items

Instructions:
- Scan all input items rapidly
- Assign rough relevance score (1-10) based on title/summary
- Sort by score descending
- Select top 20 items for Phase 2
- Discard or summarize the rest
- Save Phase 1 results to /tmp/phase1-results.json

STOP HERE. Do not proceed to Phase 2 yet.

PHASE 2 — DEEP ANALYSIS:
Objective: Detailed evaluation of top 20 items

Instructions:
- Read full content of each top-20 item
- Apply detailed scoring rubric (see /docs/scoring-rubric.md)
- Mark each as: PUBLISH, REVISE, or SKIP
- For REVISE items: note required changes
- Save Phase 2 results to /tmp/phase2-results.json

STOP HERE. Do not proceed to Phase 3 yet.

PHASE 3 — OUTPUT GENERATION:
Objective: Produce final deliverables

Instructions:
- For PUBLISH items: generate final output following format specs
- For REVISE items: apply noted changes, then generate output
- For SKIP items: log reason in /logs/skipped.json
- Assemble final deliverable
- Verify output against checklist

PHASE TRANSITION RULES:

1. Only proceed to next phase when current phase is COMPLETE
2. "Complete" means all items processed and results saved to disk
3. If interrupted, resume from last completed phase using saved results
4. Never skip ahead — phases build on each other

WHY THIS WORKS:

- Prevents cognitive overload by limiting active instruction set
- Forces completion before advancement (no half-done accumulation)
- Allows resumption if interrupted
- Reduces context bloat (only Phase N instructions active)

COLLAPSE PREVENTION:

Without explicit phase gating, agents tend to:
- Start deep analysis while still triaging
- Begin output generation before analysis complete
- Mix phases, causing inconsistent quality

Phase transitions are hard boundaries. Respect them.
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** workflow, phases, complexity, organization
- **Models:** All
- **Version:** 1.0
