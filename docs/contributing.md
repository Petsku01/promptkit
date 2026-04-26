# Contributing

We welcome contributions! Here's how to help.

## Development Setup

```bash
git clone https://github.com/Petsku01/promptkit.git
cd promptkit
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ --cov=llm_promptkit --cov-report=term-missing

# Lint
ruff check src/ tests/
ruff format src/ tests/

# Type check
mypy src/llm_promptkit
```

## Adding a Pattern

Patterns are `.md` files in `src/llm_promptkit/patterns/<category>/`.

1. **Copy the template:** `templates/pattern-template.md`
2. **Place in the correct category directory:**
   - `reasoning/` — Logic, step-by-step, self-correction
   - `agentic/` — ReAct, prompt chaining, meta-prompting
   - `context/` — Few-shot, role-play, long-context
   - `output/` — JSON, structured lists, extraction
   - `code/` — Generation, refactoring, debugging
   - `review/` — Code review, security, performance
   - `defensive/` — Hallucination reduction, constraints
3. **Use kebab-case naming:** e.g., `chain-of-thought.md`
4. **Add tests** in `tests/`
5. **Update README.md** pattern table
6. **Submit PR**

## Code Style

We use `ruff` for linting and formatting:

```bash
ruff check src/ tests/
ruff format src/ tests/
```

## Pull Request Guidelines

- One feature per PR
- Include tests
- Update docs if needed
- Follow existing code style

## Questions?

Open an issue on [GitHub](https://github.com/Petsku01/promptkit/issues).