# CLI Reference

Command-line interface for LLM Promptkit.

## Commands

### `list`

List all available patterns.

```bash
llm-promptkit list
```

Output:
```
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Pattern           ┃ Description                                   ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ chain-of-thought  │ Think through this step-by-step...           │
│ few-shot          │ Here are some examples...                     │
│ json-output       │ Return ONLY valid JSON...                     │
│ ...               │ ...                                           │
└───────────────────┴───────────────────────────────────────────────┘
```

---

### `build`

Build a prompt from arguments.

```bash
llm-promptkit build [OPTIONS]
```

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--persona` | `-p` | AI persona/role |
| `--pattern` | `-P` | Pattern to use (repeatable) |
| `--task` | `-t` | Task description |
| `--context` | `-c` | Context text |
| `--constraint` | | Constraint (repeatable) |
| `--output` | `-o` | Save to file |
| `--tokens` | | Show token estimate |
| `--interactive` | `-i` | Interactive mode |

**Examples:**

```bash
# Simple prompt
llm-promptkit build -t "Explain recursion"

# With persona and pattern
llm-promptkit build \
    -p "Senior Developer" \
    -P chain-of-thought \
    -t "Review this code" \
    -c "def foo(): pass"

# Multiple patterns
llm-promptkit build \
    -P chain-of-thought \
    -P reflection \
    -t "Solve this problem"

# With token count
llm-promptkit build -t "Write a story" --tokens

# Save to file
llm-promptkit build -t "Write docs" -o prompt.txt
```

---

### Interactive Mode

```bash
llm-promptkit build --interactive
```

Guides you through building a prompt step-by-step:

1. Enter persona (optional)
2. Select patterns
3. Enter task
4. Add context (optional)
5. Preview and copy
