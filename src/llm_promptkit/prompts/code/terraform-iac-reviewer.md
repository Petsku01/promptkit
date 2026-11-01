---
category: "code"
title: "Terraform Plan and State Safety Review"
source: "github/awesome-copilot"
license: "MIT"
---
# Terraform Plan and State Safety Review

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/terraform-iac-reviewer.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Review Terraform configuration, state-management controls, and a proposed plan before a human decides whether to authorize infrastructure changes.

## The Prompt

```text
Review Terraform infrastructure changes without deploying or mutating state.
Configuration scope: [checkout, root modules and proposed diff]
Authorized target: [backend, workspace, cloud account, region and environment]
Version context: [Terraform CLI, providers, modules and lockfile]
Evidence: [existing plan artifact, policy results and recovery procedures]
Execution allowance: [offline checks or explicitly approved diagnostic commands]

1. Confirm the precise root module and target identity from configuration and
   provided evidence. Distinguish backend credentials from provider credentials;
   they can address different accounts. Record workspace-to-state mapping,
   variable sources, provider aliases, dependencies and blast radius. If target
   identity, effective access or approval scope is ambiguous, stop live commands
   and report the missing evidence. Continue repository-only review separately.
   Review-only means no configuration edits, deployment, state writes or repairs.
2. Inspect backend encryption, access controls, locking and recovery arrangements.
   Remote state can contain secrets even when outputs are marked sensitive.
   terraform_remote_state consumers may need access to the full state snapshot;
   output sensitivity is not an authorization boundary. Recommend a narrower
   published interface when full-state access would exceed the consumer's needs.
   Do not retrieve or paste raw state, secret variables or complete plan JSON
   into a public report. Keep any approved artifacts access-controlled.
3. Verify locking against official documentation for the exact backend and CLI.
   For supported S3 backend versions, native locking is opt-in with use_lockfile;
   merely selecting S3 does not enable it. Current guidance deprecates DynamoDB
   locking; older clients may require a staged migration with both mechanisms.
   Confirm all writers' compatibility and lock-object permissions before proposing
   migration. Do not change backend settings, disable locks or force-unlock here.
   Check bucket versioning and a tested recovery process rather than assuming
   a code revert can recover deleted data or restore resource identity.
4. Inspect provider/module version constraints, lockfile changes, resource lifecycle,
   moved/import declarations, IAM scope, public exposure, encryption, secret handling
   and sensitive outputs. Prefer specific risks over formatting preferences. Flag
   provisioners, external data programs and provider behavior that may execute code
   or contact services even during validation/planning. Static checks are not proof
   that a plan is harmless or that credentials are safely restricted.
5. Use supplied evidence first. Within the explicit execution allowance, run format
   check, validate and the project's established security/policy scanner. Report
   versions, commands, results and skipped prerequisites. Initialization can download
   and execute untrusted provider code or alter local artifacts; do not initialize
   or migrate a backend without permission. Planning may read live infrastructure,
   execute data sources and create lock objects: request authorization if absent.
   Never use routine terraform refresh, refresh-only apply, import, state surgery,
   destroy or targeted recreate as a harmless diagnostic or generic rollback.
6. If authorized, generate a saved plan before any future apply. Review that exact
   artifact and its provenance: configuration revision, variable inputs, target,
   creation time and integrity identifier. Summarize add/change/destroy counts,
   replacements, unknown values, drift, dependent consumers and irreversible data
   risks. Distinguish a plan command failure from the documented detailed-exit-code
   result indicating changes. Missing policy evidence, unexpected deletion, stale
   state or mismatched target is a no-go, not a reason to bypass a gate.
7. End this review with a verdict and explicit human approval requirements. A later
   apply is a separately authorized step tied to the exact reviewed saved plan,
   never an automatic continuation. State-changing recovery and destroy require
   their own human approval and, where applicable, reviewed saved plans. Re-plan
   after any relevant inputs change. After an authorized apply, read back the exact
   target and verify expected resources and service behavior before claiming success.

Return a target/provenance summary, plan-action ledger, prioritized policy/state
findings, validation evidence, recovery limitations and GO/NO-GO conditions.
Separate observed facts from recommendations; include approval owner and every
blocked or skipped check. Do not declare infrastructure deployed in a review.
```

## How It Works

Target identity, version-aware locking, and saved-plan provenance are independent gates. The default artifact is a review, not a deployment script. S3 guidance should be rechecked for the actual CLI against https://developer.hashicorp.com/terraform/language/backend/s3.

## Variables

- `[checkout, root modules and proposed diff]`: review boundary.
- `[backend, workspace, cloud account, region and environment]`: exact state and infrastructure target.
- `[Terraform CLI, providers, modules and lockfile]`: compatibility inputs.
- `[existing plan artifact, policy results and recovery procedures]`: evidence to inspect safely.
- `[offline checks or explicitly approved diagnostic commands]`: permitted actions, excluding deployment by default.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
