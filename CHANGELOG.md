# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-26

### Changed

- **BREAKING:** CLI migrated from argparse to [Typer](https://typer.tiangolo.com/)
  - Commands: `promptkit build`, `promptkit list`, `promptkit prompts`, `promptkit search`, `promptkit doctor`
  - Options use `--` prefix (e.g., `--persona`, `--pattern`, `--task`)
  - `promptkit build --interactive` replaces bare `promptkit build`
- **BREAKING:** Patterns are now loaded from `.md` files, not a hard-coded dict
  - `PromptBuilder.PATTERNS` dict removed; use `PromptBuilder.AVAILABLE_PATTERNS` for names
  - Patterns read via `importlib.resources` — single source of truth
  - 18 patterns across 7 categories (reasoning, agentic, context, output, code, review, defensive)
- CLI monolith (`cli.py`, 719 lines) split into modular package (`cli/commands/`)
- Extracted shared helpers to `llm_promptkit/helpers.py`
- Version bumped from 0.1.0 to 0.2.0.dev0
- Classifier updated from Alpha to Beta

### Added

- `patterns/_registry.py` — pattern loading from packaged `.md` files
- `llm-promptkit` as alternative CLI entry point (in addition to `promptkit`)
- 10 new pattern `.md` files that were only in the dict: tree-of-thought, step-back, decomposition, reflection, react, prompt-chaining, meta-prompting, few-shot, role-play, json-output

### Removed

- Hard-coded `PATTERNS` dict from `builder.py`
- Duplicate `prompts/` and `patterns/` from repo root (SSOT = `src/llm_promptkit/`)
- Old argparse-based test suite (replaced with Typer CliRunner tests)

### Fixed

- All 70 tests passing (26 builder + 34 CLI + 10 registry)
- Wheel includes both prompts (275) and patterns (18) correctly
- CLI branding unified: `promptkit` everywhere (was: promptkit/llm-promptkit/prompt-patterns)

## [0.1.0] - 2026-03-10

### Added

- Initial release
- PromptBuilder fluent API
- CLI with build, list, prompts, search, doctor commands
- 275+ curated prompts
- 8 pattern templates
- Token estimation (with tiktoken optional dependency)