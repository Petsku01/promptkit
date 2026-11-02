# o3-mini

## Characteristics

**Historical guide: OpenAI shut down o3-mini on 23 October 2026.** The deprecation was announced on 22 April 2026; OpenAI names `gpt-5.6-sol` as the substitute. Do not present this folder as a currently available cheaper reasoning endpoint or use its name to infer what a third-party alias serves.

The historical model page documents text input and output, a 200,000-token context window, up to 100,000 output tokens, and an October 2023 knowledge cutoff. Structured Outputs, function calling, and Batch were supported; image input was not. These specifications describe the retired SKU rather than a promise about its replacement.

## Key Rules

State the problem, constraints, required answer format, and a checkable success criterion directly. Do not demand a private chain-of-thought transcript or rely on “think step by step” as an API control. Reasoning effort and token budgets belong in the client when supported by the actual model.

## Prompt Style

Use [reasoning.md](reasoning.md) only for a historical evaluation, preserved deployment, or migration comparison with the underlying model clearly identified. The template asks for an answer and concise verification, with an explicit path for missing evidence and conflicting constraints.

## Use Cases

The retained workflow covers math, logic, code diagnosis, and constrained decisions. Supply the relevant evidence, preserve uncertainty, and distinguish suggested tests from checks actually run. A prompt does not grant search or execution access.

## Compared to o1/o3

Do not carry historical price or latency comparisons into current purchasing decisions. Evaluate the replacement independently against the real workload; this promptkit-authored file remains not model-tested.

## Primary Sources

Audit-verified 2026-11-02: [o3-mini model page](https://platform.openai.com/docs/models/o3-mini) and [OpenAI deprecations](https://platform.openai.com/docs/deprecations).
