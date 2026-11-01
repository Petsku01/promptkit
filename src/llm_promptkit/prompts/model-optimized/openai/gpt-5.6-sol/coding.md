---
category: "model-optimized"
title: "GPT-5.6 Sol: Coding"
subcategory: "openai"
model: "gpt-5.6-sol"
source: "promptkit-authored"
---
# GPT-5.6 Sol: Coding

## Schema-First Business Integration
```
Implement an integration that converts [source records] into [target API schema].

Repository and language: [location and language]
Input examples: [valid, incomplete, and malformed records]
Target contract: [schema and documented error behavior]
Compatibility promises: [existing consumers and supported versions]
Available tools: [file access, shell, patch, and test runner]

Inspect the existing adapters and validation utilities. Specify the mapping for
every target field, explicitly covering null, missing, and empty values. Keep
business normalization separate from serialization and external I/O.
Implement the smallest adapter and contract tests using existing project style.
Test invalid input, unknown enum values, timezone conversion, and retry-safe
handling of [side effect]. Use local fixtures rather than live customer records.

Run the project's checks if tools permit. Return the mapping decisions, changed
files, and actual test outcomes. If no execution environment was provided,
return reviewable code with clearly identified unexecuted checks.
```

## Long-Context Dependency Boundary Review
```
Review [module or service boundary] using this repository evidence packet.

Files and dependency manifest: [attach named source files and lockfiles]
Proposed change: [patch or design]
Public contract: [exports, endpoints, and compatibility constraints]
Retrieval access: [file search tool, if supplied]

Build a dependency map only for paths affected by the proposed change. Locate
callers, serialization boundaries, and configuration defaults; retrieve missing
files when possible rather than guessing from names. Distinguish direct
observations from inferred runtime behavior.

Return concrete regression risks ranked by affected user behavior. For each,
include the relevant file locations, a failing scenario, and a targeted test.
Do not rewrite unaffected modules or pretend to have inspected files outside
the evidence packet. End with a minimal implementation sequence, not a broad
architecture redesign.
```
