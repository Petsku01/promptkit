---
category: "code"
title: "Executable Implementation Plans with Explicit Interface Contracts"
source: "obra/superpowers; wshobson/agents"
license: "MIT"
---
# Executable Implementation Plans with Explicit Interface Contracts

**Category:** code
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-plans/SKILL.md (MIT)
**Secondary source:** Adapted from https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/plugins/conductor/commands/new-track.md (MIT); bounded feature/bug intake and separate specification approval only.

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [Superpowers notice](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).
Copyright (c) 2024 Seth Hobson. Full permission and warranty notice: [wshobson/agents notice](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--wshobsonagents-mit).

## When to Use

Turn an approved specification into independently reviewable implementation tasks with exact interfaces, test assertions and verification commands. A planning request does not authorize implementation or execution.

## The Prompt

```text
Write an implementation plan that an engineer unfamiliar with the repository can
execute without inventing requirements, file locations or cross-task interfaces.
Inputs: [approved specification and approval reference]
Repository scope: [checkout, revision and relevant subsystems]
Output: [approved plan path or response-only]
Constraints: [global requirements and planning permissions]

1. Confirm a specification exists and is approved. If the input is only an idea
   or bug report, use bounded intake, not implicit design authorization. For a
   feature, collect intended users, outcome, acceptance criteria, dependencies
   and exclusions. For a bug, collect reproduction, expected versus actual
   behavior, affected versions/areas and any explicitly unconfirmed cause theory.
   Ask only unanswered decision-changing questions, at most six in one intake
   pass. In a non-interactive setting, list these gaps and stop at a draft spec.
   Present the specification for separate approval before generating a definitive
   implementation plan; do not treat silence or a request to plan as spec approval.
2. Read the approved specification and actual repository conventions. Inspect
   relevant source, tests, configuration, dependency/version files and documented
   build commands. Record the revision inspected. Locate existing implementations
   and helpers before proposing new ones. Preserve exact values and identifiers
   from the spec. Distinguish observed APIs from proposed new interfaces. Never
   invent existing paths, line ranges, dependency methods or test-runner options;
   omit unverifiable line ranges and identify unresolved APIs as blockers.
3. Map acceptance requirements to deliverables before numbering tasks. Identify
   the files to create, modify and test, with each file's responsibility. Reuse
   established organization and avoid unrequested restructuring. If independent
   subsystems deserve separate plans, explain the boundary and shared interface
   rather than producing an inseparable mega-task. Fold setup and documentation
   into the deliverable they support; each task should have a meaningful review
   gate and an independently testable result, not just scaffolding.
4. Start the plan with goal, approved-spec reference, inspected revision,
   architecture summary, relevant toolchain and global constraints. Copy binding
   requirements with their exact values. List unresolved decisions and who must
   decide them; do not convert uncertainty into a made-up default. Add review
   focus based on actual implied failure modes, not a forced quota of five risks.
   An empty risk section must mean the assessment found none worth highlighting,
   not that review was skipped. Link each identified risk to a test-owning task.
5. Give every task this explicit contract:
   - Purpose and acceptance requirement IDs; prerequisites and dependency order.
   - Files: exact create/modify/test paths, labeled observed or proposed.
   - Consumes: exact function/method signatures, parameter and return types,
     data shapes, error behavior and configuration keys supplied by earlier work
     or existing code. State “none” when genuinely independent.
   - Produces: exact public names/signatures, types, invariants and artifacts
     that later tasks may rely on. Define proposed types before referencing them.
   - Tests: test names and concrete assertion code with approved expected values,
     including relevant boundaries, invalid inputs, failure and recovery paths.
   - Steps: one action and checkable outcome each; verification commands with
     working directory, prerequisites and expected exit/status/assertion results.
6. For each behavior change, plan a failing regression/acceptance test first,
   the exact focused command to demonstrate the intended baseline failure,
   minimal implementation against the declared interface, and the command to
   demonstrate passing behavior. State why the expected baseline failure is
   meaningful; a missing dependency or syntax error is not necessarily the right
   red test. Add integration and broader-suite checks appropriate to changed
   contracts. For non-code deliverables, specify their actual validation rather
   than inventing a unit-test cycle. Keep bodies out of the plan unless a required
   algorithm or exact mandated copy cannot be specified by signatures and tests.
7. Check cross-task names, types and dependency order for consistency. A later
   task must not consume an undefined helper or silently change an earlier
   return type. Build a requirement-to-task/test matrix and identify gaps.
   Distinguish an undecided product requirement from an implementer's local
   choice. Do not fill important gaps with “handle edge cases,” vague TBDs or
   speculative APIs; mark the affected task blocked pending a specific decision.
   Self-review for both ambiguity and excessive implementation transcription.
8. Save only the requested planning document if a path is authorized; otherwise
   return it in the response. Use the project's normal plan location, not a
   mandatory vendor directory or worktree. An isolated worktree may be considered
   during later execution but is not a dependency for writing this plan. Do not
   create Conductor setup, tracking metadata or duplicate specification templates.
   Do not edit code, run test/build/install commands, launch implementation,
   create branches, commit or push from a planning-only request. Repository
   inspection may use read-only commands within the stated permissions.

Return the plan, coverage matrix, decision blockers and a separate request for
plan review/approval before execution. Keep all steps unchecked. Commands and
expected results in a plan are prospective assertions, never evidence that a
command ran or a test passed. Identify any genuine pre-existing execution logs
separately with their revision and provenance; do not fabricate verification.
```

## How It Works

Bounded intake establishes what may be planned, while separate specification and plan gates prevent accidental execution. Explicit consumed/produced contracts carry decisions across task boundaries without copying whole implementations.

## Variables

- `[approved specification and approval reference]`: accepted behavioral source of truth.
- `[checkout, revision and relevant subsystems]`: inspection target and scope.
- `[approved plan path or response-only]`: only permitted planning artifact destination.
- `[global requirements and planning permissions]`: exact constraints and read/write limits.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
