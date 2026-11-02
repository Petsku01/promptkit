---
category: "model-optimized"
title: "Llama 3.3: Coding"
subcategory: "meta"
model: "llama-3.3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Meta](../index.md)

# Llama 3.3: Coding

## When to Use

Use this template with Llama 3.3 70B Instruct for generate, review, debug, or refactor inside a **128k** window. The card lists code as a documented evaluation area (HumanEval / MBPP figures are vendor numbers—do not copy them into the prompt or claim them as promptkit results). Builtin **Code Interpreter** is a 3.1-compatible tool path: the model emits Python for an executor you attach; this prompt does not assume that executor exists. Zero-shot custom function calling uses the 3.2-style `[func(param=value)]` format in system or user text.

Keep jobs to a module or a focused diff. Prefer Llama 4 coding templates for current Meta weights, and Llama 3.2 general for on-device 1B/3B. Analysis of non-code documents belongs in [analysis](analysis.md).

## The Prompt

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You write or repair code. Match the stated interface. Do not claim
tests passed unless an executor in this environment ran them. Code
Interpreter is off unless the user listed it.

<|eot_id|><|start_header_id|>user<|end_header_id|>

Language: [language]
Task: [purpose]
Interface:
- Inputs: [parameters]
- Outputs: [return or side effects]
- Errors: [what must raise or return]
Constraints:
- Edges: [list]
- Style: [conventions]
- Editable surface: [snippet or files]
Existing code or error (optional):
[paste]

Procedure:
1. Restate the interface.
2. If existing code is present, name the defect in one sentence before
   editing. Do not rewrite unrelated functions.
3. Emit one complete, compilable artifact or a unified diff.
4. Tests in [framework]: happy, edge, error. Label them suggested
   unless a harness ran them.
5. If a constraint cannot be met, stop and name it.

No preamble. No invented pass output.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## How It Works

The retired stub stacked generate/review/debug/refactor without a stop rule. 3.3 70B will produce plausible code; the interface plus honest test status is what makes the template evaluable. Special-token headers keep the same format as 3.1 so hosted and local stacks that already wrap Llama 3 chat templates do not double-wrap if you send only the inner user body—if your server injects headers, strip them from this text and keep the procedure. Builtin Code Interpreter ends tool turns with `<|eom_id|>` in 3.1 docs; this coding job is ordinary assistant text ending `<|eot_id|>`. Custom function calls, if you add them, use `[func(param=value)]` and no other text in that turn. Vendor HumanEval / MBPP rows on the card are Meta’s evals; do not treat them as a guarantee that this prompt scores the same. 128k is a module window, not a monorepo dump.

## Stop rules

Stop when a constraint cannot be met, when tests did not run, or when the editable surface is exceeded. Do not assume Code Interpreter executed Python. Do not paste Meta’s HumanEval row as a self-score. If the host already wraps Llama 3 headers, send only the procedure body to avoid double special tokens. 128k is not a monorepo. Prefer Llama 4 coding for current Meta open weights.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges.
- `[conventions]`: style.
- `[snippet or files]`: write scope.
- `[framework]`: test runner or none.

## Related

[analysis](analysis.md). Llama 3.2: `../llama-3.2/`. Llama 4: `../llama-4/coding.md`.

Grounded 2026-11-02 against [Llama 3.3 prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/) (3.1-compatible template, builtin Code Interpreter) and the [Llama 3.3 model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
