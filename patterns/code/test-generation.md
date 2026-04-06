# Test Generation Pattern

## Description

Generate comprehensive unit tests covering happy path, edge cases, and error scenarios.

## When to use

Critical code paths, complex logic, or where bugs would be expensive.

## When to avoid

Simple functions where tests are obvious or time is critical.

## Template

```
Write unit tests for this code:

```
[CODE_TO_TEST]
```

Cover these scenarios:
1. Happy path: [Normal input]
2. Edge case: [Boundary conditions]
3. Error case: [Invalid inputs]
4. [Additional cases as needed]

For each test:
- Name: descriptive test name
- Input: specific test input
- Expected: expected behavior
- Assert: what to verify

```

## Example

```
Write unit tests for this code:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Cover these scenarios:
1. Happy path: divide(10, 2) == 5.0
2. Edge case: divide(5, 0) raises ValueError
3. Error case: divide("a", 1) raises TypeError
4. Performance: large numbers, negative numbers

For each test:
- Name: test_divide_normal
- Input: a=10, b=2
- Expected: 5.0
- Assert: result is float

- Name: test_divide_by_zero
- Input: a=5, b=0
- Expected: ValueError raised
- Assert: exception type

- Name: test_invalid_input
- Input: a="invalid", b=1
- Expected: TypeError raised
- Assert: exception type

- Name: test_large_numbers
- Input: a=10**18, b=10**18
- Expected: correct float result
- Assert: result == 10**18 / 10**18

## Tags

testing, unit-tests, edge-cases, pytest
