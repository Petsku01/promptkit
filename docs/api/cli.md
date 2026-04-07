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
┃ Pattern           ┃ Preview                                       ┃
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

### `doctor`

Analyze a prompt for common issues.

```bash
promptkit doctor [TEXT]
promptkit doctor --file PATH
```

**Options:**

| Option | Short | Description |
|--------|-------|-------------|
| `--file` | `-f` | Read prompt from file |

**Examples:**

```bash
# Analyze inline text
promptkit doctor "Make it good please"

# Analyze from file
promptkit doctor --file my-prompt.md
```

**Checks performed:**

- Vague/ambiguous instructions
- Missing role/persona
- Token inefficiency (verbose phrasing)
- Missing output format
- Lack of examples
- Negative constraints
- Structural formatting for long prompts
- Code block awareness
