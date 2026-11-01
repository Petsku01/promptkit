---
category: "code"
title: "Git Worktree Isolation with a Clean Baseline"
source: "obra/superpowers"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Git Worktree Isolation with a Clean Baseline

**Category:** code
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/using-git-worktrees/SKILL.md (MIT)

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).

## When to Use

Prepare an isolated checkout for feature work without disturbing the current workspace. Detect harness-managed isolation and submodules first, then establish an actual test baseline before implementing changes.

## The Prompt

```text
Prepare an isolated workspace, but do not implement the feature yet.
Repository and base revision: [canonical checkout and base]
Isolation authorization: [reuse/create permission, branch and destination preference]
Setup and baseline: [approved setup/test commands and budget]
Allowed configuration edits: [whether the exact .gitignore edit is authorized]

1. Read project and runtime instructions. Record canonical root, revision, branch
   or detached HEAD, git status --short, and git worktree list --porcelain.
   Resolve git rev-parse --git-dir and --git-common-dir to canonical paths.
   Check git rev-parse --show-superproject-working-tree and submodule status;
   a .git file or differing Git paths alone is not sufficient proof of isolation.
   A submodule is not a task-isolated workspace merely because Git paths differ.
   Verify any linked worktree or native sandbox is the intended task workspace
   before reusing it. Do not nest another worktree inside valid existing isolation.
2. Honor explicit placement and branch preferences. If creation is authorized,
   prefer a supplied native isolation tool and its actual ownership/lifecycle
   contract. Verify the resulting root and branch; do not assume native-tool
   success proves placement. Use manual git worktrees only when appropriate and
   no native mechanism manages the required isolation. Missing authorization is
   BLOCKED; in non-interactive runs stop rather than silently work in place.
3. For a manual worktree, inspect existing destinations and branch names without
   overwriting or forcibly checking out an occupied branch. Default to the
   project's declared location; absent that, use its existing .worktrees/ or
   worktrees/ convention, otherwise propose .worktrees/ under the root.
   For a project-local destination, run from the main root:
   git check-ignore -v -- "<exact-selected-relative-directory>/"
   Check that exact selected container directory, not an OR check against an
   alternate name. Also verify the exact proposed child destination is ignored
   and not tracked. Record matched rules and command statuses. For an external
   destination record why an ignore rule in the source checkout is inapplicable.
4. If the selected local path is not ignored, edit .gitignore ONLY when that exact
   edit is authorized; otherwise stop and report the required rule. Recheck the
   actual selected directory and child path after an authorized edit. Never
   automatically commit the rule, change global ignore policy or force creation.
5. Create the new branch/worktree from the approved base using quoted exact
   paths. On permission failure, sandbox denial, collision or unsupported
   submodule setup, stop with evidence. Do not fall back to the original checkout
   when isolation was requested. Record any owned resources created before failure.
6. In the verified isolated root, use only approved project-native setup commands.
   Do not infer permission for network installs or lockfile changes from a
   manifest's existence. Initialize submodules only if explicitly authorized.
   Run the baseline tests before feature edits. Record exact commands, output,
   exit statuses, collected/skipped tests and setup-induced tree changes.
7. Report READY only for established isolation and a passing baseline. A failing
   baseline is BASELINE FAILED; unavailable dependencies/tests are BLOCKED or
   UNVERIFIED. Preserve the workspace and evidence for review, unless cleanup
   was explicitly authorized. Never delete another worktree, commit, push or
   modify the feature as part of this preparation.

Return: isolated root and mechanism/ownership, base revision, branch state,
submodule findings, exact ignore checks, setup changes, baseline evidence,
readiness status and any unresolved prerequisite. Keep pre-existing work intact.
```

## How It Works

Discovery avoids redundant or misidentified worktrees. Checking the selected path rather than either conventional name closes an ignore-rule loophole; the baseline separates pre-existing failures from later feature regressions. Worktrees isolate files, not shared Git metadata, credentials, ports, or databases.

## Variables

- `[canonical checkout and base]`: source repository and approved starting revision.
- `[reuse/create permission, branch and destination preference]`: explicit isolation scope.
- `[approved setup/test commands and budget]`: permitted preparation and baseline checks.
- `[whether the exact .gitignore edit is authorized]`: narrow configuration-write permission.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
