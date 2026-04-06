# Tool Selection Heuristics Pattern

## Description

Explicit priority rules for when to use each tool — prevents expensive or risky tool misuse.

## When to use

Agents with multiple tools where cost, latency, or risk varies between options.

## When to avoid

Single-tool agents or when all tools have similar cost/risk profiles.

## Template

```
Tool selection rules (follow in priority order):

1. [CHEAPEST/SAFEST OPTION FIRST]
   Use when: [condition]
   
2. [NEXT OPTION]
   Use when: [condition]
   
3. [MOST EXPENSIVE/RISKY LAST]
   Use when: [condition]
   Cost: [estimate]

NEVER use [FORBIDDEN TOOL] for [SCOPE]
```

## Example

```
Tool selection rules (follow in priority order):

1. READ LOCAL CACHE FIRST
   Use when: data might exist in /cache/ or /sources.json
   
2. USE CACHED RSS DATA
   Use when: scraper ran within 8 hours
   
3. WEB SEARCH
   Use when: (a) local source missing info, (b) verification needed
   Cost: ~$0.002 per call

NEVER use EMAIL or SOCIAL tools during content generation
```

## Tags

tools, heuristics, cost-optimization, selection
