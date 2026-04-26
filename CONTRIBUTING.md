# Contributing to LLM Promptkit

Thanks for contributing! This guide will help you add new patterns and improve existing ones.

## Adding a New Pattern

1. **Use the template:** Copy `templates/pattern-template.md`
2. **Place in correct category directory** under `src/llm_promptkit/patterns/`:
   - `reasoning/` — Logic, step-by-step, self-correction
   - `agentic/` — ReAct, prompt chaining, meta-prompting
   - `context/` — Few-shot, role-play, long-context
   - `output/` — JSON, structured lists, extraction
   - `code/` — Generation, refactoring, debugging
   - `review/` — Code review, security, performance
   - `defensive/` — Hallucination reduction, constraints
3. **Follow the naming convention:** Use kebab-case (e.g., `chain-of-thought.md`)
4. **Test on multiple models:** At minimum GPT-4 and Claude
5. **Include real examples:** Show actual input/output
6. **Update the README:** Add to the pattern directory table

## Pattern Quality Checklist

- [ ] Clear "When to Use" section
- [ ] Explanation of WHY it works (not just WHAT)
- [ ] Copy-pasteable prompt template
- [ ] Concrete example with real output
- [ ] Tested on 2+ models
- [ ] Common mistakes documented
- [ ] Related patterns linked

## What Makes a Good Pattern?

Yes **Practical** — Solves a real problem developers have
Yes **Tested** — Actually verified on multiple models
Yes **Documented** — Explains the mechanics, not just the prompt
Yes **Copyable** — Ready to paste and use immediately

No: Theoretical patterns without real testing
No: Single-model tricks that don't generalize
No: Vague prompts without concrete examples

## Updating Existing Patterns

- Add new model test results
- Improve examples
- Add variations
- Fix common mistakes

## Style Guide

- Use plain English
- Show, don't tell (examples > explanations)
- Be specific (bad: "it works well", good: "returns valid JSON 95% of the time")
- Include failure modes (when does this NOT work?)

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ --cov=llm_promptkit --cov-report=term-missing

# Lint
ruff check src/ tests/
ruff format src/ tests/
```

## Questions?

Open an issue or reach out to [@Petsku01](https://github.com/Petsku01).