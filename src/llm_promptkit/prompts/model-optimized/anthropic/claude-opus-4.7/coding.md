---
category: "model-optimized"
title: "Claude Opus 4.7: Coding"
subcategory: "anthropic"
model: "claude-opus-4.7"
source: "promptkit-authored"
---
# Claude Opus 4.7: Coding

## When to Use

Use this template when `claude-opus-4-7` is the coding model in a tool-using harness and the job is a bounded implementation or a strict review, not a multi-hour migration (that is [long-horizon](long-horizon.md)) and not a pure RCA (that is [reasoning](reasoning.md)). Vendor status: active legacy, API ID `claude-opus-4-7`, 1M context, 128K max output, adaptive thinking, default effort `high`, text and image in / text out, knowledge cutoff January 2026. Anthropic recommends considering Opus 5.5. Computer-use and subagents exist only if the harness actually provides them; naming them here does not create them.

Do not use this file to claim 8-hour autonomous sessions, cost ratios versus other vendors, or megapixel vision scores. Those appeared in the retired stub and are not documented guarantees. If the environment has no shell or patch tool, demand a reviewable patch and an explicit list of checks not run.

## The Prompt

```
Complete [engineering task] in [repository] using only the tools this
environment actually exposes.

Acceptance criteria: [observable behaviors]
Editable paths: [allowlist]
Public contracts to preserve: [APIs, schemas, platforms]
Verification commands: [tests, types, linters]
Approval boundaries: [network, deploy, production data]
Image evidence (optional): [screenshot or none]

Read repository instructions and inspect the affected paths before editing.
Apply every acceptance criterion to every affected component; do not assume a
requirement applies only to the first file mentioned. Prefer tool output over
extended reasoning when a command can falsify a claim. Adaptive thinking and
effort belong in the API request (default effort high), not as a fake field in
this message.

Implementation loop:
1. State the smallest change that could meet acceptance.
2. Edit only allowlisted paths. Preserve unrelated working-tree work.
3. Run the verification commands after each meaningful change. Use the actual
   failure output to decide the next edit.
4. If a command is unavailable, record it as unrun. Never invent logs.
5. Pause at approval boundaries. Three failed attempts on the same error with
   no new evidence is a blocker, not a license to widen scope.

Final response: files changed, behavior delivered, exact commands and outcomes,
remaining blockers. Do not deploy. Do not substitute a plan for a result.
```

## How It Works

Opus 4.7 is documented as a long-context, high-effort coding model that follows instructions tightly. The prompt therefore repeats scope across “every affected component,” because literal models otherwise implement the first bullet and ignore the rest—the same issue Anthropic calls out in later Opus prompting guides. The loop ties each edit to a real command so thinking tokens cannot stand in for a test. Allowlists and approval boundaries stop the retired stub’s “full autonomy / do not ask questions” instruction from reading as permission to push, migrate production data, or rewrite the tree. Image evidence is optional and must be attached if cited; 4.7 accepts images, but a prose description of a UI is not a screenshot. Stop rules (unrun checks, three similar failures, no deploy) keep the delivery note honest. Effort and thinking remain request parameters.

## Variables

- `[engineering task]`: one feature or defect, with edge cases.
- `[repository]`: path or snapshot the tools can see.
- `[observable behaviors]`: user-visible or API-visible acceptance.
- `[allowlist]`: writable paths; everything else is read-only.
- `[APIs, schemas, platforms]`: compatibility that must not regress.
- `[tests, types, linters]`: commands that exist in this environment.
- `[network, deploy, production data]`: hard stops.
- `[screenshot or none]`: attach media or write `none`.

## Related

Living siblings: [long-horizon](long-horizon.md), [reasoning](reasoning.md), [analysis](analysis.md). Later champion: `claude-opus-4.8/coding.md`.

Grounded 2026-11-02 against the [Opus 4.7 overview](https://platform.claude.com/docs/en/models/opus-4-7/overview) and [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
