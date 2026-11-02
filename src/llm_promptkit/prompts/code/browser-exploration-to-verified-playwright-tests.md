---
category: "code"
title: "Browser Exploration to Verified Playwright Tests"
source: "github/awesome-copilot"
license: "MIT"
---
# Browser Exploration to Verified Playwright Tests

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/playwright-explore-website/SKILL.md (MIT)
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/playwright-generate-test/SKILL.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Turn observed behavior in a test website into executable Playwright TypeScript tests. Requires browser tools, a runnable test project and safe fixtures; a scenario description alone is not evidence that selectors or assertions work.

## The Prompt

```text
Explore the allowed website flows, then generate and execute Playwright tests.
Test URL and environment: [URL, test tenant and allowed origin boundaries]
Flows and intended assertions: [3–5 core flows, or a narrower supplied scenario]
Fixtures: [safe accounts/data, approved upload fixtures and reset procedure]
Repository and runner: [test root, existing Playwright configuration/command]
Budget: [time limit and maximum repair/rerun cycles; default two cycles]
Approval boundaries: [authorized actions and consequential-operation approvals]

1. Validate the URL, scope, fixtures and runner. Inspect repository instructions,
   installed Playwright version, test conventions and authentication setup.
   Discover live browser-tool schemas instead of inventing a tool name. If a
   required input or capability is missing, report BLOCKED; do not fabricate
   browser observations or test execution. Do not install dependencies implicitly.
2. Before interacting, identify consequential actions. Require explicit approval
   covering the exact action, destination and data before submissions or uploads
   that send messages/files, change permissions, place orders, incur charges or
   otherwise affect real records. Do not assume a label saying test is sufficient.
   Generated tests must respect the same boundary on every execution, including
   retries. Use isolated fixtures or mocks for unapproved consequential actions;
   clearly label mocked coverage, and do not claim the real action was verified.
3. With the available browser tools, execute allowed steps one by one. Observe
   the live DOM/accessibility state before selecting locators. Record role/name,
   label, test ID or other actually observed locator, action, state transition,
   visible result and evidence reference for each step. Prefer stable user-facing
   locators and web-first waiting over brittle guessed selectors or fixed sleeps.
   Separate observed behavior from intended requirements; discrepancies are
   findings, not permission to rewrite the expected result.
4. Only after observing the relevant flow and locators, write a TypeScript test
   using @playwright/test in the repository's test directory. Preserve intended
   assertions and identify any unobserved or blocked steps explicitly. Follow
   existing fixtures, baseURL, setup and cleanup conventions. Keep tests isolated,
   data reproducible and credentials out of source and traces. Do not generate
   guessed tests for flows that were never observed.
5. Execute the generated file using the actual project runner. Preserve exact
   command, browser/project, output, exit status and trace/screenshot references.
   Inspect failures before editing. Within the budget, fix verified locator,
   synchronization or fixture mistakes and rerun. Count runner-configured retries
   in the total execution budget. Do not weaken/remove assertions, add skips,
   endlessly retry or change expected behavior merely to get green. Report an
   application defect or unresolved environment failure honestly when applicable.
6. Close the exploration browser context in finally-style cleanup even on a
   blocked step or failure. Ensure test-owned contexts/processes also terminate;
   report any cleanup failure. Reset only fixtures/resources owned by this run
   using the approved procedure. Do not close unrelated sessions.

Deliver:
- Exploration table: flow/step | observed locator/action | expected assertion |
  observed result | evidence | approval/coverage limitation.
- Generated test path(s) and mapping from assertions to observed steps.
- Exact execution results, retries/repair cycles used, preserved artifacts and
  failures or blocked checks. Claim verified only for actually executed passing
  tests, and distinguish browser observations from automated-test coverage.
- Cleanup result and remaining risks. Do not commit, publish or deploy.
```

## How It Works

Exploration supplies real locators and state transitions before code generation. Executing the resulting tests closes the gap between a plausible test and a passing artifact, while bounded repairs preserve the intended behavioral assertions rather than optimizing away failures.

## Variables

- `[URL, test tenant and allowed origin boundaries]`: approved browser target and navigation scope.
- `[3–5 core flows, or a narrower supplied scenario]`: behaviors and assertions to preserve.
- `[safe accounts/data, approved upload fixtures and reset procedure]`: isolated, permitted test data.
- `[test root, existing Playwright configuration/command]`: real project execution route.
- `[time limit and maximum repair/rerun cycles; default two cycles]`: bounded exploration and execution cost.
- `[authorized actions and consequential-operation approvals]`: exact side-effect permissions.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
