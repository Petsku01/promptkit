---
category: "model-optimized"
title: "Kimi K2.7 Code: Coding"
subcategory: "moonshot"
model: "kimi-k2.7-code"
source: "promptkit-authored"
---
[← Back to Model-Optimized Moonshot](../index.md)

# Kimi K2.7 Code: Coding

## Stateful MCP Engineering Loop
```
Implement this engineering task using the available repository and MCP tools.
Task: [task]
Tool permissions: [read/write scope and prohibited actions]
Completion criteria: [criteria]

Inspect tool schemas and the existing implementation first. Work in a bounded inspect-edit-test loop; use each actual tool result to choose the next operation. Keep decisions already established in earlier turns stable unless new evidence contradicts them. Never manufacture a tool response or repeat a failed operation without changing a relevant input.

Finish with a working patch and executed checks. Report tool failures separately from code failures, and identify any acceptance criterion that could not be exercised.
```

## Visual Regression to Executable Test
```
Fix the UI regression visible in this screenshot or video.
Visual evidence: [attachments and relevant timestamps]
Expected interaction: [steps]
Frontend repository and test runner: [details]

Locate the responsible components and translate the visible failure into an executable interaction test. Check behavior at the affected breakpoint and keyboard navigation, not only static appearance. Use a browser or rendering tool if available to verify the correction against the supplied visual evidence.

Return the implementation change, regression test, and observed verification result. Avoid unrelated restyling. If only sampled video frames are available, do not infer unobserved interactions.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
