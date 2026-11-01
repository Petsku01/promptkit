---
category: "code"
title: "API Design From Requirements"
source: "promptkit-authored"
---
# API Design From Requirements

**Category:** code
**Source:** Original promptkit-authored workflow.

## When to Use

Turn requirements into a reviewable, documentation-ready API contract before implementation. Unlike a general architecture persona or requirements checklist, this workflow produces concrete operation schemas, request/response examples, failure semantics, compatibility policy, and contract-test cases while preserving unresolved business decisions.

## The Prompt

```text
Act as an API designer responsible for a contract that consumers can implement
against without guessing. Design [surface] for [consumers] using
[style REST/GraphQL/RPC]. Work contract-first. Do not implement server handlers or
choose hidden business rules merely to make the document look complete.

1. Discover the actual requirements. Read supplied use cases, repository guidance,
   existing contracts, consumer integrations, and supported schema tooling. Identify
   actors, business operations, data ownership, trust boundaries, deployment
   constraints, and compatibility obligations. Assign a requirement identifier to
   each observable outcome. Build an unknowns register with question, affected
   operations, consequence, and decision owner if known. Distinguish facts from
   proposals. Missing authorization policy, consistency semantics, or destructive
   operation requirements can block finalization; label the contract PROVISIONAL
   instead of papering over these gaps with plausible defaults.

2. Model resources and operations from consumer tasks rather than database tables.
   Describe identifiers, ownership, lifecycle states, allowed transitions, and
   relationships. Separate public representations from persistence internals and
   sensitive fields. For REST, choose resource paths and method semantics; for
   GraphQL, define types, queries, mutations, and nullability; for RPC, define
   service methods and typed messages. Explain the selected style's consequences
   without mixing incompatible transport conventions. Do not expose an internal
   field merely because the current ORM makes it convenient.

3. Define each operation precisely. Include name, purpose, linked requirements,
   input fields, types, requiredness, null versus absent behavior, defaults,
   validation bounds, output schema, and observable side effects. Specify temporal
   formats, timezone handling, monetary units, identifier opacity, and collection
   ordering where relevant. Address synchronous versus asynchronous completion,
   job status, cancellation, partial success, and atomicity when the use case needs
   them. Declare unsupported behavior explicitly instead of leaving consumers to
   infer it. Avoid adding speculative endpoints with no consumer requirement.

4. Specify authentication and authorization separately. Identify credential
   mechanism and operation scopes, then object-level, tenant-level, and field-level
   checks required after identity is established. State how resource existence is
   concealed or disclosed to unauthorized callers. Define server-owned fields and
   rejected mass-assignment attempts. Bound payload sizes, query complexity, page
   sizes, and expensive operations. Describe rate-limit signaling and retry
   guidance without inventing production quotas. Never include real credentials,
   customer identifiers, or private data in examples.

5. Establish a consistent error taxonomy. Distinguish malformed input, failed
   authentication, denied authorization, missing resources, business validation,
   conflicting state, concurrency conflict, throttling, and temporary dependency
   failure. Specify stable machine-readable codes, safe human messages, correlation
   identifiers, and field errors where appropriate. Map these to the chosen style:
   HTTP statuses for REST, documented error extensions and partial-data behavior
   for GraphQL, or transport status plus typed details for RPC. State retryability
   explicitly. Do not leak stack traces, secrets, or internal topology.

6. Define retry and concurrency semantics per operation. Identify which operations
   are naturally idempotent and which require an idempotency key or cannot safely
   be retried. For keys, describe ownership scope, request fingerprint, retention
   decision, duplicate-in-flight behavior, conflicting payloads, and replayed
   result. Mark unresolved retention periods as open decisions. Specify optimistic
   concurrency tokens or another conflict policy where updates can overwrite
   each other. Do not promise exactly-once effects without a supporting system
   design. Include timeout ambiguity: a timed-out write may still have succeeded.

7. Design collection access deliberately. Specify supported filters, stable sort
   order with tie-breakers, bounded page sizes, and pagination continuation format.
   Choose cursor or offset pagination based on required consistency and access
   patterns; explain changes between pages and expired or invalid continuation
   tokens. Apply authorization before exposing counts or page contents. Define
   empty results and completion signals. Do not invent a global total count if
   it is unavailable or too costly to guarantee under the requirements.

8. Provide a complete example request and success response for every endpoint or
   operation, plus a representative failure example and applicable retry example.
   Label illustrative values clearly; do not imply examples are live responses.
   Include headers or metadata, media types, status semantics, and all referenced
   schemas. Check examples against schema, nullability, validation, and error
   definitions. Use OpenAPI, GraphQL SDL, or the existing RPC IDL when tooling is
   available; run its native validator and report actual output. Otherwise state
   that syntax or example conformance remains unverified.

9. Define evolution before approval. List breaking changes, including stricter
   validation, changed defaults, new required inputs, removed fields, changed enum
   assumptions, and altered error or ordering behavior. Propose version selection,
   deprecation notice, consumer migration, compatibility testing, and retirement
   approval. Do not assign deadlines without an owner decision. Produce contract
   tests for happy paths, validation, unauthorized cross-tenant access, retries,
   pagination boundaries, and concurrent updates. Link every requirement to an
   operation, example, or explicit out-of-scope decision.

Return documentation-ready sections: scope and consumers; requirements map;
unknowns and blockers; resource model; operation catalog and schemas; examples;
errors; authorization; idempotency/concurrency; pagination; versioning; contract
tests; validation results. Conclude READY FOR CONTRACT REVIEW, PROVISIONAL, or
BLOCKED. This is a design deliverable, not a claim that an API was deployed or tested.
```

## How It Works

The contract is built from consumer requirements and checked for cross-section consistency. REST method semantics, error responses, pagination, and versioning are informed by Microsoft's [Best practices for RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design). GraphQL/RPC mapping and explicit unknowns are original applications of established contract-design practice, not claims that the REST guidance mandates those styles. Tool-based discovery and honest validation follow the [OpenAI GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide).

## Variables

- `[surface]`: requirements and API boundary, including existing contracts and non-goals.
- `[consumers]`: client types, trust levels, compatibility needs, and principal use cases.
- `[style REST/GraphQL/RPC]`: selected API style and repository-native schema tooling.

## Tested On

Not model-tested. Curated original workflow; no live model-quality evaluation is claimed.
