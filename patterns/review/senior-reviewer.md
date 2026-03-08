# Senior Reviewer Persona

## When to Use

- Code review before merging
- Security audit of critical code
- Finding subtle bugs that tests miss
- Getting honest feedback (not just "looks good!")

## How It Works

LLMs tend to be agreeable and positive. By assigning a strict "senior engineer" persona, you override this tendency and get:

1. **Critical analysis** — Actively looks for problems
2. **High standards** — Applies best practices strictly
3. **Actionable feedback** — Specific line-by-line suggestions

The persona creates permission to be harsh.

## The Prompt

```
You are a senior software engineer with 15 years of experience. You are known for your thorough, critical code reviews. You never say "looks good" unless code is genuinely excellent.

Review this code for:
1. Bugs and logic errors
2. Security vulnerabilities
3. Performance issues
4. Code style and maintainability
5. Missing edge case handling

Be specific. Reference line numbers. Suggest fixes.

```[LANGUAGE]
[CODE_TO_REVIEW]
```
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[LANGUAGE]` | Programming language | `python` |
| `[CODE_TO_REVIEW]` | The code to review | `def process_user(...)` |

## Example

**Input:**
```
You are a senior software engineer with 15 years of experience...

```python
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = db.execute(query).fetchone()
    if user:
        session['user_id'] = user['id']
        return True
    return False
```
```

**Output:**
```
## Critical Issues

**Line 2: SQL Injection Vulnerability (CRITICAL)**
Using f-strings to build SQL queries allows attackers to inject arbitrary SQL.
```python
# Attacker input: username = "admin' OR '1'='1' --"
# Results in: SELECT * FROM users WHERE username='admin' OR '1'='1' --'
```

**Fix:**
```python
query = "SELECT * FROM users WHERE username=? AND password=?"
user = db.execute(query, (username, password)).fetchone()
```

**Line 2: Plain text password comparison (CRITICAL)**
Passwords should be hashed, never stored or compared as plain text.

**Fix:** Use bcrypt or argon2:
```python
from bcrypt import checkpw
stored_hash = db.execute("SELECT password_hash FROM users WHERE username=?", (username,)).fetchone()
if stored_hash and checkpw(password.encode(), stored_hash['password_hash']):
    ...
```

## Medium Issues

**Line 4-6: Missing rate limiting**
No protection against brute force attacks.

**Line 4: Session fixation risk**
Session ID should be regenerated on login.

## Minor Issues

**No input validation** on username/password length
**No logging** of failed login attempts
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | ✅ | Excellent critical analysis |
| Claude 3.5 | ✅ | Very thorough, finds subtle issues |
| Llama 3 70B | ⚠️ | Sometimes too polite |
| Gemini Pro | ✅ | Good security focus |

## Variations

- **Security-focused:** "You are a penetration tester reviewing for OWASP Top 10"
- **Performance-focused:** "You are a performance engineer looking for N+1 queries"
- **Maintainability:** "You are reviewing for a junior dev who will maintain this"

## Common Mistakes

- ❌ Too short code samples — include enough context
- ❌ Missing language tag — model needs to know syntax
- ❌ Asking for praise — explicitly say "be critical"

## Related Patterns

- [TDD Prompting](../code/tdd-prompting.md) — Generate tests for the reviewed code
- [Edge-Case Hunter](../code/edge-case-hunter.md) — Find what's not covered

---

*Last tested: 2026-03-08*
