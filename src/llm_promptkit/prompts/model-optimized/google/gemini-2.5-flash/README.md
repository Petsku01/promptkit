# Gemini 2.5 Flash

## Features

- **Limits:** 1,048,576 input tokens and 65,536 output tokens in Google's model documentation.
- **Modalities:** text, image, video, and audio input; text output. Audio generation, image generation, and the Live API are not supported by this model.
- **Lifecycle:** not deprecated at the 2026-11-02 audit, but access is gated to prior users. Google directs new projects toward 3.5 Flash-Lite or 3.8 Flash; do not assume a new account can select 2.5 Flash.

## Prompts by theme

| Theme | File |
|-------|------|
| Quick Tasks | [quick-tasks.md](quick-tasks.md) |
| Long Context | [long-context.md](long-context.md) |
| Coding | [coding.md](coding.md) |

## Use cases

Use these templates on an eligible deployment for bounded extraction, classification, document-grounded answers, and code changes. Long-context work should identify documents and evidence locations rather than treating a large input allowance as guaranteed recall. Batch independent items only when output can still be checked item by item.

The documented feature set includes thinking, structured outputs, function calling, caching, code execution, file search, URL context, and Search/Maps grounding. Availability and authorization belong to the actual API configuration; a prompt mentioning search or execution does not enable those tools.

## Tips

Choose one deliverable and state its output contract, evidence boundary, and stop rule. Configure thinking and output budgets in the client. Attach real media when required and report missing attachments instead of inventing observations. For coding, distinguish proposed checks from tests actually executed. For structured extraction, validate the result against the application's schema and keep unsupported fields explicitly unknown.

These templates are promptkit-authored, not vendor benchmark submissions; the re-authored files remain not model-tested.

## Primary Sources

Audit-verified 2026-11-02: [Gemini 2.5 Flash model documentation](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash), updated 2026-10-29.
