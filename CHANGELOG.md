# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2026-11-02

### Changed
- **Quality restructure:** retired 145 low-quality prompt files (overall ≤2 in the Sol+Grok 4-judge whole-repo eval; recoverable via `git show 5849f6b:<path>`, manifest `RETIRED-2026-11-02.md`) and stripped unevidenced claims from 62 files; catalog now **262 curated prompts**
- **Re-authored 33 Tier-1 model-optimized prompt files** (Claude 3.x/4.x, DeepSeek V3/V4/R1, Gemini 2.5 Flash, Codestral, Qwen 3/3.5, Llama 3.2/3.3, Grok 2/3, o3-mini) as long-form vendor-doc-grounded prompts (401–729 words) with per-model README restorations; honest shutdown/supersession wording (o3-mini → gpt-5.6-sol, grok-3 → grok-4.6)
- Retired-legacy generations (GPT-3.5/4, Qwen 2.5, Mixtral/Nemo, Command R, Gemma 2/Phi-3.5, benchmark stubs) archived by tier-list decision
- Harness: `--files` filter for targeted smoke sweeps; reauth smoke of the 33 files (FOLLOWED 33 / PARTIAL 33 thinking-cap / FAILED 0)

## [0.5.0] - 2026-11-02

### Added
- 95 prompt files (0 new patterns); catalog now 374 curated prompts
- Model-optimized expansion for 11 newest families (gpt-6.1-sol, gpt-5.6-sol, claude-opus-4.8, gemini-3.8-flash, grok-4.6, kimi-k3, kimi-k2.7-code, qwen3.8, qwen3.8-flash-next, deepseek-v4.1-flash-1017, glm-5.3): 66 authored prompts (source: promptkit-authored; bd485f9)
- Curated coding and agentic/MCP workflows via the two-hunt blind-review + adaptation pipeline (MIT sources: awesome-copilot, superpowers, spec-kit, Fabric, Loopany, wshobson)
- Loop/graph families: refinement-loop, fixer-loop, graph-of-thoughts, agent-graph-cycle, persistent-skill-evolution (GoT paper + LangGraph + 2026 arXiv grounding ≤3kk)
- Smoke-test harness (`scripts/prompt_smoke_test.py`) and a full 374×2 two-model structural sweep (FOLLOWED 598 / PARTIAL 150 / FAILED 0). Structural status only — not a quality benchmark
- NOTICE now covers 5 new upstream notices, including the first Apache-2.0 (TradingAgents)

### Changed
- generate_docs.py type annotations, surfaced by broadened mypy scope (src+scripts); behavior unchanged

## [0.4.0] - 2026-11-01

### Added
- NOTICE.md — third-party attribution manifest (Fabric MIT notice verbatim, CC0 markings for prompts.chat and Awesome ChatGPT Prompts), backed by a full repository content audit
- YAML frontmatter metadata for all 290 prompts and 19 patterns (category, subcategory, source, license, model) with registry getters: get_pattern_metadata / get_pattern_category / get_pattern_attribution / get_pattern_license
- generate_docs.py --check — drift lint that exits 1 when the docs mirror does not match regenerated output
- py.typed + mypy check_untyped_defs; separate CI typing job
- CI: wheel-smoke job (fresh venv, non-editable install), tiktoken extra job (verified exact token counting), Python 3.13/3.14 in the test matrix
- CONTRIBUTING.md attribution guidelines

### Changed
- CLI contract: prompts --show resolves model-optimized/* paths (the README example now works); every "not found" path exits 1 instead of 0
- Doctor: empty prompt exits 2 with a clear message ({"error":"empty"} in JSON mode); providing text AND --file exits 2 ("either/or"); positional FILE treated as --file
- Doctor analyze split into doctor_heuristics.py + doctor_reports.py (behavior verified identical against a 850-prompt baseline)
- Doctor --fix: fenced code blocks preserved byte-exact, rotating backups (.bak.1/.bak.2 — never overwrite), atomic writes (tempfile + os.replace), removes empty headings and stray "PLEASE"
- config: TOML type validation (ConfigError with the exact field path; CLI exits 2)
- Builder: variables(**values) implemented to match the long-standing CHANGELOG promise
- Housekeeping: removed an uninstallable dependency pin from requirements.txt; removed uv.lock (library-lock policy; regenerate with uv sync if wanted); README/GitHub metadata corrected (19 patterns / 290 prompts)

### Fixed
- phi-3 prompt set removed — byte-identical duplicates of the phi-3.5 content (alias row kept in place)
- Provenance: source frontmatter completed for 8 content-verified Fabric-derived prompts; 160 prompts without a known origin are documented for review instead of silently guessed

## [0.3.0] - 2026-05-01

### Added

- **XDG configuration system** (`config.toml`) -- opt-in configuration via `$XDG_CONFIG_HOME/promptkit/config.toml`
  - `extra_prompt_dirs` and `extra_pattern_dirs` for custom content (absolute paths only)
  - `default_persona` for default persona in `promptkit build`
  - Missing config = old behavior preserved (zero breaking changes)
- **Doctor v2** -- 3 new heuristics + fix capabilities
  - Bigram duplication detection (identifies repeated phrases like "code review ... code review")
  - Context boundary validation (detects empty sections like `Task:` with no content)
  - Ambiguous language detection (`maybe`, `possibly`, `somewhat`)
  - `--fix` flag: applies safe automatic fixes (removes standalone "please", collapses double whitespace, strips trailing whitespace, removes empty boundary lines)
  - `--fix --dry-run`: shows what would be fixed without modifying files
  - `--fix --file FILE.md`: modifies the file in-place, creates `.md.bak` backup
  - `--format json`: machine-readable JSON output
- **Builder v2** -- `string.Template` variable substitution
  - `PromptBuilder().variables(role=..., task=..., ...)` substitutes `$variable` placeholders
  - Uses `safe_substitute` -- undefined variables are left as-is (no KeyError)
  - Fully backward compatible -- no `.variables()` call = old behavior
- **Custom content with source tags** -- `promptkit list` shows `[custom]` / `[built-in]` tags for patterns
- **`tomli` dependency** -- conditional for Python <3.11 (stdlib `tomllib` on 3.11+)

### Changed

- Doctor command: empty prompt text now returns exit code 1 (was system error)
- Pattern registry: respects `extra_pattern_dirs` from config (custom dirs searched first)
- `list_pattern_names` and `list_patterns_with_categories` now include custom patterns

### Fixed

- Doctor `_match_phrase` regex bug (negative lookahead `(?!\w)` was `(!\w)`)
- Doctor `--fix` with `--format json` now outputs single combined JSON (was double output)
- Pattern cache invalidation now graceful (`hasattr` guard on `cache_clear`)
- `pyproject.toml` mypy config: `ignore_missing_imports = true` for ehdoll dependencies

## [0.2.0] - 2026-04-26

### Changed

- **BREAKING:** CLI migrated from argparse to [Typer](https://typer.tiangolo.com/)
  - Commands: `promptkit build`, `promptkit list`, `promptkit prompts`, `promptkit search`, `promptkit doctor`
  - Options use `--` prefix (e.g., `--persona`, `--pattern`, `--task`)
  - `promptkit build --interactive` replaces bare `promptkit build`
- **BREAKING:** Patterns are now loaded from `.md` files, not a hard-coded dict
  - `PromptBuilder.PATTERNS` dict removed; use `PromptBuilder().get_available_patterns()` for names
  - Patterns read via `importlib.resources` -- single source of truth
  - 18 patterns across 7 categories (reasoning, agentic, context, output, code, review, defensive)
- CLI monolith (`cli.py`, 719 lines) split into modular package (`cli/commands/`)
- Extracted shared helpers to `llm_promptkit/helpers.py`
- `PromptBuilder.pattern()` validates against registry, raises `PatternNotFoundError` for unknown patterns
- `.format()` calls replaced with `.replace()` to prevent format string injection
- `read_pattern()` cached with `@lru_cache` to avoid redundant I/O
- `except Exception` narrowed to `except (OSError, UnicodeDecodeError)` in search
- Doctor command validates file paths (rejects directories, nonexistent files, path traversal)
- Private constants in `doctor.py` (`_VAGUE_PHRASES`, etc.) -- not exported

### Added

- `patterns/_registry.py` -- pattern loading from packaged `.md` files
- `PromptKitError(Exception)` base exception with `PatternNotFoundError` and `PatternLoadError` subclasses
- `get_pattern_description()` and `list_patterns_with_categories()` in registry
- `llm-promptkit` as alternative CLI entry point (in addition to `promptkit`)
- 10 new pattern `.md` files: tree-of-thought, step-back, decomposition, reflection, react, prompt-chaining, meta-prompting, few-shot-negatives, role-play, json-output
- `PromptBuilder().get_available_patterns()` method (returns tuple of pattern names)
- `search` command with `--category` and `--limit` options
- Token estimation via `--tokens` flag on `build` command

### Removed

- Hard-coded `PATTERNS` dict from `builder.py`
- Duplicate `prompts/` and `patterns/` from repo root (SSOT = `src/llm_promptkit/`)
- Old argparse-based test suite (replaced with Typer CliRunner tests)
- Dead `helpers.get_patterns_dir()` function (delegated to `_registry._resolve_patterns_dir`)
- Module-level docstrings with redundant info (trimmed)

### Fixed

- 130 tests passing (26 builder + 34 CLI + 13 registry + 57 edge cases)
- 92% test coverage
- `mypy` clean (0 errors)
- `ruff check + format` clean
- Wheel includes both prompts (289) and patterns (18) correctly
- CLI branding unified: `promptkit` everywhere
- `examples()` validates keys -- raises `ValueError` on missing `input`/`output`

## [0.1.0] - 2026-03-10

### Added

- Initial release
- PromptBuilder fluent API
- CLI with build, list, prompts, search, doctor commands
- 275+ curated prompts
- 8 pattern templates
- Token estimation (with tiktoken optional dependency)