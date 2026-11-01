---
category: "code"
title: "Salesforce LWC Delivery with Aura Integration Gates"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Salesforce LWC Delivery with Aura Integration Gates

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/salesforce-aura-lwc.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Implement one Salesforce Lightning Web Component, with an Aura wrapper only when its identified hosting context requires one, and verify data access, accessibility, and integration behavior separately.

## The Prompt

```text
Deliver one accessible Salesforce UI feature in the existing repository.
Feature contract: [user interactions, records, acceptance cases and boundaries]
Target context: [org release, API version, host surface and supported devices]
Existing implementation: [component, Apex, message channel and style locations]
Verification scope: [local checks and explicitly authorized target-org actions]
Output location: [component bundle, tests and delivery note paths]

1. Discover existing components, related Apex methods, metadata targets, message
   channels, project configuration and tests before building. Identify the actual
   host: App Builder, record page, Flow screen, Experience Cloud or another supported
   surface. Confirm required permissions, record shapes and mobile/offline needs.
   Prefer composition and LWC for new work; retain Aura only for a documented
   integration requirement, not an assumed list of Aura-only contexts.
2. Resolve uncertainty through repository evidence and current official Salesforce
   documentation for the target org. Batch questions when behavior, authorization,
   data writes or hosting support remains materially ambiguous. Pause the affected
   implementation until answered; do not guess record access or business behavior.
   Continue independent safe work, and record low-risk presentational choices that
   follow existing conventions. This is a general coding-agent policy, not a
   requirement for a particular editor, agent harness or proprietary tool name.
3. Choose data access deliberately. Prefer base record forms or Lightning Data
   Service for supported standard record operations. Use reactive wire access for
   reads when appropriate, cacheable Apex only for compatible read-only logic,
   and imperative calls for user-initiated writes or non-cacheable operations.
   Consider GraphQL only after checking schema, adapter module, org/API availability
   and mobile/offline limitations. For example, lightning/graphql and
   lightning/uiGraphQLApi have different capabilities; do not treat gql as the
   wire adapter or assume every GraphQL feature is supported by both modules.
4. Verify server-side security independently of presentation. Apex must enforce
   record sharing and object/field access using mechanisms supported by the target
   version and project policy. A with-sharing declaration alone is not CRUD/FLS
   enforcement. Validate user input, minimize returned fields and handle authorization
   failures without leaking records or internal details. Never render untrusted raw
   HTML or expose secrets through debug logs. Hiding a button is not access control.
5. Implement the complete LWC bundle: template, JavaScript, metadata, scoped CSS
   when needed, and Jest tests. Add or adjust Apex and its tests only within scope.
   Model loading, empty, success, validation and error states explicitly. Avoid
   lifecycle-triggered writes, repeated subscriptions and render loops. Specify
   refresh/cache invalidation after writes. Use public properties or methods for
   parent-to-child communication and narrow events for the reverse direction;
   choose Lightning Message Service for supported unrelated-component integration.
6. Verify event payloads, propagation and target contracts against the actual host.
   Flow screen communication uses the documented Flow APIs; do not mechanically
   add bubbles or composed to every event. Keep propagation no broader than needed
   and test the real listener boundary. If an Aura wrapper is required, document
   its responsibility and verify the LWC/Aura handoff rather than mixing data
   access layers unnecessarily. Clean up subscriptions when the component detaches.
7. Use supported base components and styling hooks for the org's design system.
   Treat SLDS 2 as a target-context possibility, not a universal default. Verify
   supported tokens, hooks, themes and base-component constraints against the
   actual version; do not copy a universal token-prefix recipe. Test dark mode
   only where supported and report unsupported themes. Provide labels, meaningful
   accessible names, error announcements, focus behavior and keyboard operation;
   redundant ARIA attributes are not a substitute for semantic controls.
8. Run lint/build checks and Jest tests covering loading, data success/error/empty,
   user actions, keyboard handling and event payloads. Add server-side security
   tests where Apex changes. Report exact commands and failures. Local mocked Jest
   results do not establish target-org rendering, permissions or deployment success.
   Deploy or exercise org writes only with explicit authorization, then read back
   the exact deployment target and verify the feature in its intended host.

Return files delivered, chosen framework/data pattern, version-specific evidence,
accessibility/security checks, local test results and target-org evidence separately.
Mark blocked acceptance cases incomplete instead of claiming the feature is done.
```

## How It Works

Discovery narrows the feature to one host and org context before data access or styling choices become code. Security, local test behavior, and org integration each need their own evidence; one cannot stand in for another. Adapter reference: https://developer.salesforce.com/docs/platform/lwc/guide/reference-graphql.html.

## Variables

- `[user interactions, records, acceptance cases and boundaries]`: feature behavior and limits.
- `[org release, API version, host surface and supported devices]`: platform compatibility.
- `[component, Apex, message channel and style locations]`: reusable repository context.
- `[local checks and explicitly authorized target-org actions]`: verification permissions.
- `[component bundle, tests and delivery note paths]`: file deliverables.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
