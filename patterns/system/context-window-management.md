# Context Window Management Pattern

## Description

Rules for prioritizing, summarizing, and discarding information as context grows.

## When to use

Multi-step agents processing large data or running for extended periods.

## When to avoid

Simple tasks where context never grows large.

## Template

```
Context management rules:

PRIORITIZE (always keep):
- [Critical item 1]
- [Critical item 2]

SUMMARIZE (compress when accumulating):
- After [event], replace [detailed data] with [summary format]

DISCARD (drop when no longer needed):
- [Item type 1] once [condition met]
- [Item type 2] once [condition met]

If context becomes very long, compact oldest items into running counts.
```

## Example

```
Context management rules:

PRIORITIZE (always keep in working context):
- Current task goal and success criteria
- Output file schema
- Sources processed this run (avoid duplicates)

SUMMARIZE (compress when accumulating):
- After processing each source, replace full articles with: 
  "Source: X, Articles: Y, Passed threshold: Z"

DISCARD (drop when no longer needed):
- Raw HTML once content extracted
- Full RSS XML once articles parsed
- Debug output from successful tool calls

If context becomes very long, compact oldest summaries into single count.
```

## Tags

context, memory, optimization, long-running
