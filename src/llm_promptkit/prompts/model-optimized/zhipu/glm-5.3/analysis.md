---
category: "model-optimized"
title: "GLM-5.3: Analysis"
subcategory: "zhipu"
model: "glm-5.3"
source: "promptkit-authored"
---
# GLM-5.3: Analysis

## Tool-Verified Operational Diagnosis
```
Diagnose this operational problem using the available text and tools.
Symptom: [description]
Environment: [system and service details]
Allowed diagnostic tools: [tools]
Operational restrictions: [read-only boundaries and approval rules]

Begin with read-only checks that distinguish service state, configuration, and dependency failures. Inspect tool schemas before calling unfamiliar functions. Keep a finding ledger that ties every state claim to a specific observation and time. Treat an empty result or timeout as a failed observation, not proof that a component is absent.

Return the most likely fault boundary, verified facts, unresolved hypotheses, and the next safe diagnostic action. Do not change production state during analysis.
```

## Structured Long-Horizon Work Audit
```
Audit completion of this multi-stage agent assignment.
Original acceptance checklist: [checklist]
Execution record: [text logs, artifacts, tool responses]
Read-back tools: [available tools or none]

Match each acceptance item to an artifact and a verification result. Where a tool call reported success, check the exact target through a read-back tool if available. Distinguish attempted, written, verified, and blocked states. Do not count a plausible narrative as an artifact.

Return JSON only with keys completed, unverified, blocked, and recommended_next_action. Each item must include criterion_id and evidence_reference; use null when evidence is missing. Do not invent references to satisfy the output shape.
```
