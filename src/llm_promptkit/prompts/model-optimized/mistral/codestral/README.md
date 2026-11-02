# Codestral

## Characteristics

This guide targets **Codestral 25.08**, the Premier code-specialized model identified as `codestral-2508`, released at the end of July 2025. Mistral documents a **128K** context window for that version. Do not apply an older Codestral release's window or deployment assumptions to this ID, and verify what an unversioned provider alias actually serves.

The documented capabilities include fill-in-the-middle completion, structured outputs, function calling, predicted outputs, prefix completion, and batch processing. These are serving features, not switches that natural-language instructions can activate. Vendor capability descriptions do not establish a success rate for these templates.

## Prompt Examples

### Code Generation

Use [coding.md](coding.md) with the language, public interface, constraints, surrounding code, and acceptance checks. Request one implementation or patch and distinguish code produced from code actually tested.

### Code Explanation

Supply the relevant code and ask for behavior, assumptions, and concrete failure cases. Do not infer repository structure, dependency versions, or runtime output that was not provided.

### Code Review

Provide the intended contract and relevant tests. Require findings tied to specific code locations and separate confirmed defects from proposed improvements. Stop rather than inventing missing execution evidence.

### Fill-in-the-Middle

Use Mistral's `/v1/fim/completions` endpoint with real prefix and suffix fields for native FIM. A literal placeholder pasted into a chat request is not an equivalent API operation; choose chat generation when the client cannot issue FIM requests.

## Tips

Configure sampling, tools, and context budgets in the client. Validate structured output and execute suggested checks in the real project before claiming success. The re-authored coding file is not model-tested.

## Primary Sources

Audit-verified 2026-11-02: [Codestral 25.08 documentation](https://docs.mistral.ai/models/codestral-25-08).
