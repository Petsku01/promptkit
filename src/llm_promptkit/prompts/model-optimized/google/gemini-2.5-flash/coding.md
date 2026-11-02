---
category: "model-optimized"
title: "Gemini 2.5 Flash: Coding"
subcategory: "google"
model: "gemini-2.5-flash"
source: "promptkit-authored"
---
# Gemini 2.5 Flash: Coding

## When to Use

Use this template on `gemini-2.5-flash` for focused coding, review, or debug when you need Flash latency and the 2.5 thinking stack rather than Gemini 3.8 Flash. Google still serves 2.5 Flash for accounts that already used it; it is **not deprecated**, but new projects are directed to 3.5 Flash-Lite or 3.8 Flash. Documented limits: 1,048,576 input tokens, 65,536 output tokens (separate budgets, unlike Gemini 4’s shared 1M). Inputs: text, images, video, audio. Output: text. Supported: caching, code execution, file search, function calling, Maps and Search grounding, structured outputs, thinking, URL context. Not supported: audio generation, image generation, Live API.

Prefer [long-context](long-context.md) for repo-scale Q&A without edits, [quick-tasks](quick-tasks.md) for classify/extract, and 2.5 Pro / 3.8 Flash templates for deeper architecture. Attach screenshots if the bug is visual; a caption is not media.

## The Prompt

```
Write or fix [language] code for [task].

Requirements:
1. [req]
2. [req]
Runtime: [framework, versions]
Editable surface: [files or snippet]
Media (optional): [attached screenshot/recording or none]
Verification: [tests or "none in this environment"]
Thinking: set thinking_level / thinking_budget in the API for this 2.5
model; do not paste a fake parameter here.

Instructions:
- Keep the change minimal. Match existing style.
- If media is attached, map the visible failure to a code path before
  patching. If media is missing, do not invent UI copy.
- Add a regression test only when a test runner exists.
- Use code execution or function calling only if this client enabled them.
- Put the user question after the code context when the prompt is long
  (Google long-context guidance).
- Stop after: summary, code/diff, verification status (ran / not run),
  residual risk. No tutorial.

If a requirement conflicts, name the conflict instead of guessing.
```

## How It Works

Google positions 2.5 Flash as the price-performance model for low-latency, high-volume work that still needs thinking. The prompt stays one-task, numbered requirements, and honest verification because Flash will happily emit code-shaped text without a compiler. Thinking is a request field on 2.5 (budget or level depending on SDK vintage); later 3.x docs replace budget with `thinking_level`—check the SDK you actually call. Long prompts should place the question last. Tools (Search, code execution, URL context) are no-ops unless the application enabled them. Access is limited to prior 2.5 users; this template does not reopen a gated project.

## Variables

- `[language]` / `[task]`: language and goal.
- `[req]`: numbered musts.
- `[framework, versions]`: stack freeze.
- `[files or snippet]`: write scope.
- `[attached screenshot/recording or none]`: media honesty.
- `[tests or "none in this environment"]`: verification path.

## Related

[long-context](long-context.md), [quick-tasks](quick-tasks.md). Living 2.5 Pro: `../gemini-2.5-pro/coding.md`. Current Flash champion: `../gemini-3.8-flash/coding.md`.

Grounded 2026-11-02 against the [Gemini 2.5 Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) and [long context](https://ai.google.dev/gemini-api/docs/long-context) (last updated 2026-10-29 / 2026-10-15).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
