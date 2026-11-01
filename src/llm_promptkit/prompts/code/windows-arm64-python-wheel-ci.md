---
category: "code"
title: "Native Windows ARM64 Python Wheel CI Migration"
source: "github/awesome-copilot"
license: "MIT"
---
# Native Windows ARM64 Python Wheel CI Migration

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/python-win-arm64-gha-wheel-builder.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Extend or repair an existing Python wheel pipeline for native Windows ARM64 while preserving its supported platforms, release boundaries and supply-chain policy.

## The Prompt

```text
Add or repair native Windows ARM64 wheel support in this repository.
Repository and release workflow: [checkout, revision and workflow paths]
Required outputs: [Python versions, ABI variants and package import names]
Permissions: [local edits, network lookup and CI execution budget]
Dependency policy: [approved indexes, version pins and action trust policy]

1. Inventory the actual packaging path before editing. Follow reusable workflows,
   composite actions, pyproject settings and build scripts to the authoritative
   wheel configuration. Identify cibuildwheel, maturin, setuptools-rust or custom
   build tools, their pinned versions, existing platform matrix and release jobs.
   Search all workflows for existing win_arm64 coverage: repair or extend it,
   never add a duplicate job. Record the pre-change matrix and expected artifacts.
2. Verify CURRENT compatibility from primary vendor documentation and published
   release metadata. Record retrieval dates and links for GitHub runner availability,
   repository/account eligibility and billing, the selected runner image contents,
   cibuildwheel native support, setup-python architecture/version coverage, and
   each native dependency's Windows ARM64 wheels. Build a compatibility table by
   Python/ABI/tool/dependency combination. Do not carry forward historical PyTorch
   availability claims or assume a runner label remains available. If a required
   combination lacks authoritative support, mark it blocked rather than silently
   dropping an existing platform or inventing a successful source-build fallback.
3. Use the repository's existing matrix fields to select a verified native ARM64
   runner, such as windows-11-arm only when currently supported. Preserve Linux,
   macOS and Windows AMD64 entries, triggers, permissions, fail-fast policy and
   source distributions. Narrow exclusions to unsupported ARM64 combinations.
   Review CIBW_BUILD, CIBW_SKIP, architecture overrides and reusable-workflow inputs
   so allow-lists cannot silently skip the new target. Expand the resulting matrix
   and prove every intended ARM64 entry is selected exactly once.
4. Inspect the actual image/toolchain rather than substituting hardcoded Visual
   Studio paths. Use supported discovery or setup actions under the trust policy,
   verify MSVC target selection, and isolate x64-only environment setup by matrix
   metadata. Confirm the interpreter is ARM64, not an emulated x64 installation;
   set setup-python architecture explicitly when needed by the verified action.
   For Rust components, use the full aarch64-pc-windows-msvc target consistently in
   rustup, cargo and maturin settings. Configure CMake, LLVM or Fortran only when
   the project needs them and the image supports the chosen tools.
5. Review native dependency bootstrap commands, DLL discovery and repair steps.
   Check vendor package metadata for matching version, ABI and win_arm64 tags,
   including optional test dependencies such as PyTorch when actually present.
   Use approved trusted indexes with explicit version pins and hashes where the
   project supports them. Do not add an arbitrary extra index or unpinned nightly
   source to make resolution appear successful. Explain dependency-confusion and
   reproducibility trade-offs for any proposed policy change; leave it blocked
   until approved. Avoid unrelated dependency upgrades and lockfile churn.
6. Preserve test symmetry with existing Windows jobs, adding ARM64 coverage to
   shared build and test paths rather than replacing generic tests unnecessarily.
   Validate unique upload/download artifact names across the expanded matrix,
   downstream aggregation globs and release collection. On authorized native CI,
   inspect produced wheel filenames and WHEEL tags for the intended interpreter,
   ABI and win_arm64 platform; inspect native binary architecture where relevant.
   Install the exact built wheel into a clean ARM64 environment outside the source
   tree, import the required modules and run representative package tests. Check
   runtime DLL dependencies so an import does not accidentally use the checkout.
7. Run repository formatting, YAML validation and actionlint when available.
   Review the scoped diff and matrix before/after table for accidental regressions
   and verify a second configuration pass would add no duplicate entries. Lint
   alone is not a native build. Triggering costly CI, uploading externally or
   publishing packages requires explicit authorization; preserve publish guards
   and credentials. If CI was not run, report CI-NOT-RUN and distinguish configured,
   linted, built, installed and tested states instead of declaring native support
   verified. Do not commit, push or release as part of this task.

Return changed paths, compatibility sources and dates, matrix/artifact comparison,
commands and actual results, native install/import evidence or explicit blockers,
remaining unsupported combinations, estimated CI scope and a narrow rollback plan.
```

## How It Works

A compatibility ledger replaces stale ecosystem assumptions. Matrix expansion catches skipped or duplicate jobs, and installing the produced artifact distinguishes configuration validity from usable native wheels.

## Variables

- `[checkout, revision and workflow paths]`: pipeline to modify.
- `[Python versions, ABI variants and package import names]`: required native coverage.
- `[local edits, network lookup and CI execution budget]`: side-effect permissions.
- `[approved indexes, version pins and action trust policy]`: supply-chain constraints.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
