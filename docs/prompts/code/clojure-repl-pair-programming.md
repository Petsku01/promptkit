---
category: "code"
title: "REPL-First Clojure Pair Programming and Structural Refactoring"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# REPL-First Clojure Pair Programming and Structural Refactoring

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/clojure-interactive-programming.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Develop or refactor Clojure interactively in an explicitly approved development REPL, then prove the saved implementation works independently of exploratory REPL state.

## The Prompt

```text
Pair-program this Clojure change using small, observable REPL experiments before
editing implementation files.
Task and behavior contract: [requested change and preserved behavior]
Approved environment: [development REPL identity, project and namespace]
Editing capability: [structural-edit tool and file scope]
Validation: [test commands, fixtures and resource/time limits]

1. Establish the safety boundary first. Verify the connected REPL is the approved
   development instance, its working directory, classpath, aliases and active
   namespace. Confirm structural-edit tooling is available for Clojure forms.
   If either prerequisite is missing, stop evaluation/implementation and report
   the missing capability; do not silently substitute text replacements. Never
   evaluate production-side-effecting forms, even as a quick diagnostic. Inspect
   namespace initialization, macros and library startup hooks before loading:
   require and reload can themselves execute effects. Use approved isolated
   fixtures rather than real payments, messages, remote writes or production data.
2. Read the complete relevant source and tests, plus dependency/configuration
   files that govern the target namespace. Identify public behavior, callers,
   mutation boundaries and existing idioms. Reproduce current behavior with
   bounded representative data. For a bug, run the failing test or extract its
   smallest fixture; record expected and actual results before proposing a fix.
   Redact sensitive values in shared evaluations and output.
3. Develop from subexpressions upward. Evaluate data shapes and transformations
   in the correct namespace, introducing a clearly named temporary candidate
   only when necessary. Prefer pure functions taking explicit arguments and
   returning data; use destructuring and namespaced keywords when consistent
   with the repository. Do not flatten domain structures or change keyword
   conventions merely to satisfy a stylistic preference. Explain important
   experiments with their namespace, expression, observed value and interpretation.
4. Investigate failures before changing architecture. Read the full exception
   and relevant stack frames, check argument shapes, namespace aliases, loaded
   library versions and framework contracts. Separate incorrect business logic
   from stale REPL state or unavailable infrastructure. Global atoms, managed
   state and mocks are not automatically architectural defects: assess ownership,
   lifecycle, concurrency and testability. Propose a functional-core boundary
   only when it addresses a demonstrated problem within this change's scope.
5. Make infrastructure failure explicit. Do not hide a wrong endpoint or failed
   initialization behind an unexplained hardcoded default. A documented cache,
   bounded retry or degraded-mode fallback can be legitimate resilience when its
   trigger, safety limits, observability and recovery behavior are specified.
   Preserve such contracts and test both healthy and fallback paths rather than
   banning every fallback. Stop if safe isolated evaluation cannot be established.
6. Validate the candidate against the behavior contract. Include nil, empty
   collections, boundary numbers, malformed inputs, lazy realization, ordering,
   exceptions and relevant concurrency cases. Compare original and candidate
   results with deterministic fixtures, realizing lazy values only within the
   agreed bounds. Matching sample results supports those cases, not all-input
   equivalence. Use regression and property-based tests where appropriate;
   retain existing edge cases and assertions instead of weakening tests to pass.
7. Apply the smallest change with structural editing. Preserve balanced forms,
   metadata, comments, docstrings and namespace declarations. Put function
   docstrings after the function name. Respect symbol resolution at compilation:
   forward references may require declare; aliases, qualified symbols and
   namespace loading affect resolution. Do not claim every function must always
   be physically defined before every use. Check macros and cyclic dependencies
   separately instead of adding declarations blindly.
8. Reload the edited namespace from disk using the repository's safe reload
   process, then rerun focused tests and the applicable suite/linter. Reload
   dependent namespaces when necessary; removed Vars can survive ordinary reload,
   so use a fresh approved process when stale state could mask errors. Verify
   behavior is file-backed, not only a temporary defn in the REPL. Remove only
   temporary definitions and fixtures you introduced, without disrupting shared
   development state. Report blockers rather than inventing passing results.

Return changed files, the reasoning behind the minimal change, important REPL
observations, and a validation ledger. Separate REPL-only experiments from
reloaded-file checks and fresh-process tests. Include exact commands, actual
results, warnings, skipped checks and remaining behavioral uncertainty.
```

## How It Works

The read–evaluate–compare–structurally edit–reload loop keeps exploration cheap while explicitly separating transient REPL success from saved-code validation. Safety gates cover namespace loading as well as obvious write calls.

## Variables

- `[requested change and preserved behavior]`: bug or refactor contract and invariants.
- `[development REPL identity, project and namespace]`: authorized non-production target.
- `[structural-edit tool and file scope]`: available form-aware editor and allowed files.
- `[test commands, fixtures and resource/time limits]`: executable checks and evaluation bounds.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: refusal |
