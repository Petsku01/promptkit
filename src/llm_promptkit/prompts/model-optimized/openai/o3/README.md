# o3

## Model Characteristics
- **Type:** Reasoning model (thinks internally before responding)
- **Context:** 200K tokens
- **Strengths:** Mathematics, code, logic, science, complex multi-step reasoning
- **Best for:** Hard problems requiring deep deliberation

---

## CRITICAL: How o3 Works Differently

o3 thinks **internally** before responding. It does deep reasoning on its own.

**DON'T** say:
- "Think step by step"
- "Show your reasoning"
- "Let's work through this"

**DO** say:
- State the problem directly
- Be clear about what you want
- Specify output format if needed
- Provide constraints and requirements upfront

---

## Prompts by theme

| Theme | File | Description |
|-------|------|-------------|
| Reasoning | [reasoning.md](reasoning.md) | Math, logic, analysis |
| Coding | [coding.md](coding.md) | Complex code problems |

## When to Use o3 vs GPT-4.1

| Task | Best Model |
|------|------------|
| Complex math proofs | o3 |
| Competitive programming | o3 |
| Deep logic / reasoning chains | o3 |
| PhD-level science | o3 |
| Subtle debugging (heisenbugs) | o3 |
| General coding & tasks | GPT-4.1 |
| Creative writing | GPT-4.1 |
| Speed-critical tasks | GPT-4.1 |
| Cost-sensitive bulk tasks | GPT-4.1 |

## Key Tips

- **Don't prompt for reasoning** — it's automatic and internal
- **Be direct** — just state what you want
- **Harder = better** — o3 shines on difficult problems
- **Simpler prompts** — less instruction, more problem
- **o3-mini** exists for medium-difficulty reasoning at lower cost