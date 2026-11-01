---
category: "code"
title: "Contract-Driven API Mock Generation"
source: "wshobson/agents"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Contract-Driven API Mock Generation

**Category:** code
**Source:** Adapted from https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/plugins/api-testing-observability/commands/api-mock.md (MIT)

Copyright (c) 2024 Seth Hobson. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--wshobsonagents-mit).

## When to Use

Build deterministic external-service test doubles from an existing API contract, including failure cases and tests proving that requests never escape to the real upstream service.

## The Prompt

```text
Generate verified API mocks from the supplied contract, without redesigning it.
Contract input: [OpenAPI document or versioned consumer contract]
Consumer scope: [client paths, operations and required test behaviors]
Project context: [language, test runner and existing mock tooling]
Deliverables location: [stub, fixture, test and setup documentation paths]
Isolation rules: [local binding, blocked upstream hosts and synthetic credentials]

1. Inspect the contract and scoped consumer before writing stubs. Identify its
   version, referenced schemas, supported media types, authentication shape,
   operations and documented success/error responses. Resolve local references
   and report inaccessible remote ones. Inventory installed mock libraries and
   existing test setup; use an established compatible library rather than inventing
   a server framework. If endpoints, pagination or error semantics are unspecified,
   report the gap and block affected contract claims instead of guessing an API.
2. Create an operation coverage ledger mapping each selected operation to request
   matchers, fixture, scenario and assertion. Match HTTP method, concrete path
   parameters, query encoding, relevant headers and body predicates explicitly.
   Set deterministic precedence so a broad fallback cannot shadow a specific stub.
   Define unexpected-request behavior as a test failure, not passthrough. Add a
   negative request that differs in one important field to prove the matcher is
   selective. Avoid matching volatile headers or secrets unless behavior needs it.
3. Generate small synthetic fixtures with a fixed seed and clock where useful.
   Preserve identifier relationships, enum values, nullability, required fields,
   numeric boundaries and documented formats. Cover empty and multi-page responses
   when the consumer uses pagination; keep continuation tokens deterministic.
   Validate normal fixture bodies and headers against the appropriate response
   schemas before wiring them into tests. Do not copy customer payloads, production
   credentials or captured authorization headers into mock definitions or logs.
4. Implement a failure matrix using named scenarios selected by test setup, not
   random probability. For each row record trigger, response or transport fault,
   expected attempts, terminal result and assertions. Include documented success,
   a contract-defined client/server error, rate limiting with Retry-After when
   supported, and a timeout longer than the client's configured deadline. Add
   malformed JSON or schema-invalid payloads as deliberate protocol violations,
   clearly separate from valid contract responses. Do not label these fixtures
   contract-compliant simply because the consumer handles them safely.
5. For retry behavior, use finite-use stubs or explicit state transitions: for
   example, one authorized transient failure followed by success. Assert exact
   attempt counts and bounded backoff using the runner's controllable clock when
   available. Ensure timeout tests distinguish a delayed response from a connection
   failure. Verify non-idempotent requests are not blindly retried; exercise the
   client's idempotency-key policy where the contract defines one. Exhausted
   scenarios must fail visibly rather than quietly reuse a success fixture.
6. Keep scenarios isolated per test or worker. Reset request journals, counters,
   clocks and state before each test; restore client configuration and close
   handlers, sockets and background tasks in teardown even after failures. Bind
   any server to a loopback address with collision-safe ports. Block real upstream
   network access independently of the mock matcher, and include an intentional
   unmatched request to prove no real service fallback can occur.
7. Run the actual consumer against the mocks, then run request/response contract
   checks with tooling compatible with the contract dialect. Assert observed
   request content and count, parsed results, pagination completion, timeout/error
   mapping and absence of leaked requests. A mock server starting is not a test.
   Record exact commands, exit status and covered operations. If dependencies or
   the runner are unavailable, report verification blocked; never fabricate passes.

Deliver runnable stubs, deterministic fixtures, the scenario matrix, consumer and
contract tests, and concise setup/reset/teardown instructions. Finish with verified
coverage, deliberate contract violations, unimplemented operations and isolation
evidence. Keep scope to test doubles, not new endpoints, dashboards or deployment.
```

## How It Works

The sequence is contract input → verified stubs → deterministic failure scenarios → contract and consumer checks. Unlike API Design From Requirements, it preserves an existing API rather than creating its public contract. Library-native handlers replace the upstream's incomplete custom framework examples.

## Variables

- `[OpenAPI document or versioned consumer contract]`: authoritative contract and revision.
- `[client paths, operations and required test behaviors]`: bounded consumer coverage.
- `[language, test runner and existing mock tooling]`: implementation compatibility.
- `[stub, fixture, test and setup documentation paths]`: concrete output destinations.
- `[local binding, blocked upstream hosts and synthetic credentials]`: isolation controls.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
