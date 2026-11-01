---
category: "debug"
title: "MCP Server Release QA with Live Protocol Evidence"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Debug Prompts](../index.md)

# MCP Server Release QA with Live Protocol Evidence

**Category:** debug
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/mcp-release-qa/SKILL.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Before releasing an MCP server, verify its actual protocol session, published capability inventory, failure behavior, and installation path. Requires an executable candidate and a safe sandbox; source inspection alone cannot establish release readiness.

## The Prompt

```text
Perform evidence-driven release QA for this MCP server.
Candidate checkout and revision: [checkout and candidate revision]
Transport and entry point: [transport, command or endpoint]
Sandbox configuration: [fixtures, permitted operations, redacted environment]
Budget and approvals: [time limit, installation/network permissions]

1. Establish the candidate's actual revision, working-tree changes, build commands,
   registration sources, manifests, documentation and supported protocol revisions.
   Use repository-native tests where available. Read revision-matched protocol/SDK
   documentation: derive expected errors, negotiation, lifecycle and transport
   behavior from that revision, not from a universal checklist or remembered SDK.
   Inspect commands before execution; stay inside the authorized sandbox.
2. Build and start a fresh candidate server. Preserve exact commands, stdout,
   stderr, exit status and redacted configuration names. For STDIO, stdout must
   remain protocol-only; documented stderr diagnostics are NOT failures by
   themselves. Evaluate unexpected diagnostics for actual errors or secret leaks.
   For HTTP, record relevant status/headers and session handling, redacting tokens.
3. Through a real client, keep initialize, negotiated capabilities,
   notifications/initialized, ping, discovery and invocations in one valid
   session. Do not substitute independent one-shot processes. Follow every cursor
   for supported tools/list, resources/list, resources/templates/list and
   prompts/list. Exercise at least one read-only item per advertised capability
   class. Mark unsupported classes not applicable rather than inventing them.
4. Build a parity table keyed by stable identifier: source registration | live
   discovery | generated metadata | public documentation. Compare names,
   descriptions, input/output schemas, required arguments, annotations, URIs and
   MIME types. Read resources and retrieve prompts with valid arguments. Check
   output schemas where published. Generated-file refreshes require write
   authorization; otherwise report drift without editing the candidate.
5. In separately identified disposable negative-test sessions where necessary,
   probe lifecycle violations, malformed envelopes, unknown methods/names,
   unsupported revisions, repeated initialization, missing/wrong-type/extra or
   out-of-bounds arguments, documented size limits and controlled internal errors.
   Use revision-specific expected behavior: negotiation may differ from rejection.
   Record request IDs, raw redacted responses, client/process status and observed
   sandbox state. Verify no unintended successful side effects or secret leakage.
   Never call mutation-capable tools on production data. If safe failure injection
   is unavailable, mark that case blocked rather than manufacture evidence.
6. If installation is published and authorized, install exactly as documented
   into an owned temporary destination outside the checkout. Start that artifact
   independently of source files; repeat initialization, discovery and one safe
   call. Preserve logs, then clean up only resources created by this run. Stop
   owned servers/clients in a finally-style cleanup, including after failure.

Return:
- Candidate identity, transport, negotiated revision and scoped verdict:
  PASS / PASS WITH CAVEATS / FAIL / BLOCKED / UNVERIFIED.
- Exact commands, outputs/log locations and exit statuses.
- Session transcript linking initialization, discovery and representative calls.
- Capability parity table and negative-test table: case | expected behavior and
  source | observed response/state | pass/fail/blocked.
- Findings with evidence, impact and narrowest fix; missing coverage and cleanup.

A startup, valid-session, parseability or unsafe-input failure is FAIL. Bounded
non-dangerous metadata/docs drift can be PASS WITH CAVEATS. Missing runtime
access is BLOCKED or UNVERIFIED, never PASS; do not call this a security audit.
```

## How It Works

A single initialized session exposes lifecycle bugs that disconnected requests miss. Four-way capability comparison catches release drift, while revision-aware negative tests avoid treating legitimate negotiation or documented diagnostics as failures.

## Variables

- `[checkout and candidate revision]`: exact source tree to build and test.
- `[transport, command or endpoint]`: candidate-supported transport and launch path.
- `[fixtures, permitted operations, redacted environment]`: disposable data and safe-operation boundaries.
- `[time limit, installation/network permissions]`: explicit cost and side-effect limits.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
