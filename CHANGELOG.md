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
  - `PromptBuilder.PATTERNS` dict removed; use `PromptBuilder().get_available_patterns()` for names
  - Patterns read via `importlib.resources` — single source of truth
  - 18 patterns across 7 categories (reasoning, agentic, context, output, code, review, defensive)
- CLI monolith (`cli.py`, 719 lines) split into modular package (`cli/commands/`)
- Extracted shared helpers to `llm_promptkit/helpers.py`
- `PromptBuilder.pattern()` validates against registry, raises `PatternNotFoundError` for unknown patterns
- `.format()` calls replaced with `.replace()` to prevent format string injection
- `read_pattern()` cached with `@lru_cache` to avoid redundant I/O
- `except Exception` narrowed to `except (OSError, UnicodeDecodeError)` in search
- Doctor command validates file paths (rejects directories, nonexistent files, path traversal)
- Private constants in `doctor.py` (`_VAGUE_PHRASES`, etc.) — not exported

### Added

- `patterns/_registry.py` — pattern loading from packaged `.md` files
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
- `examples()` validates keys — raises `ValueError` on missing `input`/`output`

## [0.1.0] - 2026-03-10

### Added

- Initial release
- PromptBuilder fluent API
- CLI with build, list, prompts, search, doctor commands
- 275+ curated prompts
- 8 pattern templates
- Token estimation (with tiktoken optional dependency)