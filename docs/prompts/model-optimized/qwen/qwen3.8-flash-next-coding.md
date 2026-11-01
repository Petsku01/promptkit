---
category: "model-optimized"
title: "Qwen3.8-Flash-Next: Coding"
subcategory: "qwen"
model: "qwen3.8-flash-next"
source: "promptkit-authored"
---
[← Back to Model-Optimized Qwen](../index.md)

# Qwen3.8-Flash-Next: Coding

## Latency-Budgeted Agent Patch
```
Resolve this repository issue within a bounded tool workflow.
Issue: [description]
Repository: [path]
Maximum tool rounds and runtime: [budget]
Acceptance test: [command and expected behavior]

Inspect the likely fault boundary and neighboring tests before changing code. Batch independent reads, but serialize dependent edits and checks. Choose the next tool call by information gain; do not sacrifice a necessary diagnosis just to shorten an individual response. Stop repeating a failing approach after the same evidence recurs.

Implement and exercise the smallest correct patch. Return actual test output, changed files, tool rounds consumed if measurable, and any criterion left unverified. Do not claim a latency gain without measurement.
```

## Screenshot-to-Working Application Slice
```
Implement the application slice represented by this reference screenshot.
Reference image: [attachment]
Existing stack: [repository and framework]
Required interactions and data contract: [specification]

Extract a component and interaction inventory from the image, explicitly marking behavior that is specified in text rather than visible. Build a functioning vertical slice using existing project patterns, then verify interactions and responsive rendering with available tools. Preserve semantic HTML and keyboard accessibility.

Deliver the runnable slice, the commands actually used to check it, and remaining mismatches. Never substitute a static mock for an interaction required by the contract.
```
