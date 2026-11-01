---
category: "defensive"
title: "Evidence-Gated Agent Completion Report"
source: "obra/superpowers"
license: "MIT"
---
# Evidence-Gated Agent Completion Report

**Category:** defensive
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/verification-before-completion/SKILL.md (MIT)

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).

## When to Use

Before reporting that agent work is complete, fixed, passing, or ready for integration. Use when delegated work, stale test runs, or partial checks could be mistaken for current-tree verification.

## The Prompt

```text
Produce an evidence-gated completion report for this work.
Checkout and requested outcome: [root, task and acceptance criteria]
Allowed verification: [commands/tools, environment and side-effect permissions]
Budget: [time/resource limit]

Evidence before claims:
1. Record the exact checkout, current revision and working-tree state, including
   uncommitted changes. Enumerate each acceptance criterion and proposed claim.
   For each, select a current-tree command or tool check that could falsify it.
   Inspect unknown scripts before running them; do not cross approval boundaries.
2. Run the relevant checks after the last change to the files they exercise.
   Capture exact command, working directory, relevant environment/version,
   output or saved-log reference, exit status, and tested scope. Read the complete
   relevant output; an exit code alone can hide skipped checks or zero collected
   tests. Do not reuse a stale run after a relevant tree/configuration change.
3. Match claim strength to evidence. A linter does not prove a build, a build
   does not prove behavior, and a focused test does not prove the full suite.
   Reproduce a reported bug through its original symptom where safe. Claim a
   regression test catches the bug only after a real safe red/green experiment;
   use a disposable copy rather than overwriting unrelated working-tree changes.
4. Treat delegated success reports as leads. Independently inspect the actual
   resulting diff/artifact and run an appropriate check against the current
   integrated tree. If independent verification is unavailable, label the claim
   reported-by-delegate and UNVERIFIED, not independently confirmed.
5. If a check fails, report its actual output and failure. Make only authorized
   fixes, then rerun affected checks. If execution is blocked or the budget ends,
   retain useful bounded evidence and explicitly name everything not established.
   Never manufacture output or weaken acceptance criteria to produce a success.

Return a claim-to-evidence table:
claim/criterion | checkout/tree identity | exact command/check | observed output
and exit status | VERIFIED / FAILED / PARTIAL / BLOCKED / UNVERIFIED | residual scope.

PARTIAL means a precisely identified subset was verified; state that subset and
what remains. BLOCKED names the missing prerequisite. UNVERIFIED means no suitable
current evidence exists. For a non-shell tool, report its actual result/status;
do not invent a shell exit code. Preserve log references without exposing secrets.

End with a short status, files/artifacts changed and remaining risks. Say complete
only when every acceptance criterion has suitable current-tree evidence. Do not
commit, publish or deploy merely because verification succeeded.
```

## How It Works

The claim-to-evidence mapping makes scope visible: current, relevant checks support narrow assertions, while failure and missing prerequisites remain reportable outcomes. Independent integrated-tree checks prevent a delegated success message from becoming unsupported completion evidence.

## Variables

- `[root, task and acceptance criteria]`: exact target and observable obligations.
- `[commands/tools, environment and side-effect permissions]`: available checks and authorization boundaries.
- `[time/resource limit]`: bound beyond which residual verification must be reported explicitly.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
