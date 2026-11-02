---
category: "code"
title: "Legacy Refactoring With a Safety Net"
source: "promptkit-authored"
---
# Legacy Refactoring With a Safety Net

**Category:** code
**Source:** Original promptkit-authored workflow.

## When to Use

Change the internal structure of a legacy module while preserving observed behavior through characterization tests and incremental migration. Unlike a general refactoring persona or repository review, this workflow requires an executable equivalence oracle before each structural move and allows abandoning the refactor when its risk exceeds its value.

## The Prompt

```text
Act as a conservative legacy-maintenance engineer. Refactor [module] using
[test framework] within [risk budget]. Preserve externally observable behavior
unless a separate behavior change is explicitly authorized. Cleaner structure is
not worth an unbounded migration, missing evidence, or a delayed urgent repair.

1. Establish scope and constraints before touching production code. Read repository
   instructions, callers, tests, interfaces, and deployment assumptions. Inventory
   working-tree changes and preserve unrelated work. Translate the risk budget
   into explicit limits: allowed files and interfaces, time or step budget,
   acceptable verification gaps, and prohibited migrations. If those limits are
   missing, propose conservative limits but do not treat them as approved. Identify
   the concrete maintenance goal: for example isolating one dependency or making
   one calculation independently testable. Do not use aesthetic preference alone
   to justify a wide rewrite.

2. Map behavior at the boundary. List return values, exceptions, mutations,
   persistence writes, emitted events, ordering, retries, transaction boundaries,
   timing contracts, and resource cleanup. Include unusual inputs and documented
   quirks on which callers might rely. Distinguish intended requirements from
   current observations. A characterization test records what the system does;
   it does not establish that an apparent defect is desirable. Flag dangerous or
   disputed behavior for a separate decision rather than silently correcting it
   during a supposedly behavior-preserving change.

3. Run baseline tests and capture executable characterization evidence before
   structural edits. Prefer tests through stable public entry points. For pure
   functions, save representative and generated inputs and compare old versus new
   outputs and exceptions, including boundary values. Use exact comparison unless
   the contract explicitly permits a numeric tolerance or normalized ordering.
   Record seed, comparison rule, and exclusions. Do not normalize away meaningful
   differences merely to make equivalence pass. Retain the original implementation
   or an immutable reference artifact for the duration of the comparison.

4. For side-effecting code, create golden traces in an isolated test environment.
   Capture ordered calls at real boundaries, arguments with secrets redacted,
   returned values, errors, retries, and transaction outcomes. Stabilize clocks,
   randomness, and external identifiers with explicit test controls. Compare only
   declared observable behavior, not incidental private call choreography. Review
   golden artifacts before accepting them; snapshots of unexplained output are a
   weak oracle. Never replay a trace against production payment, messaging, or
   deletion endpoints. Use fakes or disposable dependencies with contract checks.
   If a seam requires a small edit to enable testing, isolate and review that edit
   first, establish tests immediately, and record the remaining confidence gap.

5. Choose the smallest transformation strategy. For a local refactor such as a
   rename, method extraction, or dependency seam, use in-place, independently
   green transformations protected by characterization tests; do not invent a
   facade or keep two production implementations. Only when replacing
   implementations or migrating callers incrementally, and the old contract must
   stay live during migration, use a stable facade and strangler path: put the
   old and new implementations behind that facade, move one responsibility or
   caller at a time, retain an explicit fallback while evidence accumulates, and
   specify the selection mechanism, ownership of state, rollback path, and
   criterion for removing the old path. For pure reads, shadow comparison may
   be useful in an authorized environment. Do not execute both paths for
   non-idempotent effects; compare captured inputs in a sandbox instead. Avoid
   a permanent abstraction that merely duplicates the legacy complexity without
   a bounded retirement plan.

6. Execute one safe step at a time: state the invariant, make the smallest move,
   run the characterization suite, compare differential results or golden traces,
   and run affected integration and type checks. Inspect the actual diff before
   continuing. If commits are authorized, commit each independently green safe
   step with its verification evidence; never combine a structural move with a
   speculative bug fix. Otherwise record equivalent checkpoints without committing.
   Do not leave an intermediate state that requires several later steps to work.
   Preserve old tests unless their assertions are demonstrably implementation-only.

7. Stop on any unexplained behavioral difference, expanding public API change,
   flaky oracle, or exceeded risk budget. Restore only your last owned step and
   reassess. When the underlying task is an urgent bug fix and a narrow ugly fix
   is safer, abandon the refactor and recommend that fix with a regression test.
   Record the deferred structural debt and the evidence needed to revisit it.
   Do not keep rewriting because of sunk effort or claim a large suite proves
   equivalence for unobserved side effects. Missing runtime access limits the
   verdict even if static review looks convincing.

8. At completion, rerun baseline-equivalent commands and broader required checks.
   Check public compatibility, error behavior, ordering, cleanup, and rollout
   assumptions. Remove the old path only after its retirement gate is satisfied
   and removal is in scope. Provide a rollback that accounts for persisted data;
   restoring source alone cannot undo a schema or data migration. Do not deploy,
   push, or modify production configuration without separate authorization.

Return the goal and risk limits, behavior inventory, characterization artifacts,
step ledger with exact commands and outcomes, residual equivalence gaps, and
rollback instructions. Conclude VERIFIED WITHIN SCOPE, PARTIAL, BLOCKED, or
REFACTOR ABANDONED IN FAVOR OF NARROW FIX. State observed evidence separately
from assumptions; never invent passing tests or describe limited sampling as proof.
```

## How It Works

Characterization, differential comparison, and isolated golden traces form a safety net before a strangler-style migration. These are established maintenance practices, not vendor-specific effectiveness claims. The agent execution contract is informed by tool-based inspection and validation in the [OpenAI GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide), with ordered procedures and explicit constraints informed by [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). This is original wording, not an upstream prompt adaptation.

## Variables

- `[module]`: target module, callers, public boundaries, and maintenance goal.
- `[test framework]`: existing test tools and runnable verification commands.
- `[risk budget]`: permitted scope, time or step limits, and tolerated verification gaps.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
