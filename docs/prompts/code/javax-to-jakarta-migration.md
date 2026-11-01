---
category: "code"
title: "Javax-to-Jakarta Migration with Runtime and JDK Guards"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Javax-to-Jakarta Migration with Runtime and JDK Guards

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/javax-to-jakarta-migration/SKILL.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

For an explicitly authorized Java EE namespace/runtime migration. Finding `javax.*` imports alone does not authorize migration: without a request to migrate, report the inventory instead.

## The Prompt

```text
Migrate only the authorized Java EE surface to the specified Jakarta runtime.
Checkout and scope: [repository, modules and permitted files]
Authorization: [explicit migration request]
Target: [JDK, framework/BOM, server and target versions]
Verification: [baseline, build, test and runtime smoke commands]

1. Confirm explicit migration authorization and a concrete target. Imports alone
   do not authorize migration. Inventory working-tree changes and preserve them;
   use a reversible patch/step, with no automatic commit or deployment.
2. Read official documentation for the exact target runtime/framework and JDK.
   Start with https://jakarta.ee/specifications/ and the applicable server guide
   (for example https://tomcat.apache.org/migration-10.html), framework upgrade
   guide (https://docs.spring.io/spring-boot/upgrading.html), or persistence-provider
   migration guide (https://hibernate.org/orm/documentation/migrate/).
   Follow version-specific pages and cite them. Establish supported API levels,
   dependency coordinates, descriptor schemas and runtime compatibility. Do not
   copy example version pins or assume a servlet container supplies all EE APIs.
   If essential compatibility information is unavailable, stop before edits.
3. Run the repository-native baseline, such as ./mvnw verify or ./gradlew build,
   only with authorized execution permissions. Record commands, output and exit
   status. Stop on a red or blocked baseline; do not hide pre-existing failures.
4. Inventory Java EE imports and fully qualified references: servlet, persistence,
   validation, annotation, inject, enterprise, faces, ws.rs, el, json, mail and
   websocket. Verify each actual package against the target API, including package
   exceptions; never perform a global javax-to-jakarta replacement.
   Preserve JDK namespaces, including:
   javax.sql.*, javax.naming.*, javax.crypto.*, javax.net.*,
   javax.security.auth.*, javax.swing.*, javax.xml.parsers.*.
   This exclusion list is not exhaustive: check the target JDK module/API docs for
   other javax packages and mixed namespaces such as javax.annotation.processing.
5. Update only verified EE references and compatible dependency coordinates.
   Respect the framework BOM's managed versions; avoid competing explicit pins.
   Check dependency trees for old/new API mixtures and third-party compatibility;
   use runtime-provided versus packaged scopes correctly. Do not assume changing
   imports makes incompatible libraries or bytecode compatible.
6. Align web.xml, persistence.xml, beans.xml and other descriptors with the target
   specification. Inspect service-provider files, reflection strings, configuration
   keys, generated-code inputs and tests. Preserve JDK references and unrelated
   behavior. Explain any binary transformation or manual library upgrade needed;
   do not apply unreviewed transformation tools automatically.
7. Run target-compatible compilation, focused/full tests and an authorized
   disposable target-runtime startup/request smoke test. Re-scan remaining javax
   references and classify each as JDK, intentionally retained or unresolved EE.
   A green compile alone is not runtime verification. Stop and report failures
   rather than weakening assertions or deploying to obtain a pass.

Return baseline evidence; target compatibility matrix with official sources;
files/dependencies/descriptors changed; test commands, statuses and runtime
observations; remaining references, manual work and rollback instructions.
If runtime tests cannot run, label that part unverified; do not claim completion.
```

## How It Works

Authorization and a green baseline precede narrow, runtime-matched changes. JDK exclusions and dependency/descriptor checks prevent the common failure of treating every `javax` package as a Jakarta API.

## Variables

- `[repository, modules and permitted files]`: authorized edit boundary.
- `[explicit migration request]`: permission for this migration, not inferred from imports.
- `[JDK, framework/BOM, server and target versions]`: compatibility targets to verify in official documentation.
- `[baseline, build, test and runtime smoke commands]`: project-native evidence gates.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
