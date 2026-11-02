---
category: "code"
title: "Secure Multi-Stage Dockerfile Builder"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Secure Multi-Stage Dockerfile Builder

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/multi-stage-dockerfile/SKILL.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Create a build/runtime split for a real application, including its build context, secret handling and reproducible inputs. Requires application manifests and startup requirements; language labels alone are insufficient for a verified image.

## The Prompt

```text
Produce a multi-stage Dockerfile and .dockerignore for this application.
Application: [checkout, language, manifests and lockfiles]
Target: [runtime version, OS/architecture and deployment constraints]
Contract: [build command, artifact paths, startup, port and smoke behavior]
Permissions: [proposal-only or authorized edits/builds, network and secret sources]

1. Inspect actual manifests, lockfiles, build scripts, runtime assets and native
   dependencies. Confirm target image/runtime compatibility using official image
   and runtime docs. Any image versions in examples, including upstream examples,
   are EXAMPLES, never blind pins or recommendations for this project. If critical
   inputs are missing, name them rather than invent successful build artifacts.
2. Separate named dependency/build/test stages from a minimal runtime stage. Copy
   only required artifacts, production dependencies and assets into runtime; keep
   compilers, test fixtures and package-manager caches out unless truly required.
   Check native-library/ABI compatibility across stages; Alpine/musl is not a
   drop-in replacement for glibc. Distroless is optional, not a universal default.
3. Use approved image versions pinned by verified digest and respect the target
   platform. Use committed lockfiles and frozen/locked dependency installs;
   explain system package/source pinning and remaining nondeterministic inputs.
   Tags alone are mutable and do not ensure reproducibility. Provide an intentional
   digest/lockfile refresh policy; never invent a digest or promise bit-identical
   output without measuring it.
4. Order layers for caching: copy manifests/lockfiles before source, then compile
   and copy runtime artifacts. Use BuildKit cache mounts where supported without
   making cache contents part of the application contract. Include .dockerignore
   excluding VCS files, local build output, caches, credentials and irrelevant
   data while preserving required source and lockfiles. Explain exceptions.
5. Create/use a non-root runtime UID/GID, set owned writable paths and restrictive
   permissions, set WORKDIR and use an exec-form entrypoint/command with correct
   signal handling. Avoid privileged ports/capabilities where feasible. Explain
   any unavoidable elevated requirement instead of silently running as root.
6. Never pass credentials via ARG/ENV or COPY them into any stage. Use BuildKit
   RUN --mount=type=secret for authorized private dependency access and show the
   matching docker build --secret id=...,src=... command with placeholder paths.
   Do not print secret values or write them into artifacts/logs. Multi-stage
   builds alone do not prevent secret leaks into layers or caches.
7. Return complete Dockerfile and .dockerignore contents plus project-specific,
   shell-quoted build, test-stage and smoke commands. Include platform, image tag,
   required runtime configuration and safe secret placeholders. Smoke commands
   must verify the actual expected process/response and non-root identity, then
   remove only this run's container. Validate health checks against tools actually
   present in the final image; do not assume curl or a shell exists.
8. Execute builds/tests only when authorized. Record commands, output, exit status,
   image identity, smoke assertions and a final-image vulnerability scan if an
   approved scanner is available. Preserve failures; do not fake build/smoke/scan
   output. If execution is unavailable, mark commands proposed and image unverified.
   Do not push an image or deploy it without separate authorization.

Return the artifacts, stage rationale, compatibility and pinned-input evidence,
build/smoke results or blockers, secret/cache caveats and cleanup instructions.
```

## How It Works

The build/runtime split is paired with an explicit context filter and a runnable verification contract. Digest and lockfile controls address reproducibility separately from secret mounts, non-root execution and runtime compatibility.

## Variables

- `[checkout, language, manifests and lockfiles]`: actual build inputs.
- `[runtime version, OS/architecture and deployment constraints]`: supported target environment.
- `[build command, artifact paths, startup, port and smoke behavior]`: executable application contract.
- `[proposal-only or authorized edits/builds, network and secret sources]`: side-effect and credential boundaries.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: empty after thinking |
