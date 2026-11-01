---
category: "code"
title: "Production-Safe LaunchDarkly Feature Flag Removal"
source: "github/awesome-copilot"
license: "MIT"
---
# Production-Safe LaunchDarkly Feature Flag Removal

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/launchdarkly-flag-cleanup.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Assess and implement a narrowly scoped feature-flag retirement only when fresh environment configuration and application evaluation behavior support a defensible surviving value.

## The Prompt

```text
Assess whether this LaunchDarkly flag can be removed without unintended behavior
changes. Default to assessment and a PR-description draft; edit code only within
the explicitly authorized scope.
Target: [repository, project key and exact flag key]
Environment scope: [authorized environments and critical-environment set]
Freshness requirement: [snapshot timestamp, revision and maximum age]
Permissions: [read access, local edits, tests and separately authorized writes]

1. Verify project identity, exact flag key, account access and authorized environment
   set before reading remote configuration. Discover the available integration;
   do not install an MCP server or request tokens in chat. Use existing authorized
   credentials without exposing them. Obtain a fresh, timestamped configuration
   snapshot with revision metadata for every in-scope environment. Missing project,
   flag, freshness policy or environment access blocks removal. An empty critical-
   environment set is BLOCKED, never an all-environments-agree vacuous pass.
2. Build an environment behavior table from actual configuration, not lifecycle
   labels. Include on/off state, variation definitions with values and types,
   off value, fallthrough, individual targets, rules, segments, percentage and
   context-kind rollouts, experiments and scheduled changes where applicable.
   Resolve variation indexes to concrete values; matching indexes alone do not
   establish matching behavior. Check multivariate JSON, strings and numbers,
   not only booleans. Any unresolved targeting or rollout means no proven constant.
3. Inspect prerequisite flags and flags depending on this flag, including their
   environment-specific evaluations. Record cross-project or cross-repository
   dependencies only within authorized access; unavailable dependency evidence is
   a blocker, not proof of absence. Check whether different context kinds, tenant
   segments or percentage buckets can receive different values. Compare all
   authorized environments, highlighting variances outside the critical subset
   that still matter to shared code. Never discard staging or regional behavior
   merely because production appears uniform.
4. Inspect SDK evaluation semantics and application behavior. Trace literal keys,
   constants, wrappers, dynamically constructed keys, variation-detail calls and
   all-flags consumers. For each call site, record expected type, supplied default,
   initialization readiness, offline mode, missing-flag/error paths and cached
   behavior. A remote forward value does not prove equivalence to SDK fallback
   values. Removing evaluation may also remove tracking, hooks or other side
   effects; identify these explicitly. If preservation requires a behavior change,
   stop and describe the decision requiring owner approval.
5. Use lifecycle status, recent evaluations and code-reference metadata only as
   supporting evidence. An active/launched label or zero recent traffic cannot
   establish readiness by itself. Do not invent rollout history, evaluation counts
   or audit results. If logs or approvals are inaccessible, mark them unverified.
   Document the typed surviving value and evidence for every environment/context
   path, including failure modes. Conflicting values, active rollouts, unresolved
   prerequisites or stale snapshots yield NOT READY or BLOCKED, not a guess.
6. Before authorized edits, capture baseline tests for both existing branches and
   SDK error/default paths. Define expected after-removal behavior explicitly.
   Recheck snapshot freshness and revision immediately before making changes;
   configuration drift invalidates the earlier decision. Replace evaluations only
   with the justified value or surviving branch. Remove directly dead imports,
   constants and tests only when their exclusive ownership is established. Preserve
   unrelated SDK consumers, generated-code boundaries and repository conventions.
   Dynamic keys and external references require an explicit residual-risk note.
7. Run before/after behavioral tests, affected unit/integration tests, type checks
   and repository-native validation. Review the scoped diff for accidental business
   logic changes, missing failure behavior and unrelated cleanup. Repeat reference
   discovery and explain any retained matches. Missing runtime access or failed
   tests prevents a verified-ready verdict. Describe a code rollback and note that
   restoring code may depend on retained flag configuration; do not delete that
   configuration automatically.
8. Draft a PR description with exact project/flag, snapshot identity and time,
   environment behavior table, typed forward value, prerequisite/dependent audit,
   changed call sites, actual tests, uncertainties and reviewer checks. Creating a
   PR, posting messages, archiving/deleting flags or changing remote configuration
   requires separate explicit authorization. Local code-edit permission does not
   grant those writes. If authorized later, verify each external effect by reading
   back the exact target. Do not commit or push in the assessment workflow.

Return READY FOR REVIEW, NOT READY, or BLOCKED with evidence for each gate.
Separate observed configuration, inferred behavior and unverified assumptions;
never describe this assessment as a completed rollout audit without its evidence.
```

## How It Works

The removal decision compares typed behavior across environments, contexts and SDK failure modes. Freshness and nonempty-scope gates prevent stale or incomplete configuration from authorizing irreversible cleanup.

## Variables

- `[repository, project key and exact flag key]`: exact code and remote target.
- `[authorized environments and critical-environment set]`: complete permitted comparison scope.
- `[snapshot timestamp, revision and maximum age]`: evidence freshness contract.
- `[read access, local edits, tests and separately authorized writes]`: distinct permissions.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
