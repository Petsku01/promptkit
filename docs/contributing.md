# Contributing

We welcome contributions! Here's how to help.

## Development Setup

```bash
git clone https://github.com/Petsku01/promptkit.git
cd promptkit
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest -v
```

## Code Style

We use `ruff` for linting:

```bash
ruff check src/ tests/
ruff check --fix src/ tests/  # Auto-fix
```

## Adding a Pattern

1. Add to `PromptBuilder.PATTERNS` in `src/llm_promptkit/builder.py`
2. Add tests in `tests/test_builder.py`
3. Document in `docs/patterns/`
4. Submit PR

## Documentation

Build docs locally:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
# Visit http://localhost:8000
```

## Pull Request Guidelines

- One feature per PR
- Include tests
- Update docs if needed
- Follow existing code style

## Questions?

Open an issue on [GitHub](https://github.com/Petsku01/promptkit/issues).
