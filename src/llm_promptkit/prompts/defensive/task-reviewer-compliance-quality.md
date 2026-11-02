---
category: "defensive"
title: "Task-Scoped Review with Separate Compliance and Quality Verdicts"
source: "obra/superpowers"
license: "MIT"
---
# Task-Scoped Review with Separate Compliance and Quality Verdicts

**Category:** defensive
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/subagent-driven-development/task-reviewer-prompt.md (MIT)

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).

## When to Use

Review one implementation task against its brief and binding global constraints, independently of the author's confidence. This is a task gate, not a whole-branch merge approval.

## The Prompt

```text
Review one task's implementation for specification compliance and code quality.
Task brief: [complete task brief and acceptance criteria]
Global constraints: [binding specification requirements]
Author report: [implementation report and claimed validation]
Fixed revisions: [full BASE SHA and full HEAD SHA]
Review package: [complete BASE-to-HEAD diff, commit list and file summary]
Test permissions: [authorized commands, budgets and isolated environment]

1. Verify the review inputs before grading. Require the task brief, exact global
   constraints, author report, fixed full BASE/HEAD revisions and complete diff.
   Confirm both revisions exist in the intended repository and the package is
   their actual change, not a truncated paste, unrelated range or moving branch
   name. Read the entire task diff, including added/deleted files, modes, renames,
   binary changes and relevant generated artifacts. Retrieve missing portions
   using read-only commands when possible. If completeness or revision identity
   cannot be established, report BLOCKED rather than approving an unseen change.
2. Keep this checkout, index, HEAD and branches read-only. Do not fix files,
   format, install packages, regenerate artifacts, update snapshots, stage,
   checkout, commit or change branch state. Avoid tools that silently refresh
   repository state. Tests that generate files, caches or snapshots require an
   isolated approved environment containing the exact reviewed revision. Do not
   create an environment or run side-effecting/network tests without permission.
   If safe execution is unavailable, name the missing evidence and validation
   needed; never substitute invented test output.
3. Treat the author's report as claims, including statements such as “all tests
   pass,” “deliberately simple,” or “out of scope.” Compare each claim to code
   and binding requirements. Claimed passing tests are not verified evidence
   without accessible logs, commands, environment and a revision matching HEAD.
   Inspect referenced logs rather than assuming absent or truncated evidence
   does not exist. Distinguish author-reported results, inspected execution logs,
   and tests you personally ran. A valid existing run can avoid duplicate work;
   it does not prevent appropriately authorized independent testing when needed.
4. Inspect relevant unchanged definitions, callers, interfaces and tests when
   necessary to judge a concrete risk. Reread a changed function or follow a
   call chain as deeply as the risk requires; there is no “read once” limit.
   Keep reads focused on this task, naming the reason for expanded inspection.
   For API, lock-ordering, lifecycle or shared-state changes, inspect affected
   call sites rather than approving solely from isolated hunks. Do not turn
   this gate into an unbounded repository audit or whole-branch review.
5. Assess specification compliance independently of elegance. Map every task
   requirement and global constraint to implementation and test evidence.
   Classify discrepancies as Missing, Extra or Misunderstood. In a batched brief,
   inspect each listed file/change; an untouched file may mean missing work,
   but unchanged code can already satisfy a requirement when verified. Explain
   that evidence rather than demanding a meaningless edit. Separate requirements
   that remain unverifiable from actual noncompliance. Never mark an unknown
   requirement satisfied simply because the rest of the patch looks correct.
6. Assess code quality on its merits: correctness, error handling, state and
   resource lifecycle, security boundaries, relevant performance, clear interfaces
   and maintainability. Check whether tests assert observable behavior, cover
   meaningful boundaries and fail for the intended reason. Mocks are legitimate
   isolation tools, not defects by themselves; identify what a mock conceals if
   it weakens a contract. Prefer established conventions and scoped improvements
   over speculative abstractions. Do not flag pre-existing file size or unrelated
   technical debt as newly introduced damage without a demonstrated connection.
7. Use authorized focused tests to resolve concrete doubts; broader testing is
   allowed when warranted and explicitly within permissions and budget. Execute
   against the fixed reviewed revision in the approved environment, recording
   exact commands and observed results. Test success does not prove uncovered
   contracts. Benign warnings, deprecations or noisy logs are not automatically
   defects: classify their meaning, relevance and policy impact. A warning that
   reveals lost errors or an actual violated requirement is actionable evidence.
8. Calibrate severity: Critical for immediate severe safety/security/data-loss
   risks; Important for incorrect behavior, missed requirements or maintainability
   damage that blocks task acceptance; Minor for nonblocking polish or optional
   coverage. If the approved brief itself mandates defective behavior, label the
   issue plan-mandated and explain the conflict for human resolution. Do not
   downgrade a defect merely because the author supplied a rationale. Cite exact
   file:line evidence at HEAD, or BASE for deleted code, plus observable impact.

Return these sections without process narration:
- Spec compliance: Compliant / Issues found / Blocked, with Missing, Extra and
  Misunderstood findings mapped to requirement IDs and file:line evidence.
- Unverifiable requirements: separate list of evidence gaps and the exact check
  needed, even when verified portions comply. Do not hide them in a quality pass.
- Strengths: specific supported observations, not generic reassurance.
- Quality issues: severity, revision-qualified location, problem, impact and
  minimal remedy. Label suggestions distinctly from acceptance blockers.
- Task quality: Approved / Needs fixes / Blocked, with a concise reason and
  limits of the evidence. This verdict cannot override unresolved compliance.
- Validation ledger: inspected logs, commands actually executed, their revision
  and outcomes, skipped checks and remaining risks.

Do not claim whole-branch merge readiness from this task-scoped review. Approval
applies only to the fixed diff and requirements inspected; later changes require
an updated review rather than reusing this verdict.
```

## How It Works

A fixed diff anchors the evidence. Compliance, unverifiable requirements and quality remain separate so a clean implementation cannot conceal missing scope, and a confident author report cannot masquerade as independently checked validation.

## Variables

- `[complete task brief and acceptance criteria]`: task-scoped requested work.
- `[binding specification requirements]`: exact shared constraints, not inferred defaults.
- `[implementation report and claimed validation]`: claims and log references to verify.
- `[full BASE SHA and full HEAD SHA]`: immutable review endpoints.
- `[complete BASE-to-HEAD diff, commit list and file summary]`: full review package.
- `[authorized commands, budgets and isolated environment]`: permitted validation boundaries.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
