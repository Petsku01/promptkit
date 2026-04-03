# Stack Trace Decoder

## When to Use

- Debugging production errors from logs
- Understanding unfamiliar error messages
- When you have a stack trace but no idea where to start
- Teaching juniors how to read error output

## How It Works

Stack traces contain structured information that can be systematically decoded: the error type, the call chain, the failing line, and surrounding context. By prompting the model to analyze each layer, you get actionable debugging steps rather than generic advice.

The key insight: **work from the error backwards through the call stack, not the other way around.**

## The Prompt

```
Analyze this stack trace and help me debug it.

```
[STACK_TRACE]
```

Follow this process:
1. Identify the error type and message
2. Find the root cause line (usually the last line in YOUR code, not library code)
3. Trace the call chain that led there
4. Suggest the most likely cause
5. Provide a specific fix or debugging step

Be specific. Don't give generic advice.
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[STACK_TRACE]` | The full error output | Python traceback, JS error, etc. |

## Example

**Input:**
```
Analyze this stack trace and help me debug it.

```
Traceback (most recent call last):
  File "app.py", line 45, in handle_request
    user = get_user(request.user_id)
  File "auth.py", line 23, in get_user
    return db.query(User).filter_by(id=user_id).first()
  File "sqlalchemy/orm/query.py", line 1234, in first
    return self._execute().first()
TypeError: 'NoneType' object is not subscriptable
```

Follow this process:
1. Identify the error type and message
2. Find the root cause line
3. Trace the call chain
4. Suggest the most likely cause
5. Provide a specific fix
```

**Output:**
```
1. Error Type & Message:
   TypeError: 'NoneType' object is not subscriptable
   
2. Root Cause Line:
   auth.py, line 23: return db.query(User).filter_by(id=user_id).first()
   
3. Call Chain:
   app.py:45 (handle_request) 
   -> auth.py:23 (get_user) 
   -> SQLAlchemy internals
   
4. Most Likely Cause:
   The `user_id` being passed to `filter_by()` is None.
   This happens when `request.user_id` is None in app.py:45.
   
5. Specific Fix:
   Add validation before the query:
   
   def get_user(user_id):
       if user_id is None:
           raise ValueError("user_id cannot be None")
       return db.query(User).filter_by(id=user_id).first()
   
   Or check at the call site:
   
   if request.user_id is None:
       return error_response("Missing user ID")
   user = get_user(request.user_id)

Debug step: Add `print(f"user_id={request.user_id}")` before line 45.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent, spots subtle issues |
| Claude 3.5 | Yes | Very thorough analysis |
| Llama 3 70B | Partial | Good but sometimes too generic |
| Gemini Pro | Yes | Good results |

## Variations

- **Multi-language:** Specify "This is a Python/Java/JS stack trace"
- **With context:** Include the relevant source code around the failing line
- **Production mode:** Add "This is from production, suggest safe debugging steps"

## Common Mistakes

- No: Just asking "what's wrong?" without structure
- No: Expecting fixes without the surrounding code
- No: Ignoring library code entirely (sometimes the bug is in how you call it)

## Related Patterns

- [Senior Reviewer](../review/senior-reviewer.md) - For code review, not debugging
- [TDD Prompting](./tdd-prompting.md) - Write tests to prevent future errors

---

*Last tested: 2026-03-10*
