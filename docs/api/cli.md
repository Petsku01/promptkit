# CLI Reference

Command-line interface for LLM Promptkit.

## Commands

### `list`

List all available patterns.

```bash
promptkit list
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
promptkit build [OPTIONS]
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

# With token count
promptkit build -t "Write a story" --tokens

# Save to file
promptkit build -t "Write docs" -o prompt.txt
```

---

### Interactive Mode

```bash
promptkit build --interactive
```

Guides you through building a prompt step-by-step:

1. Enter persona (optional)
2. Select patterns
3. Enter task
4. Add context (optional)
5. Preview and copy
