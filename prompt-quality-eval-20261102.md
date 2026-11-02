# Promptkit whole-repo quality map — 2026-11-02

Mechanical synthesis of eight chunk-eval judge artifacts (Sol A–D, Grok E–H).
Rubric: d1 structural clarity · d2 operational concreteness · d3 substance-vs-fluff · d4 rules/stop-conditions · overall 1–5.
fab = unevidenced claims / metrics / fake tests. Category derived from path under `src/llm_promptkit/prompts/`.

## Verification

| check | value |
|---|---|
| rows parsed | 374 |
| unique files | 374 |
| duplicates | 0 |
| missing vs repo `*.md` (README excluded) | 0 |
| extra vs repo | 0 |
| chunk sizes | A 47, B 47, C 47, D 47, E 47, F 47, G 47, H 45 |
| judges | Sol (A–D, 188 rows), Grok (E–H, 186 rows) |

Source artifacts:

- `promptkit-repo-eval-sol-A-20261102.md` … `sol-D`
- `promptkit-repo-eval-grok-E-20261102.md` … `grok-H`

## 1. Full 374-row quality map

| file | category | overall | fab | judge |
|---|---|---:|:---:|---|
| code/api-design-from-requirements.md | code | 5 | no | sol |
| code/api-mock-generation.md | code | 5 | no | sol |
| code/browser-exploration-to-verified-playwright-tests.md | code | 5 | no | sol |
| code/brutal-reviewer.md | code | 2 | yes | sol |
| code/clojure-repl-pair-programming.md | code | 5 | no | sol |
| code/code-review-reception-pushback.md | code | 5 | no | sol |
| code/code-reviewer-extended.md | code | 3 | yes | sol |
| code/code-reviewer.md | code | 2 | yes | sol |
| code/commit-message-generator.md | code | 2 | yes | sol |
| code/create-git-diff-commit.md | code | 3 | yes | sol |
| code/data-pipeline-architecture.md | code | 5 | no | sol |
| code/dax-terminal.md | code | 2 | yes | sol |
| code/debugger-interactive.md | code | 2 | yes | sol |
| code/dependency-framework-upgrade-workflow.md | code | 5 | no | sol |
| code/developer-relations-consultant.md | code | 2 | yes | sol |
| code/devops-engineer.md | code | 2 | yes | sol |
| code/embedded-c-misra-deviations.md | code | 5 | no | sol |
| code/ethereum-developer.md | code | 1 | yes | sol |
| code/executable-implementation-plans.md | code | 5 | no | sol |
| code/explain-code.md | code | 3 | yes | sol |
| code/fixer-loop.md | code | 5 | no | sol |
| code/fullstack-software-developer.md | code | 1 | yes | sol |
| code/generate-code-rules.md | code | 2 | yes | sol |
| code/gha-node-runtime-upgrade.md | code | 5 | no | sol |
| code/git-worktree-isolation-baseline.md | code | 5 | no | sol |
| code/github-expert.md | code | 1 | yes | sol |
| code/it-architect.md | code | 2 | yes | sol |
| code/javascript-console.md | code | 2 | yes | sol |
| code/javax-to-jakarta-migration.md | code | 5 | no | sol |
| code/launchdarkly-flag-removal.md | code | 5 | no | sol |
| code/linux-terminal.md | code | 2 | yes | sol |
| code/logical-git-revert-confirmation.md | code | 5 | no | sol |
| code/machine-learning-engineer.md | code | 2 | yes | sol |
| code/mongodb-query-performance-advisor.md | code | 5 | no | sol |
| code/multi-stage-dockerfile-builder.md | code | 5 | no | sol |
| code/notebook-sample-builder.md | code | 5 | no | sol |
| code/password-generator.md | code | 2 | yes | sol |
| code/php-interpreter.md | code | 2 | yes | sol |
| code/pyspark-performance-reviewer.md | code | 5 | no | sol |
| code/python-interpreter.md | code | 2 | yes | sol |
| code/r-interpreter.md | code | 2 | yes | sol |
| code/read-only-test-gap-audit.md | code | 5 | no | sol |
| code/refactoring-safety-net.md | code | 5 | no | sol |
| code/review-code.md | code | 3 | yes | sol |
| code/salesforce-ui-dev-aura-lwc.md | code | 5 | no | sol |
| code/senior-engineer.md | code | 4 | yes | sol |
| code/senior-frontend-developer.md | code | 1 | yes | sol |
| code/software-quality-assurance-tester.md | code | 2 | yes | sol |
| code/sql-change-blast-radius-analysis.md | code | 5 | no | sol |
| code/sql-terminal.md | code | 3 | yes | sol |
| code/svg-designer.md | code | 3 | yes | sol |
| code/tdd-full-cycle.md | code | 5 | no | sol |
| code/tdd-generator.md | code | 3 | yes | sol |
| code/terraform-iac-reviewer.md | code | 5 | no | sol |
| code/unit-tester.md | code | 2 | yes | sol |
| code/ux-ui-developer.md | code | 2 | yes | sol |
| code/web-browser.md | code | 3 | yes | sol |
| code/windows-arm64-python-wheel-ci.md | code | 5 | no | sol |
| context/codebase-memory-mcp-discovery.md | context | 4 | no | sol |
| context/few-shot-negatives.md | context | 3 | yes | sol |
| context/session-handoff.md | context | 3 | no | sol |
| creative/advertiser.md | creative | 2 | yes | sol |
| creative/artist-advisor.md | creative | 2 | yes | sol |
| creative/ascii-artist.md | creative | 3 | yes | sol |
| creative/create-art-prompt.md | creative | 3 | yes | sol |
| creative/essay-writer.md | creative | 2 | yes | sol |
| creative/novelist.md | creative | 2 | yes | sol |
| creative/scamper.md | creative | 3 | yes | sol |
| creative/screenwriter.md | creative | 2 | yes | sol |
| creative/stand-up-comedian.md | creative | 2 | yes | sol |
| creative/storyteller.md | creative | 2 | yes | sol |
| creative/tech-writer.md | creative | 3 | yes | sol |
| debug/backend-performance-profiling.md | debug | 5 | no | sol |
| debug/bug-risk-analysis.md | debug | 1 | yes | sol |
| debug/comprehensive-repository-analysis-and-bug-fixing-f.md | debug | 2 | yes | sol |
| debug/debugger-extended.md | debug | 3 | yes | sol |
| debug/four-phase-root-cause-debugging.md | debug | 5 | no | sol |
| debug/frontend-performance-investigation.md | debug | 5 | no | sol |
| debug/mcp-server-release-qa.md | debug | 5 | no | sol |
| debug/production-incident-command.md | debug | 5 | no | sol |
| debug/rubber-duck.md | debug | 3 | yes | sol |
| debug/security-fixes-cves.md | debug | 1 | yes | sol |
| debug/security-fixes.md | debug | 1 | yes | sol |
| debug/sentry-bug-fixer.md | debug | 2 | yes | sol |
| debug/stack-trace-analyzer.md | debug | 3 | yes | sol |
| debug/stackoverflow-post.md | debug | 2 | yes | sol |
| debug/tech-troubleshooter.md | debug | 2 | yes | sol |
| debug/test-first-bug-fixing-approach.md | debug | 3 | yes | sol |
| debug/want-to-analyze-security-issues-and-vulnerabilitie.md | debug | 1 | yes | sol |
| defensive/accessibility-auditor.md | defensive | 2 | yes | sol |
| defensive/act-as-a-resume-reviewer.md | defensive | 3 | yes | sol |
| defensive/analyze-malware.md | defensive | 4 | yes | sol |
| defensive/analyze-threat-report.md | defensive | 3 | yes | sol |
| defensive/comprehensive-content-review-plan.md | defensive | 2 | yes | sol |
| defensive/comprehensive-web-application-development-with-sec.md | defensive | 2 | yes | sol |
| defensive/contrarian.md | defensive | 4 | yes | sol |
| defensive/create-stride-threat-model.md | defensive | 4 | yes | sol |
| defensive/email-authentication-header-analyzer.md | defensive | 5 | no | sol |
| defensive/evidence-gated-completion-claims.md | defensive | 5 | no | sol |
| defensive/greybeard-secure-prompt-engineer.md | defensive | 3 | yes | sol |
| defensive/hallucination-reducer.md | defensive | 4 | yes | sol |
| defensive/journal-reviewer.md | defensive | 2 | yes | sol |
| defensive/llm-security-specialist.md | defensive | 2 | yes | sol |
| defensive/plagiarism-checker.md | defensive | 1 | yes | sol |
| defensive/pull-request-review-assistant.md | defensive | 2 | yes | sol |
| defensive/refactoring-expert.md | defensive | 3 | yes | sol |
| defensive/security-code-audit.md | defensive | 5 | no | sol |
| defensive/spec-plan-task-consistency-audit.md | defensive | 5 | no | sol |
| defensive/task-reviewer-compliance-quality.md | defensive | 5 | no | sol |
| defensive/tech-reviewer.md | defensive | 1 | yes | sol |
| defensive/update-checker.md | defensive | 1 | yes | sol |
| defensive/website-security-vulnerability-checker.md | defensive | 2 | yes | sol |
| defensive/write-hackerone-report.md | defensive | 2 | yes | sol |
| education/ai-writing-tutor.md | education | 1 | yes | sol |
| education/debate-coach.md | education | 1 | yes | sol |
| education/instructor-in-a-school.md | education | 2 | yes | sol |
| education/life-coach.md | education | 1 | yes | sol |
| education/math-teacher.md | education | 1 | yes | sol |
| education/mathematical-history-teacher.md | education | 3 | yes | sol |
| education/motivational-coach.md | education | 1 | yes | sol |
| education/philosophy-teacher.md | education | 1 | yes | sol |
| education/public-speaking-coach.md | education | 1 | yes | sol |
| education/spoken-english-teacher-and-improver.md | education | 3 | yes | sol |
| education/teacher-of-react-js.md | education | 2 | yes | sol |
| model-optimized/advanced-techniques/chain-of-thought.md | model-optimized | 4 | yes | sol |
| model-optimized/advanced-techniques/meta-prompting.md | model-optimized | 3 | no | sol |
| model-optimized/advanced-techniques/prompt-chaining.md | model-optimized | 3 | no | sol |
| model-optimized/advanced-techniques/react.md | model-optimized | 3 | no | sol |
| model-optimized/advanced-techniques/self-consistency.md | model-optimized | 3 | no | sol |
| model-optimized/advanced-techniques/tree-of-thoughts.md | model-optimized | 3 | no | sol |
| model-optimized/agentic/orchestration.md | model-optimized | 3 | no | sol |
| model-optimized/agentic/planning.md | model-optimized | 3 | no | sol |
| model-optimized/agentic/reflection.md | model-optimized | 3 | no | sol |
| model-optimized/agentic/tool-use.md | model-optimized | 4 | no | sol |
| model-optimized/anthropic/claude-3-haiku/analysis.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3-haiku/coding.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3-opus/analysis.md | model-optimized | 4 | no | sol |
| model-optimized/anthropic/claude-3-opus/reasoning.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3-sonnet/analysis.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3-sonnet/coding.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3-sonnet/json-output.md | model-optimized | 4 | no | sol |
| model-optimized/anthropic/claude-3-sonnet/writing.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3.5-haiku/coding.md | model-optimized | 4 | no | sol |
| model-optimized/anthropic/claude-3.5-haiku/simple-tasks.md | model-optimized | 4 | no | sol |
| model-optimized/anthropic/claude-3.7-sonnet/coding.md | model-optimized | 3 | no | sol |
| model-optimized/anthropic/claude-3.7-sonnet/reasoning.md | model-optimized | 2 | no | sol |
| model-optimized/anthropic/claude-opus-4.5/coding.md | model-optimized | 3 | yes | sol |
| model-optimized/anthropic/claude-opus-4.5/reasoning.md | model-optimized | 3 | yes | sol |
| model-optimized/anthropic/claude-opus-4.7/analysis.md | model-optimized | 2 | yes | sol |
| model-optimized/anthropic/claude-opus-4.7/coding.md | model-optimized | 2 | yes | sol |
| model-optimized/anthropic/claude-opus-4.7/long-horizon.md | model-optimized | 3 | yes | sol |
| model-optimized/anthropic/claude-opus-4.7/reasoning.md | model-optimized | 3 | yes | sol |
| model-optimized/anthropic/claude-opus-4.8/analysis.md | model-optimized | 5 | no | sol |
| model-optimized/anthropic/claude-opus-4.8/coding.md | model-optimized | 5 | no | sol |
| model-optimized/anthropic/claude-opus-4.8/reasoning.md | model-optimized | 5 | no | sol |
| model-optimized/anthropic/claude-opus-4/analysis.md | model-optimized | 3 | yes | sol |
| model-optimized/anthropic/claude-sonnet-4/coding.md | model-optimized | 2 | yes | sol |
| model-optimized/anthropic/claude-sonnet-4/reasoning.md | model-optimized | 2 | yes | sol |
| model-optimized/benchmarks/coding.md | model-optimized | 1 | yes | sol |
| model-optimized/benchmarks/instruction-following.md | model-optimized | 2 | yes | sol |
| model-optimized/benchmarks/reasoning.md | model-optimized | 1 | yes | sol |
| model-optimized/benchmarks/safety.md | model-optimized | 2 | yes | sol |
| model-optimized/cohere/command-r-plus/analysis.md | model-optimized | 2 | no | sol |
| model-optimized/cohere/command-r-plus/grounding.md | model-optimized | 3 | no | sol |
| model-optimized/cohere/command-r-plus/rag.md | model-optimized | 3 | no | sol |
| model-optimized/cohere/command-r/analysis.md | model-optimized | 2 | no | sol |
| model-optimized/cohere/command-r/grounding.md | model-optimized | 3 | no | sol |
| model-optimized/cohere/command-r/rag.md | model-optimized | 3 | no | sol |
| model-optimized/deepseek/deepseek-coder/debugging.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-coder/generation.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-coder/refactoring.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-coder/review.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-r1/coding.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-r1/reasoning.md | model-optimized | 2 | yes | sol |
| model-optimized/deepseek/deepseek-v3.1/analysis.md | model-optimized | 3 | yes | sol |
| model-optimized/deepseek/deepseek-v3.1/coding.md | model-optimized | 3 | yes | sol |
| model-optimized/deepseek/deepseek-v3/analysis.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-v3/coding.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-v3/json-output.md | model-optimized | 3 | no | sol |
| model-optimized/deepseek/deepseek-v3/math.md | model-optimized | 2 | no | sol |
| model-optimized/deepseek/deepseek-v4-flash/analysis.md | model-optimized | 3 | yes | sol |
| model-optimized/deepseek/deepseek-v4-flash/coding.md | model-optimized | 2 | yes | sol |
| model-optimized/deepseek/deepseek-v4-pro/coding.md | model-optimized | 2 | yes | sol |
| model-optimized/deepseek/deepseek-v4-pro/reasoning.md | model-optimized | 2 | yes | sol |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/analysis.md | model-optimized | 5 | no | sol |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/coding.md | model-optimized | 5 | no | sol |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/reasoning.md | model-optimized | 5 | no | sol |
| model-optimized/evaluation/ab-testing.md | model-optimized | 3 | no | sol |
| model-optimized/evaluation/llm-judge.md | model-optimized | 4 | no | grok |
| model-optimized/evaluation/quality-metrics.md | model-optimized | 3 | no | grok |
| model-optimized/few-shot/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/few-shot/classification.md | model-optimized | 3 | yes | grok |
| model-optimized/few-shot/generation.md | model-optimized | 3 | no | grok |
| model-optimized/few-shot/transformation.md | model-optimized | 3 | no | grok |
| model-optimized/google/gemini-2.5-flash/coding.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-2.5-flash/long-context.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-2.5-flash/quick-tasks.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-2.5-pro/coding.md | model-optimized | 4 | no | grok |
| model-optimized/google/gemini-2.5-pro/multimodal.md | model-optimized | 3 | no | grok |
| model-optimized/google/gemini-2.5-pro/reasoning.md | model-optimized | 4 | no | grok |
| model-optimized/google/gemini-2.5/multimodal.md | model-optimized | 3 | no | grok |
| model-optimized/google/gemini-2.5/reasoning.md | model-optimized | 3 | no | grok |
| model-optimized/google/gemini-2/analysis.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-2/coding.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-2/multimodal.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-3.8-flash/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/google/gemini-3.8-flash/coding.md | model-optimized | 5 | no | grok |
| model-optimized/google/gemini-3.8-flash/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/google/gemini-flash/basic.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-flash/long-context.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-pro/analysis.md | model-optimized | 2 | no | grok |
| model-optimized/google/gemini-pro/coding.md | model-optimized | 2 | no | grok |
| model-optimized/meta/llama-3.1/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/meta/llama-3.1/coding.md | model-optimized | 3 | no | grok |
| model-optimized/meta/llama-3.2/general.md | model-optimized | 1 | no | grok |
| model-optimized/meta/llama-3.2/multimodal.md | model-optimized | 2 | no | grok |
| model-optimized/meta/llama-3.3/analysis.md | model-optimized | 2 | no | grok |
| model-optimized/meta/llama-3.3/coding.md | model-optimized | 2 | no | grok |
| model-optimized/meta/llama-4/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/meta/llama-4/coding.md | model-optimized | 3 | no | grok |
| model-optimized/meta/llama-4/long-context.md | model-optimized | 4 | no | grok |
| model-optimized/mistral/codestral/coding.md | model-optimized | 2 | no | grok |
| model-optimized/mistral/mistral-large/coding.md | model-optimized | 3 | no | grok |
| model-optimized/mistral/mistral-nemo/general.md | model-optimized | 1 | no | grok |
| model-optimized/mistral/mixtral/analysis.md | model-optimized | 1 | no | grok |
| model-optimized/mistral/mixtral/coding.md | model-optimized | 2 | no | grok |
| model-optimized/moonshot/kimi-k2.7-code/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/moonshot/kimi-k2.7-code/coding.md | model-optimized | 5 | no | grok |
| model-optimized/moonshot/kimi-k2.7-code/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/moonshot/kimi-k3/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/moonshot/kimi-k3/coding.md | model-optimized | 5 | no | grok |
| model-optimized/moonshot/kimi-k3/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/openai/codex-5.3/coding.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-3.5-turbo/quick-tasks.md | model-optimized | 2 | no | grok |
| model-optimized/openai/gpt-4-turbo/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4-turbo/coding.md | model-optimized | 2 | no | grok |
| model-optimized/openai/gpt-4.1/analysis.md | model-optimized | 4 | no | grok |
| model-optimized/openai/gpt-4.1/coding.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-4.1/instruction-following.md | model-optimized | 4 | yes | grok |
| model-optimized/openai/gpt-4.1/json-output.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-4.1/writing.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-4/analysis.md | model-optimized | 2 | no | grok |
| model-optimized/openai/gpt-4/coding.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4o/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4o/coding.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4o/json-output.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4o/vision.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-4o/writing.md | model-optimized | 3 | no | grok |
| model-optimized/openai/gpt-5.4/analysis.md | model-optimized | 4 | yes | grok |
| model-optimized/openai/gpt-5.4/coding.md | model-optimized | 4 | yes | grok |
| model-optimized/openai/gpt-5.4/reasoning.md | model-optimized | 4 | yes | grok |
| model-optimized/openai/gpt-5.4/thinking.md | model-optimized | 4 | yes | grok |
| model-optimized/openai/gpt-5.6-sol/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/openai/gpt-5.6-sol/coding.md | model-optimized | 5 | no | grok |
| model-optimized/openai/gpt-5.6-sol/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/openai/gpt-5/coding.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-5/reasoning.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/gpt-6.1-sol/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/openai/gpt-6.1-sol/coding.md | model-optimized | 5 | no | grok |
| model-optimized/openai/gpt-6.1-sol/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/openai/o1/reasoning.md | model-optimized | 2 | yes | grok |
| model-optimized/openai/o3-mini/reasoning.md | model-optimized | 1 | yes | grok |
| model-optimized/openai/o3/coding.md | model-optimized | 3 | yes | grok |
| model-optimized/openai/o3/reasoning.md | model-optimized | 3 | yes | grok |
| model-optimized/qwen/qwen-2.5/analysis.md | model-optimized | 3 | no | grok |
| model-optimized/qwen/qwen-2.5/coding.md | model-optimized | 3 | no | grok |
| model-optimized/qwen/qwen-2.5/json-output.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen-2.5/multilingual.md | model-optimized | 3 | no | grok |
| model-optimized/qwen/qwen-3.5/basic.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen-3.5/coding.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen-3.5/json-output.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen-3/coding.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen-3/multilingual.md | model-optimized | 2 | no | grok |
| model-optimized/qwen/qwen3.8-2.4t-a95b/analysis.md | model-optimized | 4 | no | grok |
| model-optimized/qwen/qwen3.8-2.4t-a95b/coding.md | model-optimized | 5 | no | grok |
| model-optimized/qwen/qwen3.8-2.4t-a95b/reasoning.md | model-optimized | 4 | no | grok |
| model-optimized/qwen/qwen3.8-flash-next/analysis.md | model-optimized | 4 | no | grok |
| model-optimized/qwen/qwen3.8-flash-next/coding.md | model-optimized | 5 | no | grok |
| model-optimized/qwen/qwen3.8-flash-next/reasoning.md | model-optimized | 4 | no | grok |
| model-optimized/roles/business.md | model-optimized | 2 | no | grok |
| model-optimized/roles/creative.md | model-optimized | 2 | no | grok |
| model-optimized/roles/education.md | model-optimized | 3 | no | grok |
| model-optimized/roles/simulators.md | model-optimized | 4 | no | grok |
| model-optimized/roles/technical.md | model-optimized | 4 | no | grok |
| model-optimized/safety/injection-defense.md | model-optimized | 5 | no | grok |
| model-optimized/safety/moderation.md | model-optimized | 3 | no | grok |
| model-optimized/small-models/gemma-2/simple-tasks.md | model-optimized | 2 | no | grok |
| model-optimized/small-models/phi-3.5/basic.md | model-optimized | 2 | no | grok |
| model-optimized/small-models/phi-3.5/coding.md | model-optimized | 3 | no | grok |
| model-optimized/system-prompts/coding.md | model-optimized | 4 | no | grok |
| model-optimized/system-prompts/creative.md | model-optimized | 3 | no | grok |
| model-optimized/system-prompts/education.md | model-optimized | 4 | no | grok |
| model-optimized/system-prompts/expert.md | model-optimized | 4 | no | grok |
| model-optimized/system-prompts/productivity.md | model-optimized | 3 | no | grok |
| model-optimized/use-cases/customer-support.md | model-optimized | 3 | no | grok |
| model-optimized/use-cases/data-processing.md | model-optimized | 3 | no | grok |
| model-optimized/use-cases/hr-recruiting.md | model-optimized | 3 | no | grok |
| model-optimized/use-cases/sales-marketing.md | model-optimized | 3 | no | grok |
| model-optimized/xai/grok-2/analysis.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-2/coding.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-2/creative.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-2/realtime.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-3-mini/coding.md | model-optimized | 3 | no | grok |
| model-optimized/xai/grok-3-mini/reasoning.md | model-optimized | 3 | no | grok |
| model-optimized/xai/grok-3/coding.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-3/reasoning.md | model-optimized | 2 | no | grok |
| model-optimized/xai/grok-4.6/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/xai/grok-4.6/coding.md | model-optimized | 5 | no | grok |
| model-optimized/xai/grok-4.6/reasoning.md | model-optimized | 5 | no | grok |
| model-optimized/zhipu/glm-5.3/analysis.md | model-optimized | 5 | no | grok |
| model-optimized/zhipu/glm-5.3/coding.md | model-optimized | 5 | no | grok |
| model-optimized/zhipu/glm-5.3/reasoning.md | model-optimized | 5 | no | grok |
| output/ai-agent-security-evaluation-checklist.md | output | 3 | no | grok |
| output/create-mermaid-visualization.md | output | 3 | no | grok |
| output/cyber-security-specialist.md | output | 2 | no | grok |
| output/diagram-generator.md | output | 3 | no | grok |
| output/excel-sheet.md | output | 3 | no | grok |
| output/journalist.md | output | 2 | no | grok |
| output/json-enforcer.md | output | 4 | no | grok |
| output/large-language-models-security-specialist.md | output | 2 | no | grok |
| output/regex-generator.md | output | 3 | no | grok |
| output/to-flashcards.md | output | 3 | yes | grok |
| output/transcribe-minutes.md | output | 2 | no | grok |
| output/xml-framing.md | output | 3 | no | grok |
| professional/analyze-candidates.md | professional | 2 | no | grok |
| professional/architecture-decision-record.md | professional | 5 | no | grok |
| professional/career-coach.md | professional | 2 | no | grok |
| professional/career-counselor.md | professional | 2 | no | grok |
| professional/create-prd.md | professional | 3 | no | grok |
| professional/job-interviewer.md | professional | 3 | yes | grok |
| professional/legal-advisor.md | professional | 1 | yes | grok |
| professional/product-manager.md | professional | 2 | yes | grok |
| professional/project-manager.md | professional | 1 | yes | grok |
| professional/recruiter.md | professional | 2 | yes | grok |
| professional/requirements-quality-checklist.md | professional | 5 | no | grok |
| professional/seo-consultant.md | professional | 2 | yes | grok |
| professional/social-media-manager.md | professional | 2 | yes | grok |
| professional/startup-idea-generator.md | professional | 3 | yes | grok |
| professional/startup-tech-lawyer.md | professional | 2 | yes | grok |
| professional/web-design-consultant.md | professional | 2 | yes | grok |
| reasoning/adaptive-rag-gates.md | reasoning | 5 | no | grok |
| reasoning/bull-bear-research-debate.md | reasoning | 5 | no | grok |
| reasoning/chain-of-thought.md | reasoning | 3 | yes | grok |
| reasoning/check-falsifiability.md | reasoning | 4 | yes | grok |
| reasoning/data-analyst.md | reasoning | 2 | yes | grok |
| reasoning/data-scientist.md | reasoning | 1 | yes | grok |
| reasoning/decomposition.md | reasoning | 3 | yes | grok |
| reasoning/deep-research-supervisor.md | reasoning | 5 | no | grok |
| reasoning/expert-persona.md | reasoning | 3 | yes | grok |
| reasoning/financial-analyst.md | reasoning | 1 | yes | grok |
| reasoning/find-logical-fallacies.md | reasoning | 2 | yes | grok |
| reasoning/graph-of-thoughts.md | reasoning | 5 | no | grok |
| reasoning/llm-researcher.md | reasoning | 2 | yes | grok |
| reasoning/logic-builder-tool.md | reasoning | 3 | yes | grok |
| reasoning/mathematician.md | reasoning | 3 | yes | grok |
| reasoning/philosopher.md | reasoning | 2 | yes | grok |
| reasoning/readability-logic-simulator.md | reasoning | 1 | yes | grok |
| reasoning/refinement-loop.md | reasoning | 5 | no | grok |
| reasoning/root-cause-analyst.md | reasoning | 3 | yes | grok |
| reasoning/self-consistency.md | reasoning | 3 | yes | grok |
| reasoning/self-discover-plan.md | reasoning | 5 | no | grok |
| reasoning/self-refinement.md | reasoning | 3 | yes | grok |
| reasoning/statistician.md | reasoning | 2 | yes | grok |
| reasoning/step-back.md | reasoning | 3 | yes | grok |
| reasoning/storm-persona-outline-polish.md | reasoning | 5 | no | grok |
| reasoning/tree-of-thoughts.md | reasoning | 2 | yes | grok |
| system/agent-graph-cycle.md | system | 5 | no | grok |
| system/claude-soul-principles.md | system | 3 | yes | grok |
| system/coding-assistant.md | system | 4 | yes | grok |
| system/improve-prompt.md | system | 2 | yes | grok |
| system/persistent-skill-evolution.md | system | 5 | no | grok |
| system/seo-bet-scale-lifecycle.md | system | 5 | no | grok |
| system/support-triage-investigate-hold.md | system | 5 | no | grok |
| system/test-driven-agent-skill-authoring.md | system | 5 | no | grok |

## 2. Statistics

**Repo-wide overall mean:** 3.0535  (sum 1142 / 374 = 3.053476 → **3.05**)

### Histogram (overall 5 → 1)

| overall | count | share |
|---:|---:|---:|
| 5 | 80 | 21.4% |
| 4 | 34 | 9.1% |
| 3 | 115 | 30.7% |
| 2 | 116 | 31.0% |
| 1 | 29 | 7.8% |
| **total** | **374** | 100% |

Histogram row: `5:80  4:34  3:115  2:116  1:29`

### Per-category means and fab split

| category | n | mean overall | fab yes | fab no | fab rate |
|---|---:|---:|---:|---:|---:|
| code | 58 | 3.45 | 32 | 26 | 55% |
| context | 3 | 3.33 | 1 | 2 | 33% |
| creative | 11 | 2.36 | 11 | 0 | 100% |
| debug | 17 | 2.88 | 12 | 5 | 71% |
| defensive | 24 | 3.00 | 19 | 5 | 79% |
| education | 11 | 1.55 | 11 | 0 | 100% |
| model-optimized | 188 | 3.09 | 37 | 151 | 20% |
| output | 12 | 2.75 | 1 | 11 | 8% |
| professional | 16 | 2.44 | 10 | 6 | 62% |
| reasoning | 26 | 3.12 | 19 | 7 | 73% |
| system | 8 | 4.25 | 3 | 5 | 38% |
| **all** | **374** | **3.05** | **156** | **218** | **42%** |

**Fab-flag total:** 156 / 374 (41.7%).

Per-category overall histogram:

| category | 5 | 4 | 3 | 2 | 1 |
|---|---:|---:|---:|---:|---:|
| code | 26 | 1 | 8 | 19 | 4 |
| context | 0 | 1 | 2 | 0 | 0 |
| creative | 0 | 0 | 4 | 7 | 0 |
| debug | 5 | 0 | 4 | 4 | 4 |
| defensive | 5 | 4 | 4 | 8 | 3 |
| education | 0 | 0 | 2 | 2 | 7 |
| model-optimized | 30 | 25 | 71 | 56 | 6 |
| output | 0 | 1 | 7 | 4 | 0 |
| professional | 2 | 0 | 3 | 9 | 2 |
| reasoning | 7 | 1 | 9 | 6 | 3 |
| system | 5 | 1 | 1 | 1 | 0 |

## 3. Actionable ranked lists

### (a) RETIRE-CANDIDATES — overall ≤ 2

**Count: 145** (29 at overall 1, 116 at overall 2).

Ranked worst-first. Top examples = all overall-1 rows with judge reasons, then representative overall-2 rows.

#### Overall = 1 (n=29) — retire first

| file | category | fab | reason |
|---|---|:---:|---|
| code/ethereum-developer.md | code | yes | Hardcoded messenger-contract demo; not reusable; unevidenced Works well. |
| code/fullstack-software-developer.md | code | yes | Hardcoded Golang/Angular demo; not reusable; unevidenced Works well. |
| code/github-expert.md | code | yes | One-shot GitHub persona; hardcoded fork request; unevidenced Works well. |
| code/senior-frontend-developer.md | code | yes | Hardcoded Pokemon/Vite demo; not reusable; unevidenced Works well. |
| debug/bug-risk-analysis.md | debug | yes | Finished pm-agent report sold as a reusable analysis prompt. |
| debug/security-fixes-cves.md | debug | yes | Bullet slogans, not a prompt; claims AI accelerated velocity. |
| debug/security-fixes.md | debug | yes | Incomplete stub with 'Step 2: ...'; Works-well on empty instructions. |
| debug/want-to-analyze-security-issues-and-vulnerabilitie.md | debug | yes | Marketing notes, not a prompt; invented upgrade-success claim. |
| defensive/plagiarism-checker.md | defensive | yes | Misnamed evasion rewriter, not a checker; fake tests. |
| defensive/tech-reviewer.md | defensive | yes | One-line gadget-review persona; hardcoded example; fake tests. |
| defensive/update-checker.md | defensive | yes | One-off Pydroid script request mislabeled as update checker. |
| education/ai-writing-tutor.md | education | yes | Generic tutor persona; no rubric, loop, or stop. |
| education/debate-coach.md | education | yes | Roleplay coach with one hardcoded motion; no drill structure. |
| education/life-coach.md | education | yes | Generic life-coach persona; no method or boundaries. |
| education/math-teacher.md | education | yes | Generic explain-math persona; no pedagogy or stop. |
| education/motivational-coach.md | education | yes | Affirmation persona; no protocol or limits. |
| education/philosophy-teacher.md | education | yes | Generic explain-philosophy persona; no method. |
| education/public-speaking-coach.md | education | yes | Roleplay coach; no session structure or criteria. |
| model-optimized/benchmarks/coding.md | model-optimized | yes | Fake HumanEval table and pass-rate theater, not a reusable prompt. |
| model-optimized/benchmarks/reasoning.md | model-optimized | yes | Fabricated MMLU/GSM8K grid; CoT stubs; garbled advice table. |
| model-optimized/meta/llama-3.2/general.md | model-optimized | no | Empty “just talk naturally” stub; not an operational prompt. |
| model-optimized/mistral/mistral-nemo/general.md | model-optimized | no | Near-empty task lines; tips are license/size marketing. |
| model-optimized/mistral/mixtral/analysis.md | model-optimized | no | Three hollow analysis shells; MoE tips are fluff. |
| model-optimized/openai/o3-mini/reasoning.md | model-optimized | yes | Near-empty stubs; unevidenced cost-effectiveness and capability claims. |
| professional/legal-advisor.md | professional | yes | Advice-only legal persona; no jurisdiction, disclaimer, or halt. |
| professional/project-manager.md | professional | yes | Assistant PRD reply misfiled as project-manager prompt; Works-well. |
| reasoning/data-scientist.md | reasoning | yes | Imaginary app-engagement persona; no data, method, or output. |
| reasoning/financial-analyst.md | reasoning | yes | Broken-punctuation market-prediction ask; Works-well on garbage. |
| reasoning/readability-logic-simulator.md | reasoning | yes | Truncated HTML-to-Markdown engine; invented fetch_html; Works-well. |

#### Overall = 2 (n=116) — by category

| category | overall=2 |
|---|---:|
| code | 19 |
| creative | 7 |
| debug | 4 |
| defensive | 8 |
| education | 2 |
| model-optimized | 56 |
| output | 4 |
| professional | 9 |
| reasoning | 6 |
| system | 1 |

Representative overall-2 reasons (worst-path / typical failure modes):

| file | category | fab | reason |
|---|---|:---:|---|
| code/brutal-reviewer.md | code | yes | Thin ruthless-reviewer persona; unevidenced GPT/Claude/Llama quality claims. |
| code/code-reviewer.md | code | yes | One-sentence reviewer persona; dummy variables; unevidenced Works-well claims. |
| creative/advertiser.md | creative | yes | Energy-drink advertiser persona; no brief, metrics, or stop. |
| creative/artist-advisor.md | creative | yes | Broken run-on artist advisor; no deliverable shape; Works-well claims. |
| debug/comprehensive-repository-analysis-and-bug-fixing-f.md | debug | yes | Unbounded fix-all-bugs theater; cannot execute as specified; Works-well. |
| debug/sentry-bug-fixer.md | debug | yes | Generic Sentry role; no event schema, repro, or deploy halt. |
| defensive/accessibility-auditor.md | defensive | yes | WCAG 2.2 name-drop; no pages, tools, or fail criteria; Works-well. |
| defensive/comprehensive-content-review-plan.md | defensive | yes | Katex leftover review plan; no standards or halt; Works-well. |
| education/instructor-in-a-school.md | education | yes | Beginner algorithms with examples; still one-shot persona, fake tests. |
| education/teacher-of-react-js.md | education | yes | One-shot React curriculum table; no progression or stops. |
| model-optimized/anthropic/claude-3.7-sonnet/reasoning.md | model-optimized | no | Thin hybrid-reasoning stub; little operational meat. |
| model-optimized/anthropic/claude-opus-4.7/analysis.md | model-optimized | yes | Forced health scores and unmatched-vision claims without evidence. |
| output/cyber-security-specialist.md | output | no | Classic act-as one-liner; no method, format, or stop conditions. |
| output/journalist.md | output | no | Act-as journalist with no sourcing, verification, or no-invention rules. |
| professional/analyze-candidates.md | professional | no | Job-candidate wrapper actually compares election candidates; unsourced. |
| professional/career-coach.md | professional | no | Generic act-as career coach; no format, sourcing, or stop rules. |
| reasoning/data-analyst.md | reasoning | yes | Generic analyst bullets; no schema, dataset contract, or stop. |
| reasoning/find-logical-fallacies.md | reasoning | yes | Wikipedia fallacy dump; 15-word list output; unevidenced Works-well. |
| system/improve-prompt.md | system | yes | OpenAI-guide dump plus three rewrite steps; unevidenced Works-well. |

Complete overall-2 file list:

- **code** (19): `code/brutal-reviewer.md`, `code/code-reviewer.md`, `code/commit-message-generator.md`, `code/dax-terminal.md`, `code/debugger-interactive.md`, `code/developer-relations-consultant.md`, `code/devops-engineer.md`, `code/generate-code-rules.md`, `code/it-architect.md`, `code/javascript-console.md`, `code/linux-terminal.md`, `code/machine-learning-engineer.md`, `code/password-generator.md`, `code/php-interpreter.md`, `code/python-interpreter.md`, `code/r-interpreter.md`, `code/software-quality-assurance-tester.md`, `code/unit-tester.md`, `code/ux-ui-developer.md`
- **creative** (7): `creative/advertiser.md`, `creative/artist-advisor.md`, `creative/essay-writer.md`, `creative/novelist.md`, `creative/screenwriter.md`, `creative/stand-up-comedian.md`, `creative/storyteller.md`
- **debug** (4): `debug/comprehensive-repository-analysis-and-bug-fixing-f.md`, `debug/sentry-bug-fixer.md`, `debug/stackoverflow-post.md`, `debug/tech-troubleshooter.md`
- **defensive** (8): `defensive/accessibility-auditor.md`, `defensive/comprehensive-content-review-plan.md`, `defensive/comprehensive-web-application-development-with-sec.md`, `defensive/journal-reviewer.md`, `defensive/llm-security-specialist.md`, `defensive/pull-request-review-assistant.md`, `defensive/website-security-vulnerability-checker.md`, `defensive/write-hackerone-report.md`
- **education** (2): `education/instructor-in-a-school.md`, `education/teacher-of-react-js.md`
- **model-optimized** (56): `model-optimized/anthropic/claude-3.7-sonnet/reasoning.md`, `model-optimized/anthropic/claude-opus-4.7/analysis.md`, `model-optimized/anthropic/claude-opus-4.7/coding.md`, `model-optimized/anthropic/claude-sonnet-4/coding.md`, `model-optimized/anthropic/claude-sonnet-4/reasoning.md`, `model-optimized/benchmarks/instruction-following.md`, `model-optimized/benchmarks/safety.md`, `model-optimized/cohere/command-r-plus/analysis.md`, `model-optimized/cohere/command-r/analysis.md`, `model-optimized/deepseek/deepseek-coder/debugging.md`, `model-optimized/deepseek/deepseek-coder/generation.md`, `model-optimized/deepseek/deepseek-coder/refactoring.md`, `model-optimized/deepseek/deepseek-coder/review.md`, `model-optimized/deepseek/deepseek-r1/coding.md`, `model-optimized/deepseek/deepseek-r1/reasoning.md`, `model-optimized/deepseek/deepseek-v3/analysis.md`, `model-optimized/deepseek/deepseek-v3/coding.md`, `model-optimized/deepseek/deepseek-v3/math.md`, `model-optimized/deepseek/deepseek-v4-flash/coding.md`, `model-optimized/deepseek/deepseek-v4-pro/coding.md`, `model-optimized/deepseek/deepseek-v4-pro/reasoning.md`, `model-optimized/google/gemini-2.5-flash/coding.md`, `model-optimized/google/gemini-2.5-flash/long-context.md`, `model-optimized/google/gemini-2.5-flash/quick-tasks.md`, `model-optimized/google/gemini-2/analysis.md`, `model-optimized/google/gemini-2/coding.md`, `model-optimized/google/gemini-2/multimodal.md`, `model-optimized/google/gemini-flash/basic.md`, `model-optimized/google/gemini-flash/long-context.md`, `model-optimized/google/gemini-pro/analysis.md`, `model-optimized/google/gemini-pro/coding.md`, `model-optimized/meta/llama-3.2/multimodal.md`, `model-optimized/meta/llama-3.3/analysis.md`, `model-optimized/meta/llama-3.3/coding.md`, `model-optimized/mistral/codestral/coding.md`, `model-optimized/mistral/mixtral/coding.md`, `model-optimized/openai/gpt-3.5-turbo/quick-tasks.md`, `model-optimized/openai/gpt-4-turbo/coding.md`, `model-optimized/openai/gpt-4/analysis.md`, `model-optimized/openai/o1/reasoning.md`, `model-optimized/qwen/qwen-2.5/json-output.md`, `model-optimized/qwen/qwen-3.5/basic.md`, `model-optimized/qwen/qwen-3.5/coding.md`, `model-optimized/qwen/qwen-3.5/json-output.md`, `model-optimized/qwen/qwen-3/coding.md`, `model-optimized/qwen/qwen-3/multilingual.md`, `model-optimized/roles/business.md`, `model-optimized/roles/creative.md`, `model-optimized/small-models/gemma-2/simple-tasks.md`, `model-optimized/small-models/phi-3.5/basic.md`, `model-optimized/xai/grok-2/analysis.md`, `model-optimized/xai/grok-2/coding.md`, `model-optimized/xai/grok-2/creative.md`, `model-optimized/xai/grok-2/realtime.md`, `model-optimized/xai/grok-3/coding.md`, `model-optimized/xai/grok-3/reasoning.md`
- **output** (4): `output/cyber-security-specialist.md`, `output/journalist.md`, `output/large-language-models-security-specialist.md`, `output/transcribe-minutes.md`
- **professional** (9): `professional/analyze-candidates.md`, `professional/career-coach.md`, `professional/career-counselor.md`, `professional/product-manager.md`, `professional/recruiter.md`, `professional/seo-consultant.md`, `professional/social-media-manager.md`, `professional/startup-tech-lawyer.md`, `professional/web-design-consultant.md`
- **reasoning** (6): `reasoning/data-analyst.md`, `reasoning/find-logical-fallacies.md`, `reasoning/llm-researcher.md`, `reasoning/philosopher.md`, `reasoning/statistician.md`, `reasoning/tree-of-thoughts.md`
- **system** (1): `system/improve-prompt.md`

### (b) FAB-LIST — all fab=yes, grouped by fabrication type

**Count: 156.** Primary type from judge reason (benchmark keywords > invented metrics/numbers/fake tests > Works-well / Excellent / GPT-Claude-Llama claim tables). Remaining persona-thin fab flags default to Works-well tables — that is the corpus’s typical unevidenced Tested-On vehicle.

| type | count |
|---|---:|
| Works well tables | 121 |
| invented metrics | 30 |
| benchmark tables | 5 |
| **total** | **156** |

#### Works well tables (n=121)

| file | overall | reason |
|---|---:|---|
| code/brutal-reviewer.md | 2 | Thin ruthless-reviewer persona; unevidenced GPT/Claude/Llama quality claims. |
| code/code-reviewer-extended.md | 3 | Five-pass review format; unevidenced GPT/Claude/Codex thoroughness claims. |
| code/code-reviewer.md | 2 | One-sentence reviewer persona; dummy variables; unevidenced Works-well claims. |
| code/commit-message-generator.md | 2 | Conventional-commit blob; dummy vars; unevidenced Works-well model claims. |
| code/create-git-diff-commit.md | 3 | Fabric commit writer with conflicting output rules and unevidenced Works well. |
| code/dax-terminal.md | 2 | Roleplay DAX terminal; dummy variables; unevidenced Works-well claims. |
| code/debugger-interactive.md | 2 | Three-format debugger persona; no variables; unevidenced Excellent/thorough claims. |
| code/developer-relations-consultant.md | 2 | DevRel persona; dummy vars; unevidenced Works-well claims. |
| code/devops-engineer.md | 2 | Generic DevOps persona; dummy vars; unevidenced Works-well claims. |
| code/ethereum-developer.md | 1 | Hardcoded messenger-contract demo; not reusable; unevidenced Works well. |
| code/explain-code.md | 3 | Fabric explainer with output sections; dummy vars; unevidenced Works well. |
| code/fullstack-software-developer.md | 1 | Hardcoded Golang/Angular demo; not reusable; unevidenced Works well. |
| code/generate-code-rules.md | 2 | Short rules distiller; dummy vars; unevidenced Works-well claims. |
| code/github-expert.md | 1 | One-shot GitHub persona; hardcoded fork request; unevidenced Works well. |
| code/it-architect.md | 2 | Generic IT-architect persona; dummy vars; unevidenced Works well. |
| code/javascript-console.md | 2 | JS-console roleplay; dummy vars; unevidenced Works-well claims. |
| code/linux-terminal.md | 2 | Linux-terminal roleplay; dummy vars; unevidenced Works-well claims. |
| code/machine-learning-engineer.md | 2 | ML explainer persona; dummy vars; unevidenced Works-well claims. |
| code/password-generator.md | 2 | Password-generator roleplay; dummy vars; unevidenced Works-well claims. |
| code/php-interpreter.md | 2 | PHP-interpreter roleplay; dummy vars; unevidenced Works-well claims. |
| code/python-interpreter.md | 2 | Python-interpreter roleplay; dummy vars; unevidenced Works-well claims. |
| code/r-interpreter.md | 2 | R-interpreter roleplay; dummy vars; unevidenced Works-well claims. |
| code/review-code.md | 3 | Structured Fabric review with example; dummy vars; unevidenced Works well. |
| code/senior-engineer.md | 4 | Strong agentic system prompt; unevidenced battle-tested and Works-well claims. |
| code/senior-frontend-developer.md | 1 | Hardcoded Pokemon/Vite demo; not reusable; unevidenced Works well. |
| code/software-quality-assurance-tester.md | 2 | Roleplay login test; tautological When-to-Use; no app, format, or halt. |
| code/svg-designer.md | 3 | SVG-to-base64 markdown-only protocol; no validation; unevidenced Works-well. |
| code/tdd-generator.md | 3 | Tests-then-code skeleton; no runner or stops; Excellent/Native-strength claims. |
| code/unit-tester.md | 2 | One-sentence unit-test teacher; no cases, runner, or stop rules. |
| code/ux-ui-developer.md | 2 | Tautological UX persona; no method, deliverable, or halt conditions. |
| code/web-browser.md | 3 | Imaginary-web protocol with numbered links; unevidenced Works-well table. |
| context/few-shot-negatives.md | 3 | Good/bad few-shot shell; no task freeze; qualitative model-fit claims. |
| creative/advertiser.md | 2 | Energy-drink advertiser persona; no brief, metrics, or stop. |
| creative/artist-advisor.md | 2 | Broken run-on artist advisor; no deliverable shape; Works-well claims. |
| creative/ascii-artist.md | 3 | ASCII-only code-block protocol; thin but clear output rule; Works-well. |
| creative/create-art-prompt.md | 3 | Fabric art-prompt steps with identity fluff; Works-well; no empty-input halt. |
| creative/essay-writer.md | 2 | Broken-punctuation essay persona; no sources, length, or stop. |
| creative/novelist.md | 2 | Genre-agnostic novelist roleplay; no outline, constraints, or halt. |
| creative/scamper.md | 3 | Seven-lens SCAMPER fill-in; concrete angles, no quality or stop gates. |
| creative/screenwriter.md | 2 | Paris-romance screenwriter persona; no format, length, or stop. |
| creative/stand-up-comedian.md | 2 | Politics stand-up roleplay; no length, audience, or off-limits. |
| creative/storyteller.md | 2 | Audience-theme storyteller persona; no length, structure, or halt. |
| creative/tech-writer.md | 3 | Guide-from-steps with screenshot markers; Works-well; thin stop rules. |
| debug/bug-risk-analysis.md | 1 | Finished pm-agent report sold as a reusable analysis prompt. |
| debug/comprehensive-repository-analysis-and-bug-fixing-f.md | 2 | Unbounded fix-all-bugs theater; cannot execute as specified; Works-well. |
| debug/debugger-extended.md | 3 | Observe-hypothesize-fix outline; textbook-thin; unevidenced Excellent claims. |
| debug/rubber-duck.md | 3 | One-question Socratic mentor; real don't-answer rule; qualitative model claims. |
| debug/security-fixes.md | 1 | Incomplete stub with 'Step 2: ...'; Works-well on empty instructions. |
| debug/sentry-bug-fixer.md | 2 | Generic Sentry role; no event schema, repro, or deploy halt. |
| debug/stack-trace-analyzer.md | 3 | Three-step trace pin; no missing-trace halt; Excellent claims. |
| debug/stackoverflow-post.md | 2 | Contradicts explain vs no-explanations; unevidenced Works-well. |
| debug/tech-troubleshooter.md | 2 | Steps-only hardware persona; generic first issue; Works-well. |
| debug/test-first-bug-fixing-approach.md | 3 | Eight-step TDD fix; forbids questions; unbounded ALL-tests loop. |
| defensive/accessibility-auditor.md | 2 | WCAG 2.2 name-drop; no pages, tools, or fail criteria; Works-well. |
| defensive/act-as-a-resume-reviewer.md | 3 | JD/resume variables plus confidentiality; no scoring rubric or stop. |
| defensive/analyze-malware.md | 4 | Structured IoC/ATT&CK extract with no-invent-IOCs; still Works-well table. |
| defensive/comprehensive-content-review-plan.md | 2 | Katex leftover review plan; no standards or halt; Works-well. |
| defensive/comprehensive-web-application-development-with-sec.md | 2 | Nested YAML, generic fullstack roleplay, unevidenced Works-well tests. |
| defensive/contrarian.md | 4 | Tight contrarian brief; generic unevidenced model-test table. |
| defensive/create-stride-threat-model.md | 4 | Solid STRIDE schema; theatrical think-time and generic test claims. |
| defensive/greybeard-secure-prompt-engineer.md | 3 | Persona scaffolding without concrete injection tests or stop criteria. |
| defensive/journal-reviewer.md | 2 | One-line persona, hardcoded paper, no review criteria or stops. |
| defensive/llm-security-specialist.md | 2 | Generic security-persona request without methodology or refusal bounds. |
| defensive/update-checker.md | 1 | One-off Pydroid script request mislabeled as update checker. |
| defensive/website-security-vulnerability-checker.md | 2 | URL-in generic vuln scan, no method, legal line only. |
| defensive/write-hackerone-report.md | 2 | Report template plus exploit-generation and anti-refusal fluff. |
| education/ai-writing-tutor.md | 1 | Generic tutor persona; no rubric, loop, or stop. |
| education/debate-coach.md | 1 | Roleplay coach with one hardcoded motion; no drill structure. |
| education/life-coach.md | 1 | Generic life-coach persona; no method or boundaries. |
| education/math-teacher.md | 1 | Generic explain-math persona; no pedagogy or stop. |
| education/motivational-coach.md | 1 | Affirmation persona; no protocol or limits. |
| education/philosophy-teacher.md | 1 | Generic explain-philosophy persona; no method. |
| education/public-speaking-coach.md | 1 | Roleplay coach; no session structure or criteria. |
| education/teacher-of-react-js.md | 2 | One-shot React curriculum table; no progression or stops. |
| model-optimized/anthropic/claude-opus-4.5/coding.md | 3 | Architecture/review shells plus unevidenced Excellent/Great tips. |
| model-optimized/anthropic/claude-opus-4.5/reasoning.md | 3 | XML thinking shells; unevidenced Excellent multi-perspective claims. |
| model-optimized/anthropic/claude-opus-4.7/coding.md | 2 | Autonomous no-questions loop; unevidenced self-test excellence. |
| model-optimized/anthropic/claude-opus-4.7/reasoning.md | 3 | Known/infer/assume RCA; unevidenced calibrate-well tips. |
| model-optimized/anthropic/claude-sonnet-4/coding.md | 2 | Thin XML stubs; unevidenced speed/quality balance claims. |
| model-optimized/anthropic/claude-sonnet-4/reasoning.md | 2 | Three-bullet analysis shells; unevidenced structured-analysis tips. |
| model-optimized/deepseek/deepseek-r1/reasoning.md | 2 | Nearly empty zero-shot note plus unevidenced R1-best claims. |
| model-optimized/deepseek/deepseek-v3.1/analysis.md | 3 | Structured analysis templates; unevidenced language/cost tips. |
| model-optimized/openai/gpt-4.1/writing.md | 3 | Paste-ready writing slots; weak stop rules; unevidenced voice claim. |
| model-optimized/openai/gpt-5.4/coding.md | 4 | Agentic multi-file templates; unevidenced autonomous-loop claims. |
| model-optimized/openai/gpt-5.4/reasoning.md | 4 | Solid RCA/decision scaffolds; unevidenced long-chain excellence claims. |
| model-optimized/openai/gpt-5.4/thinking.md | 4 | Thorough thinking procedures; unevidenced native-work-showing claim. |
| model-optimized/openai/gpt-5/coding.md | 3 | Generic full-stack templates; unevidenced excellence tips. |
| model-optimized/openai/gpt-5/reasoning.md | 3 | Adequate stepwise scaffolds; unevidenced Works-well tip line. |
| model-optimized/openai/o1/reasoning.md | 2 | Intentionally empty wrappers; unevidenced works-best domain claims. |
| model-optimized/openai/o3/coding.md | 3 | Mixed one-shot palindrome and templates; unevidenced excellence claim. |
| model-optimized/openai/o3/reasoning.md | 3 | Mix of hardcoded integral and thin slots; unevidenced behavior claims. |
| professional/job-interviewer.md | 3 | Interviewer roleplay waits one question; no rubric, debrief, or stop. |
| professional/legal-advisor.md | 1 | Advice-only legal persona; no jurisdiction, disclaimer, or halt. |
| professional/product-manager.md | 2 | PRD header list with typos; tautological when-to-use; Works-well. |
| professional/project-manager.md | 1 | Assistant PRD reply misfiled as project-manager prompt; Works-well. |
| professional/recruiter.md | 2 | Recruiter sourcing persona; CV request mismatches job; no method. |
| professional/seo-consultant.md | 2 | Hardcoded WebPilot SEO outline; needs live Google; Works-well. |
| professional/social-media-manager.md | 2 | Generic social-media persona; no calendar, metrics, or stop. |
| professional/startup-idea-generator.md | 3 | Wish-to-canvas markdown table; no cost-evidence rule; Works-well. |
| professional/startup-tech-lawyer.md | 2 | One-page DPA draft; no parties, jurisdiction, or legal disclaimer. |
| professional/web-design-consultant.md | 2 | Generic web-design persona; hardcoded jewelry shop; no method. |
| reasoning/chain-of-thought.md | 3 | Canonical step-by-step cue; unevidenced Excellent; no stop rules. |
| reasoning/check-falsifiability.md | 4 | Structured falsifiability audit; AGI-safety padding; unevidenced Works-well. |
| reasoning/data-analyst.md | 2 | Generic analyst bullets; no schema, dataset contract, or stop. |
| reasoning/data-scientist.md | 1 | Imaginary app-engagement persona; no data, method, or output. |
| reasoning/decomposition.md | 3 | Least-to-most steps pasteable; unevidenced Excellent; no halt. |
| reasoning/expert-persona.md | 3 | Role/years/domain skeleton; latent-space fluff; Excellent claims. |
| reasoning/financial-analyst.md | 1 | Broken-punctuation market-prediction ask; Works-well on garbage. |
| reasoning/find-logical-fallacies.md | 2 | Wikipedia fallacy dump; 15-word list output; unevidenced Works-well. |
| reasoning/llm-researcher.md | 2 | LLM-paper explainer persona; no source contract or citation halt. |
| reasoning/logic-builder-tool.md | 3 | Hint-only coding coach; no problem slot or session stop. |
| reasoning/mathematician.md | 3 | Expression-in result-out calculator; Works-well despite PARTIAL smoke. |
| reasoning/philosopher.md | 2 | Generic philosopher persona; hardcoded ethics ask; no method. |
| reasoning/root-cause-analyst.md | 3 | RCA toolkit card; no input schema or evidence-missing halt; Works-well. |
| reasoning/self-consistency.md | 3 | Three-approach majority vote; unevidenced Excellent; no disagreement halt. |
| reasoning/self-refinement.md | 3 | Two-pass self-critique; unevidenced Excellent; no quality threshold. |
| reasoning/statistician.md | 2 | Statistician persona with typos; unanswerable banknote ask; Works-well. |
| reasoning/step-back.md | 3 | Principles-then-apply cue; unevidenced Excellent; no stop. |
| reasoning/tree-of-thoughts.md | 2 | Three-expert theater, not tree search; unevidenced Excellent. |
| system/coding-assistant.md | 4 | Concise coding system prompt with edit format; unevidenced Excellent. |
| system/improve-prompt.md | 2 | OpenAI-guide dump plus three rewrite steps; unevidenced Works-well. |

#### invented metrics (n=30)

| file | overall | reason |
|---|---:|---|
| code/sql-terminal.md | 3 | Fake-DB terminal, table-only replies; invented schema; unevidenced Works-well. |
| debug/security-fixes-cves.md | 1 | Bullet slogans, not a prompt; claims AI accelerated velocity. |
| debug/want-to-analyze-security-issues-and-vulnerabilitie.md | 1 | Marketing notes, not a prompt; invented upgrade-success claim. |
| defensive/analyze-threat-report.md | 3 | Forced 20-trend quotas can invent findings; unevidenced Works-well. |
| defensive/hallucination-reducer.md | 4 | Useful uncertainty rules; unevidenced model-compat table. |
| defensive/plagiarism-checker.md | 1 | Misnamed evasion rewriter, not a checker; fake tests. |
| defensive/pull-request-review-assistant.md | 2 | Vague PR-review bullets, typos, unevidenced tests. |
| defensive/refactoring-expert.md | 3 | Decent catalog and boundaries; implied metrics plus fake tests. |
| defensive/tech-reviewer.md | 1 | One-line gadget-review persona; hardcoded example; fake tests. |
| education/instructor-in-a-school.md | 2 | Beginner algorithms with examples; still one-shot persona, fake tests. |
| education/mathematical-history-teacher.md | 3 | Format plus no-solve rule; still thin and unevidenced tests. |
| education/spoken-english-teacher-and-improver.md | 3 | Tight loop (limit, correct, question); unevidenced tests. |
| model-optimized/advanced-techniques/chain-of-thought.md | 4 | Useful CoT templates; unevidenced 10–20% gain and model-benefit table. |
| model-optimized/anthropic/claude-opus-4.7/analysis.md | 2 | Forced health scores and unmatched-vision claims without evidence. |
| model-optimized/anthropic/claude-opus-4.7/long-horizon.md | 3 | Test-loop with 3-attempt blocker; unevidenced price/excellence tips. |
| model-optimized/anthropic/claude-opus-4/analysis.md | 3 | XML analysis plus filling-gaps and Opus-excels marketing. |
| model-optimized/deepseek/deepseek-v3.1/coding.md | 3 | Full-stack coding shells; unevidenced GPT-4o-class claims. |
| model-optimized/deepseek/deepseek-v4-flash/analysis.md | 3 | Batch analysis shells plus unevidenced 1M/35×-cheaper tips. |
| model-optimized/deepseek/deepseek-v4-flash/coding.md | 2 | Fast-codegen stubs; unevidenced param/cost/CI marketing. |
| model-optimized/deepseek/deepseek-v4-pro/reasoning.md | 2 | Stepwise reasoning; unevidenced GPT-5/Opus competitiveness. |
| model-optimized/few-shot/classification.md | 3 | Clear class exemplars; English “Hello…” labeled Finnish. |
| model-optimized/openai/codex-5.3/coding.md | 3 | Short agentic shells; unevidenced “OpenAI docs” efficiency/Windows claims. |
| model-optimized/openai/gpt-4.1/coding.md | 3 | Usable coding templates; unevidenced GPT-4o comparisons; nested-fence review block. |
| model-optimized/openai/gpt-4.1/instruction-following.md | 4 | Strong MUST/MUST-NOT patterns; unevidenced superiority-over-GPT-4o claim. |
| model-optimized/openai/gpt-4.1/json-output.md | 3 | Solid JSON schemas plus SDK snippet; unevidenced schema-adherence claim. |
| model-optimized/openai/gpt-5.4/analysis.md | 4 | Strong analysis frameworks; unevidenced quantitative-skill tips. |
| model-optimized/openai/o3-mini/reasoning.md | 1 | Near-empty stubs; unevidenced cost-effectiveness and capability claims. |
| output/to-flashcards.md | 3 | Anki principles solid; STEPS vs CSV clash; example rounds 396/74. |
| reasoning/readability-logic-simulator.md | 1 | Truncated HTML-to-Markdown engine; invented fetch_html; Works-well. |
| system/claude-soul-principles.md | 3 | Condensed HHH principles; false “this IS Claude's training” claim. |

#### benchmark tables (n=5)

| file | overall | reason |
|---|---:|---|
| model-optimized/benchmarks/coding.md | 1 | Fake HumanEval table and pass-rate theater, not a reusable prompt. |
| model-optimized/benchmarks/instruction-following.md | 2 | Invented IFEval numbers; a few usable format-constraint snippets. |
| model-optimized/benchmarks/reasoning.md | 1 | Fabricated MMLU/GSM8K grid; CoT stubs; garbled advice table. |
| model-optimized/benchmarks/safety.md | 2 | Invented jailbreak rates; some delimiter defense patterns remain. |
| model-optimized/deepseek/deepseek-v4-pro/coding.md | 2 | Agentic loop plus unevidenced LiveCodeBench 93.7 cost claims. |

### (c) CHAMPIONS — overall = 5

**Count: 80.**

| category | champions |
|---|---:|
| code | 26 |
| debug | 5 |
| defensive | 5 |
| model-optimized | 30 |
| professional | 2 |
| reasoning | 7 |
| system | 5 |

| file | category | fab | judge | reason |
|---|---|:---:|---|---|
| code/api-design-from-requirements.md | code | no | sol | Contract-first API design with named vars, unknowns register, and stop states. |
| code/api-mock-generation.md | code | no | sol | Contract-preserving mocks with isolation proofs and no fabricated test passes. |
| code/browser-exploration-to-verified-playwright-tests.md | code | no | sol | Observe-then-generate Playwright tests with approvals, budget, and real runs. |
| code/clojure-repl-pair-programming.md | code | no | sol | REPL-first Clojure edits with production-effect bans and file-backed checks. |
| code/code-review-reception-pushback.md | code | no | sol | Review-comment ledger with evidence-backed pushback and external-write gates. |
| code/data-pipeline-architecture.md | code | no | sol | Incremental pipeline with replay tests, idempotency, and explicit blockers. |
| code/dependency-framework-upgrade-workflow.md | code | no | sol | Bounded upgrades with baseline, peer matrix, batches, and verified recovery. |
| code/embedded-c-misra-deviations.md | code | no | sol | Embedded C review with MISRA deviation drafts and no-certification gates. |
| code/executable-implementation-plans.md | code | no | sol | Spec-to-task plans with interface contracts and no-execution planning gates. |
| code/fixer-loop.md | code | no | sol | Run-fix-rerun loop with attempt ceiling and same-failure stop. |
| code/gha-node-runtime-upgrade.md | code | no | sol | Actions runtime upgrade with runner compatibility and no auto-publish. |
| code/git-worktree-isolation-baseline.md | code | no | sol | Isolation-first worktree setup with ignore checks and baseline gates. |
| code/javax-to-jakarta-migration.md | code | no | sol | Jakarta migration with JDK exclusions, baseline, and runtime smoke. |
| code/launchdarkly-flag-removal.md | code | no | sol | Flag-removal assessment with freshness, typed values, and write gates. |
| code/logical-git-revert-confirmation.md | code | no | sol | History-preserving revert with exact-SHA plan and YES confirmation. |
| code/mongodb-query-performance-advisor.md | code | no | sol | Read-only query advisor with cost budget and no invented timings. |
| code/multi-stage-dockerfile-builder.md | code | no | sol | Multi-stage Dockerfile with digest pins, secrets, and smoke contract. |
| code/notebook-sample-builder.md | code | no | sol | Notebook builder with run-before-write, paid-call, and redaction gates. |
| code/pyspark-performance-reviewer.md | code | no | sol | Evidence-gated Spark review; no fabricated speedups or cluster edits. |
| code/read-only-test-gap-audit.md | code | no | sol | Read-only coverage audit with literal anchors and P0–P3 ranking. |
| code/refactoring-safety-net.md | code | no | sol | Characterization-first refactor with risk budget and abandon-to-fix. |
| code/salesforce-ui-dev-aura-lwc.md | code | no | sol | LWC delivery with security, a11y, and org-versus-Jest evidence split. |
| code/sql-change-blast-radius-analysis.md | code | no | sol | Read-only SQL dependency trace with evidence classes; never call unused or safe-to-drop. |
| code/tdd-full-cycle.md | code | no | sol | Red-green-refactor with execution evidence, BLOCKED/VERIFIED, no invented tests. |
| code/terraform-iac-reviewer.md | code | no | sol | Plan/state safety review with locking provenance; apply forbidden by default. |
| code/windows-arm64-python-wheel-ci.md | code | no | sol | Native ARM64 wheel CI with compatibility ledger, CI-NOT-RUN, no-publish. |
| debug/backend-performance-profiling.md | debug | no | sol | Measure-then-optimize A/B loop; INCONCLUSIVE allowed; never invent timings. |
| debug/four-phase-root-cause-debugging.md | debug | no | sol | Evidence-before-fix with 3-attempt REASSESS; no invented causal chain. |
| debug/frontend-performance-investigation.md | debug | no | sol | Lab-vs-field frontend investigation; no fabricated vitals; no app edits. |
| debug/mcp-server-release-qa.md | debug | no | sol | Live MCP session QA with PASS/FAIL/BLOCKED; source inspection is not enough. |
| debug/production-incident-command.md | debug | no | sol | Commander-support IR with mutation gate; no invented impact totals. |
| defensive/email-authentication-header-analyzer.md | defensive | no | sol | Precise RFC-aware protocol with hard stop on invented evidence. |
| defensive/evidence-gated-completion-claims.md | defensive | no | sol | Evidence-gated claims with explicit verification states and stops. |
| defensive/security-code-audit.md | defensive | no | sol | Evidence-chained audit with qualitative severity and non-exploit stops. |
| defensive/spec-plan-task-consistency-audit.md | defensive | no | sol | Fail-fast inputs, stable IDs, coverage vs contradiction split. |
| defensive/task-reviewer-compliance-quality.md | defensive | no | sol | Task-gated dual verdicts with revision identity and evidence ledger. |
| model-optimized/anthropic/claude-opus-4.8/analysis.md | model-optimized | no | sol | Evidence ledger, budget stop, sources-as-data, no inferred measures. |
| model-optimized/anthropic/claude-opus-4.8/coding.md | model-optimized | no | sol | Allowlisted autonomous edits, per-criterion evidence, no deploy. |
| model-optimized/anthropic/claude-opus-4.8/reasoning.md | model-optimized | no | sol | Durable decision record with clause table and reopen triggers. |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/analysis.md | model-optimized | no | sol | Visual/source ledger; no pixel estimates; tools only if present. |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/coding.md | model-optimized | no | sol | Harness-verified patch; bans invented terminal output. |
| model-optimized/deepseek/deepseek-v4.1-flash-1017/reasoning.md | model-optimized | no | sol | Independent verifier required; no silent merge of tool scopes. |
| model-optimized/google/gemini-3.8-flash/analysis.md | model-optimized | no | grok | Dense analysis with citation, clock-offset uncertainty, anti-invention. |
| model-optimized/google/gemini-3.8-flash/coding.md | model-optimized | no | grok | Media-to-test and API-migration with verification and stop rules. |
| model-optimized/google/gemini-3.8-flash/reasoning.md | model-optimized | no | grok | Feasibility and tool-plan prompts with uncertainty and stop conditions. |
| model-optimized/moonshot/kimi-k2.7-code/analysis.md | model-optimized | no | grok | Incident and change-surface prompts with evidence and confirmation gates. |
| model-optimized/moonshot/kimi-k2.7-code/coding.md | model-optimized | no | grok | Tool-loop and visual-regression prompts with anti-fake-results rules. |
| model-optimized/moonshot/kimi-k2.7-code/reasoning.md | model-optimized | no | grok | Behavioral-contract and experiment-selection with domain and budget stops. |
| model-optimized/moonshot/kimi-k3/analysis.md | model-optimized | no | grok | Corpus reconciliation and visual-audit with truncation and no-guess rules. |
| model-optimized/moonshot/kimi-k3/coding.md | model-optimized | no | grok | Migration and vision-repair loops with anti-false-done rules. |
| model-optimized/moonshot/kimi-k3/reasoning.md | model-optimized | no | grok | Constraint resolution and falsification-first research with explicit stop. |
| model-optimized/openai/gpt-5.6-sol/analysis.md | model-optimized | no | grok | Evidence locators, no-inference, unverified-calc gates; paste-ready. |
| model-optimized/openai/gpt-5.6-sol/coding.md | model-optimized | no | grok | Schema-first adapter with unexecuted-check and no-guess file rules. |
| model-optimized/openai/gpt-5.6-sol/reasoning.md | model-optimized | no | grok | Policy conflict reporting and VoI without invented probabilities. |
| model-optimized/openai/gpt-6.1-sol/analysis.md | model-optimized | no | grok | Retrieval budget, claim-to-source table, no invented execution. |
| model-optimized/openai/gpt-6.1-sol/coding.md | model-optimized | no | grok | Tool-realism, approval pause, never substitute a plan for a result. |
| model-optimized/openai/gpt-6.1-sol/reasoning.md | model-optimized | no | grok | Hard-constraint validation and no silent relaxation; checkable witnesses. |
| model-optimized/qwen/qwen3.8-2.4t-a95b/coding.md | model-optimized | no | grok | Paper-to-code with no smoke-test-as-reproduction; missing-prereq stop. |
| model-optimized/qwen/qwen3.8-flash-next/coding.md | model-optimized | no | grok | Latency-budgeted patch plus no-mock interaction; measure-or-don't-claim. |
| model-optimized/safety/injection-defense.md | model-optimized | no | grok | Defense-in-depth with code, hierarchy, and honest prompt-only limits. |
| model-optimized/xai/grok-4.6/analysis.md | model-optimized | no | grok | Search-grounded analysis with claim ledger, sampling limits, injection stop. |
| model-optimized/xai/grok-4.6/coding.md | model-optimized | no | grok | Agent coding with mocked search, hostile-input tests, and no-deploy rule. |
| model-optimized/xai/grok-4.6/reasoning.md | model-optimized | no | grok | Claim-testing with falsification, no fake symmetry, unexecuted-code labeling. |
| model-optimized/zhipu/glm-5.3/analysis.md | model-optimized | no | grok | Tool-verified diagnosis plus audit JSON; forbids invented evidence. |
| model-optimized/zhipu/glm-5.3/coding.md | model-optimized | no | grok | End-to-end coding with checklist evidence and noisy-benchmark honesty. |
| model-optimized/zhipu/glm-5.3/reasoning.md | model-optimized | no | grok | Side-effect-aware plans and consistency proofs with unresolved state. |
| professional/architecture-decision-record.md | professional | no | grok | ADR draft with evidence labels, no invented history, Proposed-not-Accepted. |
| professional/requirements-quality-checklist.md | professional | no | grok | Section-linked requirements checklist; gaps explicit; reviewer owns boxes. |
| reasoning/adaptive-rag-gates.md | reasoning | no | grok | Route-grade-generate RAG with separate retry caps and escalate-out. |
| reasoning/bull-bear-research-debate.md | reasoning | no | grok | Capped bull/bear debate; citations required; no orders; human decides. |
| reasoning/deep-research-supervisor.md | reasoning | no | grok | Brief-delegate-compress research with budgets, citations, ResearchComplete. |
| reasoning/graph-of-thoughts.md | reasoning | no | grok | Branch-explore-score-prune-merge with frozen rubric and budget stops. |
| reasoning/refinement-loop.md | reasoning | no | grok | Generate-critique-revise with incumbent, regression guard, typed stops. |
| reasoning/self-discover-plan.md | reasoning | no | grok | SELECT-ADAPT-IMPLEMENT-SOLVE with id bounds, arity checks, BLOCKED. |
| reasoning/storm-persona-outline-polish.md | reasoning | no | grok | Persona interviews with INTERVIEW_COMPLETE, citations, no wiki publish. |
| system/agent-graph-cycle.md | system | no | grok | Worker/reviewer cycles with veto, gap metric, dead-letter, max cycles. |
| system/persistent-skill-evolution.md | system | no | grok | Experience-to-skill loop with leakage screen, promotion gate, decay. |
| system/seo-bet-scale-lifecycle.md | system | no | grok | Scout/engine keyword bets; missing metrics BLOCKED; human SCALE/sunset. |
| system/support-triage-investigate-hold.md | system | no | grok | Cursor-based triage; no unsolicited sends; money/legal HOLD. |
| system/test-driven-agent-skill-authoring.md | system | no | grok | RED-GREEN-REFACTOR skill tests with fresh-context controls and budget. |

## 4. Calibration cross-check — 20-file stratified panel

Earlier tonight’s 20-file panel (canonical sample from `promptkit-quality-eval-20261102.md`):

| stratum | Sol overall mean | Grok overall mean | kimi+deepseek overall mean |
|---|---:|---:|---:|
| A | 4.6 | 4.4 | 4.8 |
| B | 4.4 | 4.4 | 4.6 |
| C | 3.0 | 2.2* | 3.1 |
| D | 2.6 | 1.8 | 2.7 |

\* Grok C substituted `debug/debugger-extended.md` (overall 3) for `code/sql-change-blast-radius-analysis.md` (not scored by Grok in the 20-file panel). kimi/deepseek and Sol C used the canonical five, including sql-change.

Chunk-eval (this map) means on the **same 20 files**:

| stratum | n | chunk mean (this map) | vs Sol 4.6/4.4/… | vs Grok 4.4/4.4/… | vs kimi+ds 4.8/4.6/3.1/2.7 |
|---|---:|---:|---|---|---|
| A | 5 | 5.00 | +0.40 | +0.60 | +0.20 |
| B | 5 | 5.00 | +0.60 | +0.60 | +0.40 |
| C | 5 | 2.80 | -0.20 | n/a (sample mismatch) | -0.30 |
| D | 5 | 1.80 | -0.80 | +0.00 | -0.90 |

Row-level overview:

| stratum | file | chunk | judge | Sol panel | Grok panel | kimi | deepseek | k+ds mean | flag |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| A | code/fixer-loop.md | 5 | sol | 5 | 5 | 5 | 5 | 5.00 |  |
| A | reasoning/graph-of-thoughts.md | 5 | grok | 4 | 4 | 5 | 5 | 5.00 |  |
| A | reasoning/refinement-loop.md | 5 | grok | 5 | 5 | 5 | 5 | 5.00 |  |
| A | system/agent-graph-cycle.md | 5 | grok | 4 | 4 | 4 | 5 | 4.50 |  |
| A | system/persistent-skill-evolution.md | 5 | grok | 5 | 4 | 5 | 4 | 4.50 |  |
| B | code/api-mock-generation.md | 5 | sol | 5 | 4 | 5 | 4 | 4.50 |  |
| B | code/dependency-framework-upgrade-workflow.md | 5 | sol | 4 | 4 | 5 | 4 | 4.50 |  |
| B | code/mongodb-query-performance-advisor.md | 5 | sol | 5 | 5 | 4 | 5 | 4.50 |  |
| B | code/terraform-iac-reviewer.md | 5 | sol | 5 | 5 | 5 | 5 | 5.00 |  |
| B | reasoning/adaptive-rag-gates.md | 5 | grok | 3 | 4 | 4 | 5 | 4.50 |  |
| C | code/code-reviewer-extended.md | 3 | sol | 4 | 3 | 4 | 5 | 4.50 |  |
| C | code/create-git-diff-commit.md | 3 | sol | 2 | 2 | 3 | 2 | 2.50 |  |
| C | code/sql-change-blast-radius-analysis.md | 5 | sol | 5 | — | 5 | 4 | 4.50 |  |
| C | debug/bug-risk-analysis.md | 1 | sol | 1 | 1 | 2 | 1 | 1.50 |  |
| C | debug/comprehensive-repository-analysis-and-bug-fixing-f.md | 2 | sol | 3 | 2 | 2 | 3 | 2.50 |  |
| D | model-optimized/deepseek/deepseek-r1/coding.md | 2 | sol | 3 | 2 | 4 | 4 | 4.00 | INCONSISTENCY chunk≤2 vs panel≥4 |
| D | model-optimized/google/gemini-pro/coding.md | 2 | grok | 3 | 2 | 2 | 3 | 2.50 |  |
| D | model-optimized/meta/llama-3.2/general.md | 1 | grok | 2 | 1 | 2 | 2 | 2.00 |  |
| D | model-optimized/qwen/qwen-3/coding.md | 2 | grok | 3 | 2 | 2 | 3 | 2.50 |  |
| D | model-optimized/qwen/qwen-3/multilingual.md | 2 | grok | 2 | 2 | 2 | 3 | 2.50 |  |

Grok C substitution (not in canonical 20): `debug/debugger-extended.md` — Grok panel overall 3, chunk overall 3 (sol-B). No flag.

### Inconsistency flags (chunk ≤2 vs any earlier panel score ≥4, or the reverse)

**1 file(s):**

- `model-optimized/deepseek/deepseek-r1/coding.md` — chunk overall 2; earlier panel scores [3, 2, 4, 4]. INCONSISTENCY: chunk≤2 vs panel≥4.

Notes:

- A/B subset is at ceiling in the chunk map (mean 5.00) vs earlier panel 4.4–4.8. Direction is the same; chunk judges did not use the mid-4s the 20-file panel used for graph-of-thoughts / agent-graph / adaptive-rag / api-mock.
- D subset is harsher in the chunk map (mean 1.80) vs kimi+deepseek 2.70, matching Grok’s 20-file D mean (1.80). Sol D panel was 2.6.
- The only ≤2-vs-≥4 clash is `model-optimized/deepseek/deepseek-r1/coding.md`: chunk **2** (sol-D) vs kimi 4 + deepseek 4 (panel mean 4.00). Sol panel 3, Grok panel 2. Treat as judge-disagreement on a 100-word stub, not a quality reversal.
- No file that scored ≤2 in the earlier panel scores ≥4 in this chunk map.

## Parent summary

Counts verified 374/374 (0 missing, 0 dup). Repo mean **3.05**. Histogram 5→1: 80/34/115/116/29. Fab **156**. Retire ≤2: **145**. Champions (5): **80**. Path: `/home/Petsku/.hermes/cache/scratch/promptkit-repo-eval-FULL-20261102.md`.

