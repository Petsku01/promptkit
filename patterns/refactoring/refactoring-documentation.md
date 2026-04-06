# Refactoring Documentation Pattern

## Description

Document code changes with before/after comparison and rationale.

## When to use

Code reviews, handoffs, or maintaining documentation over time.

## When to avoid

Rapid iterations where documentation overhead slows down development.

## Template

```
Document this refactoring:

**Before:**
```
[OLD_CODE]
```

**After:**
```
[NEW_CODE]
```

**What changed**:
1. [Change 1 with rationale]
2. [Change 2 with rationale]
3. [Change 3 with rationale]

**Impact**:
- [Impact 1]
- [Impact 2]
- [Impact 3]

**Migration notes:** [Notes for existing users]
```

## Example

```
Document this refactoring:

**Before:**
```python
def get_data():
    data = fetch_from_db()
    processed = []
    for item in data:
        processed.append(transform(item))
    return processed
```

**After:**
```python
def get_data():
    return [transform(item) for item in fetch_from_db()]
```

**What changed**:
1. Replaced manual loop with list comprehension (readability)
2. Added inline comment explaining transform logic (maintainability)

**Impact:**
- 40% faster on large datasets
- Simpler to maintain

**Migration notes:** Existing callers see no change in behavior
```

## Tags

documentation, refactoring, migration, changelog
