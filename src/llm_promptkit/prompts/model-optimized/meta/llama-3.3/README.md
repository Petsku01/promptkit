# Llama 3.3 (70B) Prompting Guide

## Model Characteristics

Llama 3.3 70B Instruct is a text-only, instruction-tuned model with a documented 128K context window. Meta's card records release on 6 December 2024 and a December 2023 knowledge cutoff. Its supported languages are English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai. There is no pretrained sibling in this release.

Meta describes improvements over Llama 3.1 70B and results approaching Llama 3.1 405B for some applications. That is a vendor comparison, not a universal quality guarantee or a PromptKit benchmark. Llama 4 is the newer Meta family represented elsewhere in this catalog.

## Prompt Files

| Theme | File | Purpose |
|-------|------|---------|
| Analysis | [analysis.md](analysis.md) | Source-grounded comparison, document analysis, and questions |
| Coding | [coding.md](coding.md) | Interface-first generation, repair, review, and proposed tests |

These focused files replace the guide's former collection of generic examples. For analysis, provide identifiable sources and require sourced, inferred, and unknown claims to remain distinguishable. For coding, specify the interface and acceptance checks; generated test suggestions are not evidence that tests ran.

## Key Tips

The chat template follows Llama 3.1. Apply it through the tokenizer or serving client without double-wrapping messages. Tool definitions can be supplied in system or user messages; builtin Brave Search, Wolfram, and Code Interpreter still require actual harness support and authorization. A template cannot enable them by name alone.

Budget input and output against the deployed context, state missing prerequisites explicitly, and stop after the requested artifact. These promptkit-authored workflows remain not model-tested; vendor evaluation tables are not their scores.

## Primary Sources

Model-card basis used by the new files: [Meta Llama 3.3 70B Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct). The audit did not re-fetch its language and cutoff rows.
