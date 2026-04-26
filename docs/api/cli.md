# CLI Reference

Command-line interface for LLM Promptkit.

## Commands

### `list`

List all available patterns with categories and descriptions.

```bash
promptkit list
```

---

### `build`

Build a prompt from arguments or interactively.

```bash
promptkit build [OPTIONS]
```

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--persona` | `-p` | AI persona/role |
| `--pattern` | `-P` | Pattern slug to use (repeatable) |
| `--task` | `-t` | Task description |
| `--context` | `-c` | Context text |
| `--constraint` | | Constraint (repeatable) |
| `--output` | `-o` | Save to file |
| `--tokens` | | Show token estimate |
| `--interactive` | `-i` | Interactive mode |

**Examples:**

```bash
# Simple prompt
promptkit build -t "Explain recursion"

# With persona and pattern
promptkit build \
    -p "Senior Developer" \
    -P chain-of-thought \
    -t "Review this code" \
    -c "def foo(): pass"

# Multiple patterns
promptkit build \
    -P chain-of-thought \
    -P reflection \
    -t "Solve this problem"

# With constraints
promptkit build \
    -t "Write a poem about AI" \
    --constraint "Max 4 lines" \
    --constraint "Must rhyme"

# With token count
promptkit build -t "Write a story" --tokens

# Save to file
promptkit build -t "Write docs" -o prompt.txt
```

---

### `doctor`

Analyze a prompt for common issues. No API calls required.

```bash
promptkit doctor "Make it good please"
promptkit doctor my-prompt.md
promptkit doctor --file my-prompt.md
```

**Checks:**
- Vague/ambiguous instructions
- Missing role/persona
- Token inefficiency (verbose phrasing)
- Missing output format
- Lack of examples (few-shot)
- Negative constraints ("don't" → use positive)
- Structural formatting
- Code block handling

---

### `search`

Search prompts by content and category.

```bash
promptkit search "json"
promptkit search "code review" --category reasoning
promptkit search "debug" --limit 5
```

**Options:**

| Option | Description |
|--------|-------------|
| `--category` | Filter by category |
| `--limit` | Maximum number of results |

---

### `prompts`

Browse included model-optimized prompts.

```bash
promptkit prompts                              # List all providers
promptkit prompts --model openai               # List models for provider
promptkit prompts --model openai/gpt-4o        # List prompts for model
promptkit prompts --show openai/gpt-4o/coding  # View prompt content
```