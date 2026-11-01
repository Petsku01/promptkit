---
category: "model-optimized"
title: "DeepSeek V4.1 Flash 1017: Coding"
subcategory: "deepseek"
model: "deepseek-v4.1-flash-1017"
source: "promptkit-authored"
---
# DeepSeek V4.1 Flash 1017: Coding

## Harness-Verified Repository Fix
```
Complete this repository task with the tool-enabled coding harness.
Task: [issue]
Working tree: [path]
Authorized scope: [files and operations]
Acceptance commands: [commands]

Inspect the current implementation and failing behavior, then produce a focused patch with a regression test. Use real tool output to decide whether a failure is environmental or caused by the patch. Avoid verbose restatement between tool calls; carry forward a compact record of observations and next checks.

Run the acceptance commands where possible. Report the root cause, patch, exact commands and outcomes, and any remaining blocker. Do not emit invented terminal output or imply a tool was called when it was not.
```

## Visual Bug to Backend Boundary
```
Diagnose and repair the defect shown in this application screenshot.
Screenshot: [attached image]
Expected behavior: [description]
Relevant frontend/backend repository: [path]
Observed request or console logs: [logs]

Trace the visible symptom through component state, request serialization, and the service contract. Use the screenshot to locate the failure but validate the causal explanation against source and runtime evidence. Add a test at the boundary that actually caused the defect, not only a screenshot snapshot.

Deliver the code change and a concise evidence trail connecting the visible symptom to the tested correction. Mark rendering checks separately from service and unit tests.
```
