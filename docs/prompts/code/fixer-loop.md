---
category: "code"
title: "Fixer Loop (Run-Fix-Re-Run Until Green)"
source: "promptkit-authored"
---
[← Back to Code Prompts](../index.md)

# Fixer Loop (Run-Fix-Re-Run Until Green)

**Category:** code
**Source:** Grounded in vendor agent-loop guidance; authored.

## When to Use

Repair reproducible failures with actual command execution, small patches, and a strict retry ceiling. This is a failure-repair workflow, not a replacement for specifying a new feature or performing the complete TDD cycle.

## The Prompt

```text
Repair failures from [command] until the observed result satisfies [expected],
within [max iterations]. Use the available execution and editing tools. Never
substitute a hypothetical command transcript for a run. If execution is not
available, return BLOCKED with the missing prerequisite instead of claiming green.

1. Establish scope and a reproducible baseline. Read repository instructions,
   relevant manifests, existing implementation, and current working-tree changes.
   Preserve unrelated edits. Record the exact full command, working directory,
   interpreter or environment, relevant flags, and expected exit status. Confirm
   the command represents the required full suite. If it is only a focused check,
   identify the repository's full-suite command and make that an additional final
   gate. Do not silently redefine the user's command or acceptance expectations.

2. Set the iteration ceiling before editing; use four fix attempts if the supplied
   maximum is empty. An attempt comprises one coherent patch followed by the full
   verification command. Count unsuccessful or reverted patches against the budget.
   Reserve time for final full-suite verification and reporting. Run the complete
   baseline command and capture its exit status, failing identifiers, diagnostic
   output, and warning inventory. Distinguish pre-existing warnings and failures
   from those introduced later; unavailable services are environment blockers.

3. Select exactly one actionable failure. Prefer the first reproducible failure
   in the runner's reported order. If failures are independent, choose the cheapest
   reproducible failure to diagnose, explaining the departure. A collection or
   setup failure takes priority when it prevents meaningful behavioral checks.
   Record a stable signature: failing test or stage, error type, and causal message.
   Do not chase every downstream failure from one broken prerequisite, and do not
   relabel the same failure just because a line number or timestamp changed.

4. Diagnose before patching. Read the complete relevant traceback and the code
   at the failing boundary. State a concise root-cause hypothesis and a falsifying
   check. Follow the data or control path across callers when necessary. Additional
   focused probes may help diagnosis, but they are not replacements for the full
   command. If evidence points to configuration, dependency compatibility, or a
   shared fixture, investigate that layer rather than repeatedly patching symptoms.

5. Apply the smallest coherent change that addresses that hypothesis. Limit edits
   to necessary implementation and directly justified supporting files. Avoid
   unrelated refactors, broad dependency upgrades, formatting churn, and speculative
   fixes. Never disable tests, weaken assertions, remove warning reporting, alter
   expected behavior without authorization, or hide a nonzero exit status. Inspect
   the diff for accidental scope growth before executing the next verification.

6. Re-run the FULL same command with the same arguments, directory, and environment
   after every patch. Do not replace it with the previously failing test, a subset,
   a cached summary, or a piped command that conceals failure. Capture actual exit
   status and compare all failures and warnings with the baseline. If new failures
   appear, treat them as regressions and revert or correct only your own patch
   before pursuing another independent failure. Each further patch consumes an
   attempt and requires the full command again.

7. Track consecutive reruns that retain the selected stable failure signature.
   If the same failure survives two consecutive fix attempts, STOP the repair loop
   and patching. Re-diagnose at a higher level: challenge the reproduction,
   environment, API contract, shared dependency, fixture, or architectural assumption.
   Report new evidence and an escalation target; a new hypothesis alone does not
   authorize a third patch. Resume only after explicit user re-authorization and
   within the original remaining attempt budget; the global ceiling never resets.
   Reset the consecutive-failure counter only on observed PROGRESS: the selected
   failure is verified resolved and a genuinely different failure is observed.
   Renamed diagnostics, new hypotheses, and re-authorization are not progress.

8. Declare GREEN only when the complete required suite passes, the full original
   command satisfies every expected outcome, and no new warnings were introduced.
   If expected requires zero warnings, baseline warnings must also be resolved.
   Check additional required lint, type, or integration gates rather than assuming
   a passing unit suite proves them. A timeout, skipped required test, missing
   dependency, or unreachable service is not green.

Stop when green, the attempt budget is exhausted, a permission boundary is
reached, or further diagnosis cannot produce a justified patch. Return the final
status, exact commands and outcomes, files changed, attempt ledger, remaining
failure signatures, warnings, and the next escalation target. Preserve a useful
reviewable patch or revert only your own regressing changes. Report partial
progress instead of thrashing, installing unapproved infrastructure, or claiming
that unexecuted checks passed.
```

## How It Works

The loop specializes ReAct's action/observation structure into reproducible repair attempts. Unlike reflection, its acceptance evidence comes from execution rather than self-assessment. Unlike prompt chaining, it returns to the same full command until green or a stop gate; unlike TDD Full Cycle, it starts from an existing failure rather than a newly specified red behavior. Unlike Test-First Bug Fixing Approach's repeat-until-green instruction, this repair loop has a hard attempt ceiling; Four-Phase Root-Cause Debugging structures investigation rather than specifying this bounded run-fix-rerun acceptance loop.

[Anthropic's client-tool loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) separates model requests from real execution and returned results. [OpenAI's agentic workflow guidance](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) supports investigation, incremental fixes, repeated testing, and final verification. The full-command requirement, warning gate, and same-failure-twice rule are authored safeguards, not quoted vendor policies.

## Variables

- `[command]`: exact runnable verification command, directory, environment, and full-suite context.
- `[expected]`: required exit status, behavior, warning policy, and additional acceptance gates.
- `[max iterations]`: hard patch-attempt ceiling; defaults to four if unspecified.

## Tested On

Not model-tested. Original authored workflow; repository validation does not constitute an agent repair benchmark.
