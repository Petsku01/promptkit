---
category: "code"
title: "Dependency and Framework Upgrade Workflow"
source: "wshobson/agents; github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Dependency and Framework Upgrade Workflow

**Category:** code
**Source:** Adapted from https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/plugins/framework-migration/commands/deps-upgrade.md (MIT); additional variants adapted from https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/react19-migrator.agent.md (MIT) and https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/dotnet-upgrade.agent.md (MIT).

Copyright (c) 2024 Seth Hobson; Copyright GitHub, Inc. Full permission and warranty notices: [wshobson/agents MIT](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--wshobsonagents-mit) and [GitHub MIT](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Upgrade a bounded dependency group or framework target through compatibility analysis, reproducible baselines, incremental changes, and fail-fast verification. React 19 and .NET SDK/TFM branches specialize the same workflow rather than creating separate migration shells.

## The Prompt

```text
Upgrade only the authorized dependency or framework scope.
Scope and target: [repository, packages/frameworks and exact target versions]
Compatibility obligations: [supported consumers, peers, platforms and runtimes]
Verification contract: [build, typecheck, tests, behavior and performance budgets]
Execution limits: [allowed files, network/install permissions and excluded actions]
Recovery destination: [retained reference or verified backup including local work]

1. Inventory manifests, lockfiles, workspace boundaries, runtime/SDK pins, build
   tools, peer dependencies, project references and CI environments. Inspect local
   changes and protect unrelated work. Record current resolved versions rather
   than only manifest ranges. Confirm which target versions are authorized; do not
   turn a narrow request into upgrading everything to latest. Dependency installation
   and lifecycle scripts execute code, so respect repository trust and install scope.
2. Obtain official release notes, changelogs, migration guides and lifecycle evidence
   covering current through target versions. Build a compatibility matrix with
   component, current, target, runtime/SDK constraints, peer ranges, consumers,
   evidence URL and unresolved conflicts. An absent warning is not proof of peer
   compatibility. Categorize source, behavior, security and tooling risks; patch
   labels alone do not make a batch safe. Block unsupported combinations or propose
   explicit alternatives without silently forcing peer resolution.
3. Capture a reproducible baseline using the existing locked installation process.
   Run the agreed build, lint/typecheck, unit/integration tests and critical behavior
   checks. Record commands, versions, exit status and known failures. Measure bundle
   size or performance only when relevant and under comparable conditions. A failing
   baseline needs a documented decision before migration; never call a post-upgrade
   failure pre-existing without evidence. Preserve recovery material containing
   manifests, locks, source/config changes and any uncommitted work within scope.
4. Plan small compatible batches with explicit stop points. Keep coupled peers
   together but separate unrelated changes. Select intermediate versions when the
   official migration path requires them. For each batch list exact files, expected
   API adaptations, tests and rollback procedure. Pin codemod packages and transforms
   to reviewed versions or immutable commits; inspect their behavior and scope before
   execution. Never execute a moving remote script or latest codemod by default.
5. Apply one authorized batch, update the lockfile through its package manager and
   inspect the entire diff, including transitive changes and generated files. Do
   not bypass conflicts by removing the lockfile or disabling checks. Re-run the
   baseline verification plus focused migration tests. Snapshot changes require
   reviewed diffs and a behavioral explanation; do not blindly update snapshots
   until tests pass. Preserve assertions rather than weakening them to accept a
   regression. Record per-batch evidence and unresolved warnings before continuing.

Worked variant — React 19 application:
6. Discover JavaScript, JSX, TypeScript and TSX entry points, components, tests and
   server-rendering/hydration paths. Align React, React DOM, typings and required
   toolchain peers through the matrix. For an application using ReactDOM.render,
   migrate to createRoot while retaining its root for unmount; for hydration use
   hydrateRoot instead of replacing server HTML with a client-only render path.
   Replace removed findDOMNode usage with an explicit DOM ref and test focus and
   measurement behavior. Review legacy context and string refs where actually used.
7. For function-component defaultProps, evaluate parameter defaults and preserve
   undefined versus null behavior; do not mechanically rewrite class defaultProps.
   Treat forwardRef conversion to a ref prop as optional modernization, not a
   React 19 prerequisite. Check public component consumers and ref typing before
   changing it. For useRef typing changes choose an appropriate initial value and
   type, not a blanket null replacement that changes program semantics. Retain
   imports required by actual namespace or runtime use.
8. Search for remaining migration patterns and record paths and counts, including
   intentional compatibility cases. Search results are audit evidence, not tests.
   Run the real production build, typecheck and behavior tests for mounting,
   hydration, refs, events and key user flows. Report only measured deprecated
   pattern findings; never announce unconditional zero remaining patterns.

Worked variant — .NET SDK and target frameworks:
9. Discover solutions, project files, Directory.Build properties, TargetFramework
   and TargetFrameworks, global.json, runtime identifiers, project references and
   deployment/CI constraints. Resolve imported or conditional properties rather
   than relying on a text search of each project alone. Choose a supported SDK/TFM
   using Microsoft's official release lists, support policy and migration guidance.
   Local installed-SDK listings describe this machine, not available remote releases;
   do not use an arbitrary two-year heuristic to select a target.
10. Keep this variant scoped to SDK/TFM changes and necessary compatibility edits.
    Route NuGet version changes through the general dependency batches and matrix,
    not an automatic latest-package sweep. Do not retarget netstandard libraries
    without an explicit consumer-compatibility decision; retaining or multi-targeting
    may be required. Work in project-reference order with coherent shared settings.
    Update authorized SDK pins and CI configuration consistently, then restore,
    build and test affected projects and their consumers across supported targets.
    Report platform-specific workloads or deployment checks that cannot run locally.

11. After all applicable branches, repeat the full verification contract from a
    reproducible install and compare against baseline. Stop immediately on failed
    gates, incompatible peers, unexplained diffs or budget regressions; do not hide
    a failing exit code behind a success message. If recovery is authorized, restore
    only owned changes, reinstall from saved locks and run baseline checks again.
    A failed reinstall or test means recovery is unverified. Retain recovery refs
    and backups; never delete the upgrade branch as a rollback technique.

Deliver the inventory, sourced compatibility/risk matrix, batch ledger, changed-file
list, reviewed snapshot explanations and pre/post command evidence. State exactly
what passed, failed or remains unverified, plus recovery status. Do not commit,
push, deploy, delete references or discard unrelated work without separate approval.
```

## How It Works

The baseline and peer-compatibility matrix constrain each batch, while the worked variants add ecosystem-specific discovery and checks. Unlike `gha-node-runtime-upgrade.md`, this covers dependency/framework compatibility rather than action-runner runtime gates. Unlike `refactoring-safety-net.md`, its primary operation is version migration, not behavior-preserving structural refactoring. Recovery is successful only after real checks pass.

## Variables

- `[repository, packages/frameworks and exact target versions]`: bounded upgrade request.
- `[supported consumers, peers, platforms and runtimes]`: compatibility matrix dimensions.
- `[build, typecheck, tests, behavior and performance budgets]`: baseline and acceptance gates.
- `[allowed files, network/install permissions and excluded actions]`: execution scope.
- `[retained reference or verified backup including local work]`: non-destructive recovery material.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
