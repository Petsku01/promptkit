# Qwen 3.5

## Features

This folder targets official post-trained cards such as `Qwen/Qwen3.5-4B` and `Qwen/Qwen3.5-9B`: causal language models with a **vision encoder**, not a generic edge-only text family. The documented native context is **262,144** tokens, extensible toward **1,010,000** using supported YaRN configuration. Extended context is a serving option, not a capability unlocked by wording in a prompt.

Thinking is enabled by default. The card advises keeping at least 128K context available so thinking does not collapse. Configure the actual engine and budget input, reasoning, and final output together. Do not silently identify these models with Qwen3 or Qwen3.8.

## Prompts by theme

| Theme | File |
|-------|------|
| Basic tasks | [basic.md](basic.md) |
| Coding | [coding.md](coding.md) |
| JSON output | [json-output.md](json-output.md) |

Choose basic tasks for classification, extraction, summaries, and language identification; coding for implementation or repair; JSON output for a schema-shaped artifact. Supply actual images when a task needs them and declare when no media is attached.

## Task and Thinking Rules

Keep one deliverable and an explicit insufficiency path, not an arbitrary universal prompt-length cap. For short basic jobs, disable thinking through the client's supported `enable_thinking` or instruct-mode setting. For reasoning-dependent coding, retain an appropriate budget. Sampling and parsers belong in the runtime; a JSON request still needs application-side validation.

## Deployment Recommendations

Check the exact checkpoint, vision support, configured window, and chat template rather than inferring capability from parameter size alone. The model card's benchmark rows are vendor results, not evidence for these templates. The re-authored files remain not model-tested.

## Primary Sources

Audit-verified 2026-11-02: [4B model card](https://huggingface.co/Qwen/Qwen3.5-4B), [9B model card](https://huggingface.co/Qwen/Qwen3.5-9B), and [vendor blog](https://qwen.ai/blog?id=qwen3.5).
