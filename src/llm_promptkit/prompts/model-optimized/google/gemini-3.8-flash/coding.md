---
category: "model-optimized"
title: "Gemini 3.8 Flash: Coding"
subcategory: "google"
model: "gemini-3.8-flash"
source: "promptkit-authored"
---
# Gemini 3.8 Flash: Coding

## Media-to-Regression-Test Engineering
```
Fix the defect demonstrated in [screen recording or image sequence].

Media and timestamps: [attachments and relevant intervals]
Repository and runtime: [location, stack, and startup command]
Expected interaction: [user journey and correct behavior]
Allowed paths and tools: [edit scope, shell, patch, and browser tools]
Verification budget: [maximum test cycles or time]

Read the visual evidence and map each observable interaction to a likely code
path. Separate the visible failure from hypotheses about its cause. Inspect
handlers, state transitions, and network boundaries before choosing a patch.
Use the actual repository tools to reproduce the failure where possible.

Add a regression test matching the demonstrated sequence, including timing or
ordering conditions. Implement the smallest correction, run the test, and
exercise the same journey in the browser if a browser tool is supplied.
Stop repeating an unsuccessful tool strategy after new output stops providing
evidence; explain the blocker and the next discriminating check instead.

Return the observed defect, root-cause evidence, changed paths, and real test
results. If no execution tools were supplied, mark the patch as unverified.
```

## Stateful Gemini Function-Calling Migration
```
Migrate [application integration] to gemini-3.8-flash.

Existing client and SDK version: [code and lockfile]
Function declarations and handlers: [schemas and implementations]
Conversation persistence: [storage design]
Safe test commands: [commands]

Check the current vendor API contract before editing. Replace legacy thinking
budgets with a supported thinking level. For the Interactions API, use the
server-side previous_interaction_id pattern. If the application intentionally
retains generateContent, preserve thought signatures and validate that every
FunctionResponse has the required call_id and name for the documented version.
Do not fabricate or rewrite opaque signatures.

Remove unsupported prefilled model turns and audit obsolete sampling parameters.
Test a two-turn function workflow with a sandboxed handler, a failed handler,
and resumed conversation state. Keep multimodal function assets in the response
payload rather than losing them during text serialization.

Return the API path chosen, migration changes, and executed contract-test results.
```
