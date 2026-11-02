---
category: "model-optimized"
title: "Qwen3.8-Flash-Next: Analysis"
subcategory: "qwen"
model: "qwen3.8-flash-next"
source: "promptkit-authored"
---
[← Back to Model-Optimized Qwen](../index.md)

# Qwen3.8-Flash-Next: Analysis

## Strata Evidence Layering
```
Organize this long-context investigation into evidence strata.
Question: [question]
Materials: [ID-labeled documents, tables, and attached images]
Required output budget: [length]

Layer 1: directly observed facts with source IDs or image regions.
Layer 2: relationships supported by multiple independent observations.
Layer 3: tentative hypotheses and the observations needed to test them.

Keep contradictions visible between layers. Use the full supplied context to detect distant references, but do not assume that an unquoted fact was retrieved correctly. For chart-derived quantities, verify labels and scales before performing calculations with tools.

Return the layered evidence map and a brief answer whose certainty does not exceed its strongest supporting layer.
```

## Long-Video Event Audit
```
Audit the supplied video for [events or interaction failures].
Video: [attachment]
Event definitions: [observable criteria]
Sampling metadata, if available: [frame rate and timestamps]

Create an event timeline from visible evidence. Distinguish exact observations from intervals whose timing is limited by frame sampling. Correlate events with the supplied log excerpts [logs], without treating temporal proximity alone as causation. Ask for denser sampling where an important transition is not visible.

Output event, timestamp or interval, visual evidence, matching log ID, and uncertainty. State whether the available video coverage is sufficient for the requested conclusion.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
