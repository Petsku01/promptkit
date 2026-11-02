---
category: "code"
title: "Logical-Unit Git Revert with Exact-Commit Confirmation"
source: "wshobson/agents"
license: "MIT"
---
# Logical-Unit Git Revert with Exact-Commit Confirmation

**Category:** code
**Source:** Adapted from https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/plugins/conductor/commands/revert.md (MIT)

Copyright (c) 2024 Seth Hobson. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--wshobsonagents-mit).

## When to Use

Undo a task, phase or feature track through history-preserving revert commits, after mapping logical scope to an inspected exact commit set. Conductor metadata is optional and parameterized rather than an installation prerequisite.

## The Prompt

```text
Prepare a history-preserving revert of a logical work unit. Discovery is read-only;
execution requires explicit confirmation of an immutable commit plan.
Repository and target: [checkout, branch and logical unit]
Scope semantics: [task only, phase only, phase plus later phases, or full track]
Metadata map: [optional index, plan, status paths and ID conventions; or none]
Verification: [reverted-tree tests and relevant behavior checks]

1. Inspect repository identity, branch, full HEAD SHA, index and working tree,
   including untracked files and relevant submodules. Check for an active merge,
   rebase, cherry-pick or revert. Preserve all existing work. If the tree/index
   is dirty or another operation is active, stop execution and report why;
   read-only discovery may continue. Never automatically stash, commit, discard,
   clean or overwrite changes. The user must establish a safe starting state.
2. Resolve the requested logical unit from supplied metadata or documented
   repository conventions. Conductor paths can be supplied as a map, but do not
   require Conductor setup or invent missing status files. If a phase is named,
   explicitly decide whether it means only that phase or that phase and later
   dependent phases BEFORE displaying the confirmation plan. Neither silently
   expand to later phases nor ignore them when dependency analysis requires them.
   Ambiguous scope blocks execution; report alternatives without choosing for
   the user. With no commits found, report no verified mapping rather than
   deleting metadata or assuming there was no implementation.
3. Use commit-message patterns, task IDs and path history only as discovery
   hints. Escape search patterns appropriately and resolve candidates to exact
   full SHAs reachable from the intended branch. Inspect each diff, its parent(s),
   files and relationship to the task. Find implementation, verification and
   metadata commits even if messages differ. Exclude unrelated matching commits.
   Flag mixed-purpose commits: whole-commit revert may remove unrelated work and
   requires an explicitly revised plan, not silent partial patch selection.
4. Inspect merges and dependency order. A merge requires an explicitly chosen,
   justified mainline parent; do not guess -m from parent numbering alone.
   Determine whether newer work depends on the target or changes the same API,
   schema or configuration. Inspect existing revert commits and resulting tree
   state: a message saying “revert” is not proof the original change is absent,
   especially after reapplication. Deduplicate and explain included/excluded
   candidates. Stop on unresolved mapping, already-reverted ambiguity or unsafe
   dependent work rather than blindly collecting regex matches.
5. Display the exact execution plan: starting branch/HEAD, selected scope
   semantics, full SHAs and subjects, newest-first reverse-dependency order,
   merge-parent choices, expected affected files, consumer/dependency impact,
   metadata treatment and verification commands. Explain destructive application
   effects that reverting code will not undo, such as deployed data migrations.
   List any proposed follow-up status edits separately. Request literal YES for
   this exact plan. No answer, a generic earlier approval, lowercase yes, or an
   unavailable interactive channel means no execution. In non-interactive mode,
   return the plan awaiting confirmation unless exact-plan confirmation was
   already supplied and remains valid. Never push or publish from this prompt.
6. Immediately before execution, recheck branch, HEAD and clean index/tree
   against the confirmed plan. Any drift invalidates confirmation. Execute one
   git revert at a time, newest first in the inspected dependency order, using
   the confirmed mainline parent only for merges. Record the original SHA,
   generated revert SHA and actual command result after each success. These
   authorized revert commits are not permission to commit unrelated work.
7. STOP on any conflict or command error. Do not auto-resolve, skip a commit,
   continue the sequence or abort without separate instruction. Report conflicts,
   current operation state, completed revert SHAs and pending originals. Earlier
   completed reverts remain real commits; aborting an active revert does not
   remove them. Never advertise all-or-nothing rollback when the operation was
   partial. Preserve enough state for a maintainer to choose resolution or abort.
8. After the full sequence, inspect the resulting diff and status. Update only
   explicitly authorized metadata using the actual resulting task state; do not
   blindly decrement counters, reset every task marker or delete a track. Avoid
   duplicate status changes already made by revert commits. Keep additional
   metadata edits visible and uncommitted unless separately authorized. Run the
   agreed tests against the reverted tree and check affected application behavior.
   If tests fail or cannot run, report that result rather than “revert verified.”

Return an original-to-revert SHA ledger, completed/pending scope, file impact,
metadata state and actual verification results. To undo this operation, propose
inspection and confirmation of the exact generated revert SHAs with dependency
analysis; never assume a HEAD-relative range still identifies them. Do not use
history-reset or checkout-discard recipes as a shortcut. Partial success, conflict
state and untested behavior must remain explicit in the final verdict.
```

## How It Works

Logical IDs locate candidates; inspected diffs and dependency relationships determine the real plan. Exact confirmation and a per-commit ledger prevent ambiguous phase semantics, dirty-work loss and misleading rollback claims.

## Variables

- `[checkout, branch and logical unit]`: repository and requested task/phase/track.
- `[task only, phase only, phase plus later phases, or full track]`: explicit scope semantics.
- `[optional index, plan, status paths and ID conventions; or none]`: optional Conductor or equivalent metadata.
- `[reverted-tree tests and relevant behavior checks]`: executable post-revert acceptance checks.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
