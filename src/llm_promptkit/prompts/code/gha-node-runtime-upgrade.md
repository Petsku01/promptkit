---
category: "code"
title: "GitHub Actions JavaScript Runtime Upgrade with Runner Compatibility Gates"
source: "github/awesome-copilot"
license: "MIT"
---
# GitHub Actions JavaScript Runtime Upgrade with Runner Compatibility Gates

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/github-actions-node-upgrade.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Upgrade the embedded Node runtime of a maintained JavaScript/TypeScript GitHub Action while preserving its consumer contract, bundle conventions and maintainer-controlled release process.

## The Prompt

```text
Upgrade this repository's JavaScript GitHub Action to the explicitly approved
supported Node runtime, producing a tested local patch and release/PR drafts.
Action scope: [repository and action directories]
Target runtime: [exact supported runs.using value]
Consumer support: [hosted/self-hosted runner versions, OS and architectures]
Release policy: [versioning, compatibility commitments and bundled-file rules]

1. Require an explicit target runtime; do not infer that the newest Node release
   is supported by GitHub Actions. Verify current official Actions runtime and
   runner documentation and record the source and compatibility conditions.
   Confirm hosted and self-hosted runners in the supported consumer set can run
   the target, including operating-system/library and architecture constraints.
   If runner inventory or minimum support is unknown, report the gap and stop
   runtime edits rather than assuming consumers can upgrade automatically.
2. Inspect action.yml or action.yaml for every in-scope action. Identify whether
   each is JavaScript, composite or Docker-based; runs.using for a composite
   action is not a JavaScript runtime selector. Follow main, pre and post to
   their actual entrypoints and inspect committed bundles, source maps and
   lifecycle conditions. Trace nested local actions and workflows without
   automatically upgrading separately maintained dependency actions.
3. Read package.json, package-manager declarations, lockfiles, workspace config,
   build scripts, TypeScript settings, bundler configuration and contributor
   instructions. Identify the repository's actual install/build/test commands.
   Respect npm, pnpm or Yarn conventions and their pinned versions; do not
   introduce another lockfile. Inspect native addons and transitive native
   dependencies for ABI, prebuilt-binary, platform and toolchain compatibility.
   Check removed/deprecated Node APIs, module resolution, ESM/CommonJS behavior,
   OpenSSL changes and assumptions about bundled versus external dependencies.
4. Decide release impact using the maintainer's documented policy and consumer
   support promise. A runtime change can break older runners, but it does not
   justify an unconditional major bump independent of that policy. Document
   whether a major, minor, patch or deferred version change is required. If
   policy is ambiguous, prepare the compatibility analysis and leave release
   versioning blocked. Avoid version commands with unreviewed lifecycle scripts;
   never generate tags or commits as a side effect of a package-version update.
5. Change only the approved runtime declarations and directly related sources,
   development-engine constraints and CI jobs. Distinguish the embedded action
   runtime from application test matrices and setup-node versions used for other
   projects. Search old version references and classify each before editing.
   Do not globally replace unrelated Node versions, dependency-action tags,
   historical release notes or examples for other actions. Update this action's
   usage examples only when the approved release policy calls for a new tag.
6. Install reproducibly under the target runtime with the existing package
   manager and lockfile rules, within authorized network/script permissions.
   Build using the real repository command, regenerating every required main,
   pre and post bundle. Review lockfile and bundle changes for unexpected
   upgrades, missing assets and accidentally committed local artifacts. Where
   committed dist files are required, verify regeneration is deterministic using
   the project's established check, not a source-only diff.
7. Run real unit and integration tests appropriate to the action, including
   failure handling and pre/post behavior. Run lint and type checks where
   configured. Exercise the action on the supported runner matrix through an
   authorized CI path when available. node --check is a parse-only check: it
   neither runs the action nor proves dependencies or runner compatibility.
   If no behavioral tests exist, state that limitation and propose or add
   authorized focused tests; never relabel parsing as a passing test suite.
   Keep local results separate from pending hosted/self-hosted validation.
8. Draft a release note, suggested commit subject, PR title and PR body that
   reflect the actual version decision. Include runtime change, minimum runner
   requirements, migration guidance, bundle changes, measured validation and
   unresolved risks. Mark all unexecuted CI checks as pending. Never move major
   tags, publish packages/releases, open a PR, push branches or commit changes
   automatically; these drafts are not publication authorization.

Return the scoped patch summary, compatibility evidence, release-policy decision,
and command/result ledger. List exact files changed, tests actually executed,
platforms not exercised, blockers and the final draft release/PR text. Do not
claim consumer readiness until the promised compatibility checks are complete.
```

## How It Works

Runtime support, consumer compatibility and release policy are separate decisions. Entry-point and bundle tracing prevents an apparently simple YAML change from shipping stale compiled code or incompatible native dependencies.

## Variables

- `[repository and action directories]`: actions authorized for this upgrade.
- `[exact supported runs.using value]`: maintainer-selected Actions runtime.
- `[hosted/self-hosted runner versions, OS and architectures]`: supported consumer matrix.
- `[versioning, compatibility commitments and bundled-file rules]`: release and artifact conventions.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
