---
category: "model-optimized"
title: "Claude Opus 4.8: Coding"
subcategory: "anthropic"
model: "claude-opus-4.8"
source: "promptkit-authored"
---
# Claude Opus 4.8: Coding

## Autonomous Change with Explicit Scope
```
Complete [engineering task] in [repository].

Full requirements: [behaviors and edge cases]
Editable paths: [allowlist]
Public contracts to preserve: [APIs, schemas, and supported platforms]
Verification commands: [tests, type checks, and UI checks]
Allowed tools and approval limits: [execution environment and side effects]
Delegation limit: [maximum workers, or none]

Read repository guidance and inspect the affected paths. Apply every acceptance
criterion across all affected components; do not assume a requirement applies
only to the first file mentioned. Use tools to inspect runtime assumptions and
run checks instead of relying solely on extended reasoning.

Work autonomously within the stated boundaries. Delegate only independent
investigations with explicit outputs if workers are actually available; keep
small local edits in the main task. Never assign overlapping file ownership.
For frontend work, use the supplied design tokens [palette, typography, spacing]
throughout rather than choosing a default editorial theme.

Implement, execute the checks, and resolve failures attributable to the change.
Return a concise delivery note with evidence for each acceptance criterion,
remaining limitations, and any actions requiring approval. Do not deploy.
```

## Coverage-First Defect Discovery
```
Review [patch or component] for behavioral defects.

Source and call sites: [files]
Expected behavior: [contract]
Discovery scope: [paths and categories of defects]
Verification tools: [tests and execution tools, if available]

Investigate all supplied paths for incorrect results, unsafe state transitions,
resource leaks, and compatibility breaks. During discovery, retain plausible
low-severity and low-confidence findings as candidates rather than silently
filtering them. Exclude pure naming and formatting preferences.

Then validate each candidate against actual control flow and, where possible,
a targeted test. Keep confirmed defects separate from unverified concerns;
discard candidates contradicted by evidence with a short reason.

For every retained finding provide a location, triggering input or sequence,
expected versus actual behavior, severity, confidence, and verification status.
Rank findings only after discovery. Do not equate a narrow reporting threshold
with permission to skip investigating the rest of the component.
```
