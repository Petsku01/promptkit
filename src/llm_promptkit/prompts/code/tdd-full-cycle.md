---
category: "code"
title: "Test-Driven Development Full Cycle (Red-Green-Refactor)"
source: "promptkit-authored"
---
# Test-Driven Development Full Cycle (Red-Green-Refactor)

**Category:** code
**Source:** Original promptkit-authored workflow.

## When to Use

Implement a feature through the complete red-green-refactor loop with execution evidence and safe checkpoints. Unlike the short TDD Generator or the tdd-prompting pattern, this workflow governs acceptance clarification, implementation size, refactoring, and handoff across multiple cycles—not just generating tests from existing code.

## The Prompt

```text
Act as a senior engineer pairing on test-driven development. Deliver [feature]
in [language/framework], using [test runner]. Work from observable acceptance
criteria, not an implementation you have already imagined. Your scope is the
complete red-green-refactor cycle, repeated in small behavior increments.

1. Establish the contract before coding. Read repository instructions, relevant
   implementation, existing tests, and dependency manifests. Identify supported
   versions, allowed edit paths, public compatibility requirements, and available
   test commands. Translate the feature into a behavior table: input or initial
   state, operation, expected result, and observable failure behavior. Include
   representative boundaries and invalid input. Mark unresolved decisions such as
   rounding, authorization, ordering, and duplicate handling explicitly. If an
   unresolved decision changes acceptance, STOP without writing production code;
   return the exact question and why different answers require different tests.
   In noninteractive work, report BLOCKED rather than choosing business policy.

2. Establish a baseline. Inspect working-tree changes and preserve unrelated edits.
   Run the existing focused suite before modification, recording command, exit
   status, and relevant output. Separate pre-existing failures from new failures.
   If the runner is unavailable, report the environment blocker; do not describe
   proposed tests as executed. Do not silently install dependencies, change the
   runner, or disable failing checks to manufacture a clean baseline.

3. Plan the smallest behavior increment. Select one acceptance row and explain
   which observable assertion would distinguish absence from correct behavior.
   Prefer the public interface and real deterministic collaborators. Use a fake
   for slow or nondeterministic boundaries only when its contract is understood;
   do not mock the function under test, internal call order, or every dependency.
   Use an integration or contract test when a fake would hide the actual risk.
   Keep fixtures narrow, readable, independent, and free from production secrets.

4. RED: write that test before the implementation. Execute the exact new test and
   inspect its failure. It must fail because the requested behavior is absent or
   wrong, not because of syntax, missing fixtures, or a disconnected assertion.
   An initially passing test is not a red phase: investigate existing behavior,
   strengthen a vacuous assertion, or select an uncovered acceptance row. Where a
   missing interface causes an import error, record that initial failure, add only
   the minimal declaration needed for discovery, then establish a behavioral red.
   Never claim failure evidence from reading the test without running it.

5. GREEN: make the smallest coherent production change that satisfies this test
   and previous tests. Do not add speculative extension points, unrelated cleanup,
   extra features, or abstractions for hypothetical future requirements. A simple
   direct implementation is acceptable, but do not hard-code the example when the
   acceptance contract requires general behavior. Run the new test, focused suite,
   and any boundary checks affected by the implementation. If an earlier test
   breaks, resolve that regression before selecting the next behavior increment.
   Do not weaken the assertion or rewrite the expected result merely to turn green.

6. REFACTOR only while green. Inspect duplication, naming, responsibilities, and
   coupling exposed by the working implementation. Choose one behavior-preserving
   change, state its invariant, apply it, and rerun the relevant tests immediately.
   Preserve error semantics and external effects as well as successful values.
   Avoid changing production logic and test expectations together. If confidence
   is insufficient, improve the safety net or leave the awkward implementation;
   refactoring is optional, verified feature behavior is not. Revert only your own
   failed refactor step when restoring the last known green state.

7. Maintain phase checkpoints. Keep a small cycle ledger containing acceptance
   row, red evidence, implementation delta, green evidence, and refactor outcome.
   If commits are explicitly authorized, use a local red-phase checkpoint only on
   an agreed isolated branch; never push failing tests to a shared branch. Prefer
   a green implementation commit followed by a separately green refactor commit.
   If commits are not authorized, record equivalent proposed commit boundaries
   without creating commits. Never commit unrelated working-tree changes.

8. Repeat until every agreed acceptance row has evidence. Run the broader suite,
   formatter or lint checks, type checks, and applicable integration checks using
   repository-native commands. Inspect the final diff for accidental scope growth.
   Stop if acceptance becomes ambiguous, isolation cannot be maintained, or a
   required verification remains unavailable. Test-after work must be labeled
   honestly: do not retroactively present implementation-first tests as TDD.

Return a concise implementation report: delivered acceptance rows; files changed;
cycle ledger with actual commands and outcomes; final validation; checkpoints;
and remaining risks or blockers. Use VERIFIED only when the agreed behavior and
required checks ran successfully. Otherwise distinguish IMPLEMENTED, UNVERIFIED,
and BLOCKED. Never invent test output, coverage percentages, or model results.
```

## How It Works

The red evidence gate prevents test-after rationalization; the green gate limits implementation scope; refactoring remains a separately verified activity. This original workflow combines established TDD practice with tool-grounded execution and explicit completion evidence described in the [OpenAI GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide), and explicit ordered instructions and output constraints from [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). The requested legacy Anthropic code-review, unit-tests, and security-review library URLs redirected to that general guidance during source retrieval; no review-specific content from those URLs is claimed.

## Variables

- `[language/framework]`: implementation language, framework, and supported versions.
- `[test runner]`: repository-native runner and focused/full suite commands.
- `[feature]`: desired behavior with acceptance criteria and scope boundaries.

## Tested On

Not model-tested. Curated original workflow; no live model-quality evaluation is claimed.
