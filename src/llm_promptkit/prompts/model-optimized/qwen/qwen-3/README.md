# Qwen 3

## Features

Qwen3's April 2025 release includes dense 0.6B, 1.7B, 4B, 8B, 14B, and 32B models plus the 30B-A3B and 235B-A22B mixture-of-experts variants. Context is SKU-dependent: 0.6B, 1.7B, and 4B have 32K; 8B and larger dense models and both MoE variants have 128K. Check the actual serving configuration rather than assigning one limit to the whole family.

The release documents hybrid thinking and coverage of **119 languages**. Do not transfer Qwen3.5's 201-language claim or its vision encoder to these earlier models. This directory preserves the Qwen3 generation; newer Qwen3.8 templates live in separate folders.

## Prompts

- [Coding](coding.md): interface-first generation, repair, and explicit acceptance checks.
- [Multilingual](multilingual.md): source/target language contracts, terminology preservation, and ambiguity handling.

These are dedicated Qwen3 workflows, not instructions to substitute Qwen2.5 files. Select one artifact, fill the variables, and stop at the stated boundary. Provide missing source material before expecting a reliable translation or implementation.

## MoE Models (30B-A3B, 235B-A22B)

Only a subset of parameters is activated per token, but that architectural fact does not guarantee a particular latency or quality on your hardware. Match the exact model, context, and output budget to the job and measure results locally.

## Qwen3-Coder

Qwen3-Coder is a separate coding variant, not another name for every Qwen3 checkpoint. Check its own model card and serving contract before transferring settings. For compatible Qwen3 chat templates, `/think` and `/no_think` control mode as documented; configure sampling in the client and do not fabricate tool execution. These re-authored prompts remain not model-tested.

## Primary Sources

Audit-verified 2026-11-02: [official Qwen3 release](https://qwenlm.github.io/blog/qwen3/).
