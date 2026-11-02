---
category: "model-optimized"
title: "DeepSeek V3: Coding"
subcategory: "deepseek"
model: "deepseek-v3"
source: "promptkit-authored"
---
# DeepSeek V3: Coding

## When to Use

Use this template for DeepSeek-V3 instruct coding: generate, review, debug, or add tests inside a 128K context, on local weights or a residual V3 endpoint. The model card highlights code and math as strong vendor-eval areas and notes distillation from R1-style reasoning into a normal chat model, so a short plan-then-code user prompt is appropriate—without R1’s empty-system rule and without V4 Pro’s 1M agent loop. Prefer [json-output](json-output.md) when the artifact is schema-constrained data, [math](math.md) when the artifact is a derivation, and V4.x files when the runtime is `deepseek-flash` or `deepseek-v4-pro`.

Do not claim SWE-bench or HumanEval rates in the prompt. Do not assume tools exist; V3 chat does not magically run pytest.

## The Prompt

```
Write or repair [language] code for [purpose].

Interface:
- Inputs: [parameters]
- Outputs: [return or side effects]
- Errors: [what must raise or return]

Constraints:
- Edge cases: [list]
- Complexity target: [optional big-O]
- Style: [project conventions or "standard library only"]
- Editable surface: [snippet / files]

Existing code or error (optional):
[paste]

Procedure:
1. Restate the interface and name edge cases you will handle.
2. If existing code is present, state the defect in one sentence before
   editing. Do not rewrite unrelated functions.
3. Emit one complete, compilable artifact (or a unified diff) that meets
   the interface.
4. Provide tests in [framework]: happy path, edge, error. Mark them as
   suggested unless a harness ran them.
5. If a constraint cannot be met, stop and say which one. No pseudo-code
   disguised as a solution.

Do not open with praise. Do not invent passing test output.
```

## How It Works

The retired V3 coding stub was a stack of unlabeled skeletons (generate/review/debug/refactor/algorithm/tests) with no stop rule. This rewrite keeps one procedure that covers those jobs by optional “existing code or error,” and it binds the model to an interface plus honest test status. V3 can follow a system prompt; keep it light if you set one (“you write code”) and put the contract in the user message so evals stay portable. 128K is enough for a module, not a monorepo—say so in the editable surface. Distilled reasoning helps on algorithms; it does not replace running the compiler.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges the author cares about.
- `[optional big-O]`: omit if irrelevant.
- `[project conventions or "standard library only"]`: style freeze.
- `[snippet / files]`: what the model is allowed to change.
- `[framework]`: pytest, junit, jest, etc.

## Related

[analysis](analysis.md), [math](math.md), living [json-output](json-output.md). Agent-style coding: `deepseek-v4-pro/coding.md`.

Grounded 2026-11-02 against [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
