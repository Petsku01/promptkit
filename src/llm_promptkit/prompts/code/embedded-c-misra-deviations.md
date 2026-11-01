---
category: "code"
title: "Safety-Critical Embedded C Review and MISRA Deviation Drafts"
source: "github/awesome-copilot"
license: "MIT"
---
# Safety-Critical Embedded C Review and MISRA Deviation Drafts

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/expert-embedded-c-engineer.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit). This adaptation does not reproduce or grant rights to MISRA standards text.

## When to Use

Review embedded C against the actual target, compiler and safety process, producing evidence-based findings and deviation drafts for qualified human review rather than compliance or certification claims.

## The Prompt

```text
Review this embedded C change for correctness, defensive behavior and alignment
with the project's authorized coding-standard process. Deliver review findings
and proposed deviation records, not a compliance certificate.
Target code: [checkout, revision, modules and generated-code boundaries]
Build context: [C dialect, compiler/version, MCU, RTOS and build commands]
Safety context: [applicable standards editions, authorized references and process]
Authorization: [analysis tools, test hardware, local edits and approval owners]

1. Discover actual project constraints before prescribing code. Read build files,
   compiler flags, linker settings, target configuration, coding conventions and
   existing analysis/deviation records. Establish C dialect and extensions, integer
   widths, alignment, endianness, memory map, stack/heap limits and interrupt/task
   model. Do not impose C99 or a newer dialect over the existing standard. Confirm
   unfamiliar pragmas and compiler behavior against version-matched vendor docs.
   Record unknown constraints and block conclusions that require them.
2. Identify the applicable safety lifecycle, standard edition/amendments, project
   rule classifications, analysis configuration and approval authority. Verify every
   cited MISRA rule identifier and classification against authorized references for
   that edition; do not invent numbers or copy MISRA text verbatim. Summarize the
   code-specific concern in your own words. If references are unavailable, label
   the concern a general C finding with rule mapping unverified. The source prompt's
   MIT license is not permission to reproduce proprietary standards. Do not claim
   compliance, certification or a completed safety assessment from this review.
3. Trace data and control flow at module boundaries and safety-relevant internal
   paths. Check pointer lifetime, ownership, nullability, alignment and aliasing;
   array bounds and length arithmetic; signedness, narrowing, shifts, overflow and
   integer promotions; initialization, unreachable/error paths and side effects
   in macros. Evaluate const qualification and internal linkage without changing
   public ABI. Use project-compatible types and explicit conversions only when
   their ranges are justified, not casts that merely silence diagnostics.
4. Inspect concurrency and hardware interactions. Review volatile accesses against
   compiler/MCU guarantees; volatile alone is not atomicity or synchronization.
   Check interrupt/task shared state, critical sections, ordering, reentrancy,
   peripheral register semantics and watchdog servicing. Consider worst-case
   execution time and stack use where evidence exists; do not invent timing bounds.
   Preserve required reads/writes and barriers. Separate host-test evidence from
   target behavior that requires hardware or simulator validation.
5. Evaluate defensive checks using the hazard and fault model, not a blanket rule
   that all internal inputs are trusted. Trace corruption, concurrency and invalid
   state paths before removing checks. Distinguish development assertions from
   required production diagnostics and safety mechanisms. Never blindly compile
   out bounds, plausibility, watchdog or fault checks to improve speed or reduce
   warnings. Establish deterministic error propagation and defined safe reactions.
   Use AUTOSAR DEM/DTC reporting and Std_ReturnType only if this project actually
   uses the relevant AUTOSAR interfaces; otherwise follow its established error API.
6. Preserve generated-code boundaries, including RTE/MCAL/vendor files. Recommend
   a generator-input change or documented issue rather than hand-editing generated
   output. Do not change optimization, warning policy, linker script, target settings
   or analyzer suppressions without explicit approval. Inspect existing suppression
   syntax and scope; never globally disable a diagnostic to erase one finding.
   Default to findings and patch suggestions, making local edits only if authorized.
7. For each finding, provide source location, observed behavior, triggering condition,
   possible hazard, evidence, severity and narrow remediation. Distinguish confirmed
   defects, analyzer candidates, accepted project deviations and unresolved concerns.
   Draft deviations only where the process permits them: record verified rule ID,
   edition, affected scope, necessity, rejected alternatives, risk assessment,
   compensating controls, verification evidence, residual risk, expiry/review trigger
   and required approver. Leave approval pending; no agent signature substitutes
   for the designated authority. A nondeviable requirement remains a blocker.
8. Run the existing build and configured static analysis within authorization.
   Preserve baseline diagnostics and compare scoped changes without weakening
   tests. Use boundary, invalid-input, fault-injection and concurrency tests where
   safe; hardware actions require approved equipment and safe-state controls.
   Record tool versions, commands, exit statuses and target configuration. New
   source files proposed for implementation need explicit build integration.
   Missing proprietary tools, licensed references or hardware means verification
   is incomplete, not clean. Recheck related call sites for the same defect while
   keeping unrelated redesign outside scope.

Return context/assumptions, ranked findings, verified and unverified rule mappings,
deviation drafts awaiting approval, actual build/analysis/test results, generated-
code constraints and remaining safety-owner decisions. State precisely what was
reviewed and what was not verified; never infer system safety from zero warnings.
```

## How It Works

Target discovery prevents inappropriate language or hardware assumptions. Findings remain separate from rule mappings and deviation approvals, preserving both licensing boundaries and the project's human safety authority.

## Variables

- `[checkout, revision, modules and generated-code boundaries]`: exact review scope.
- `[C dialect, compiler/version, MCU, RTOS and build commands]`: actual build/target constraints.
- `[applicable standards editions, authorized references and process]`: valid rule-mapping basis.
- `[analysis tools, test hardware, local edits and approval owners]`: execution and approval limits.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
