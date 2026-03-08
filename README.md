# 🛠️ Prompt Patterns

A curated collection of practical, copy-pasteable prompt patterns for developers. No fluff, no "Awesome lists"—just prompts that work.

## How to Use

1. Find your use case in the table below
2. Copy the template block
3. Replace `[VARIABLES]` with your context
4. Paste into your LLM of choice

## Pattern Directory

| Category | Pattern | Use When You Need To... |
|----------|---------|-------------------------|
| **Reasoning** | [Chain-of-Thought](patterns/reasoning/chain-of-thought.md) | Get step-by-step logical reasoning |
| **Reasoning** | [Self-Consistency](patterns/reasoning/self-consistency.md) | Verify answers through multiple paths |
| **Output** | [JSON Enforcer](patterns/output/json-enforcer.md) | Get clean, valid JSON output |
| **Code** | [TDD Prompting](patterns/code/tdd-prompting.md) | Generate tests first, then implementation |
| **Code** | [Stack Trace Decoder](patterns/code/stack-trace-decoder.md) | Debug errors from stack traces |
| **Review** | [Senior Reviewer](patterns/review/senior-reviewer.md) | Get strict code review feedback |
| **Context** | [Few-Shot with Negatives](patterns/context/few-shot-negatives.md) | Teach by example (including what NOT to do) |
| **Defensive** | [Hallucination Reducer](patterns/defensive/hallucination-reducer.md) | Reduce confident nonsense |

## Anatomy of a Pattern

Each pattern follows this format:

```markdown
# Pattern Name

## When to Use
The specific scenario where this pattern excels.

## How It Works
The underlying mechanics of WHY the LLM responds well to this.

## The Prompt
\```
[The actual prompt template]
\```

## Example
**Input:** [What you provide]
**Output:** [What you get back]

## Tested On
- GPT-4: ✅ Works well
- Claude: ✅ Works well  
- Llama 3: ⚠️ Needs adjustment
```

## Categories

- **reasoning/** — Logic, step-by-step, self-correction
- **output/** — JSON, structured lists, schema extraction
- **code/** — Generation, refactoring, debugging
- **review/** — Code review, security, performance
- **context/** — RAG, few-shot, long-context management
- **defensive/** — Hallucination reduction, constraint enforcement

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

*Built with 🌙 by [Petsku](https://github.com/Petsku01)*
