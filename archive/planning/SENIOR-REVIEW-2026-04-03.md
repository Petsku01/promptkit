# Senior Engineering Review - promptkit

Date: 2026-04-03
Reviewer mode: OBSERVE -> ISOLATE -> FIX + VERIFY

## 1. Reality Check

### What actually works
- Core `PromptBuilder` API works for basic composition and chaining.
- CLI commands `list`, `build`, `prompts`, `search`, and `doctor` execute in the repo environment.
- Test suite passes locally in the project venv.

Verification evidence:
- `.venv/bin/pytest -q` -> `104 passed in 0.50s`
- `.venv/bin/python -m llm_promptkit.cli --help` shows all 5 subcommands
- `.venv/bin/promptkit build --persona ... --pattern chain-of-thought --task ... --tokens` generates expected output

### What is claimed but not reliably true
- Claim: installed package includes broad prompt browsing/search experience.
- Reality: distribution artifacts do **not** include `prompts/` or `patterns/` content.
  - `dist/llm_promptkit-0.1.0-py3-none-any.whl` contains only Python package files.
  - `dist/llm_promptkit-0.1.0.tar.gz` likewise omits prompt data directories.
  - `get_prompts_dir()` assumes a repo-like layout and points to `Path(__file__).parent.parent.parent / "prompts"` (`src/llm_promptkit/cli.py:44-55`). That path is wrong for wheel installs.
- Claim drift in docs:
  - README import example uses wrong module in one section: `from promptkit import PromptBuilder` (`README.md:125`). Actual package import is `from llm_promptkit import PromptBuilder`.
  - Installation docs claim "No required dependencies (just stdlib)" (`docs/getting-started/installation.md:28`), but `pyproject.toml` requires `rich>=13.0` (`pyproject.toml:30`).
  - CLI branding is inconsistent: runtime parser program is `prompt-patterns` (`src/llm_promptkit/cli.py:661`), while docs use `llm-promptkit` and README often uses `promptkit`.

Bottom line reality: repo-clone workflow works; packaged/distributed workflow is incomplete and misleading.

## 2. Code Quality

### Strengths
- `PromptBuilder` implementation is small and readable.
- CLI behavior is mostly deterministic and covered by tests.
- Error handling exists for missing prompt files and invalid selections.

### Quality problems
- Monolithic CLI file (`src/llm_promptkit/cli.py`, ~700 lines) mixes unrelated concerns: argument parsing, prompt browsing, search, clipboard integration, and doctor heuristics.
- Strong drift between "patterns" docs and executable builder patterns:
  - Builder has 13 hardcoded patterns.
  - `patterns/` directory has 8 files and a different taxonomy.
  - This creates two sources of truth and guaranteed entropy.
- Test suite has high coverage but uneven assertion quality:
  - Multiple tests only assert that `console.print` was called (e.g. `tests/test_cli.py:140-147`, `tests/test_cli.py:579-594`).
  - `tests/test_cli_doctor_edge_cases.py` mainly prints mock calls with no assertions (`tests/test_cli_doctor_edge_cases.py:11-48`).
  - Result: coverage inflates confidence without validating meaningful outcomes.
- Dead/maintenance-risk scripts at repo root:
  - `patch_doctor.py` and `refactor_doctor.py` are one-off mutation scripts with hardcoded absolute paths (`patch_doctor.py:4`, `refactor_doctor.py:3`) and no integration in build/test flow.

## 3. Architecture Issues

1. Packaging architecture is broken for product promises.
- Core CLI features (`prompts`, `search`, `prompts --show`) depend on non-packaged content trees.
- Package metadata only discovers `src` Python packages (`pyproject.toml:52-53`), with no package-data strategy.

2. Content architecture has no single canonical source.
- `PromptBuilder.PATTERNS` is hardcoded in code.
- Large markdown prompt libraries live separately under `prompts/` and `patterns/`.
- No synchronization mechanism, validation pass, or generated index binding them.

3. Product identity is fragmented.
- `prompt-patterns` (argparse prog), `llm-promptkit` (package/script), and `promptkit` (alias/docs) coexist with no clear canonical command.
- This is small technically, but high-friction for users and docs maintenance.

## 4. Priority Fixes (Ranked)

### P0 - Must fix before recommending install/use
1. Ship prompt assets in the distributable package.
- Add package-data configuration for `prompts/**` and any required metadata.
- Refactor `get_prompts_dir()` to resolve package resources robustly (e.g., `importlib.resources`) instead of filesystem assumptions.
- Add an integration test that installs built wheel in isolated env and verifies `promptkit prompts` and `promptkit search` work outside repo root.

2. Repair documentation truthfulness.
- Fix incorrect import (`README.md:125`).
- Fix dependency statement in installation docs.
- Choose one canonical command name and standardize all docs/help text.

### P1 - High value, medium urgency
3. Split `cli.py` into modules by responsibility.
- Suggested split: `commands/build.py`, `commands/doctor.py`, `commands/prompts.py`, `commands/search.py`, `app.py` (parser wiring).
- Keeps each command testable without heavy mocking and reduces regression risk.

4. Replace weak tests with behavior assertions.
- Remove print-only tests.
- Assert table rows/messages/content, not merely method calls.
- Add negative-path tests for installed-package asset resolution.

5. Establish one source of truth for patterns.
- Either generate `PromptBuilder.PATTERNS` from canonical markdown metadata, or clearly scope builder patterns as a separate API contract and validate docs against it in CI.

### P2 - Cleanup / maintainability
6. Remove or quarantine ad-hoc surgery scripts (`patch_doctor.py`, `refactor_doctor.py`) into a `tools/` folder with explicit "manual/internal" labeling, or delete.
7. Add lint/type gates to CI if absent (`ruff`, optional `mypy`) and enforce doc checks for command/import consistency.

## 5. Verdict

**Fix first. Do not call this "ready" for general install/distribution yet.**

Reason:
- The project works in-repo for developers, but the packaged product undermines core advertised features because required content is not shipped.
- Documentation has factual contradictions that will produce user failure and support churn.
- Test pass rate is real but overstates confidence in user-visible behavior.

This is salvageable quickly with a packaging + docs truth pass (P0). After that, modularization and test quality upgrades (P1) can make it robust.
