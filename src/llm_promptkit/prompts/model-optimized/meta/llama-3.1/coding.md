# Llama 3.1: Coding

> **Model Sizes**: 8B, 70B, 405B
> **Best for coding**: 70B+ (8B limited for complex tasks)

## Code Generation

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a skilled programmer. Write clean, working code.
<|eot_id|><|start_header_id|>user<|end_header_id|>

Write a [language] function that [description].

Requirements:
- Include comments
- Handle errors
- Add type hints
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## Simple Format (Works Too)

```
Write Python code for: [task]

Include:
- Type hints
- Docstring
- Error handling
- Example usage
```

## Code Review

```
Review this code:

```[language]
[code]
```

Check for:
1. Bugs and logic errors
2. Security issues
3. Performance problems
4. Style/readability

For each issue:
- Line: [number]
- Problem: [description]
- Fix: [solution]
```

## Debugging

```
Error: [error message]

Code:
```[language]
[code]
```

Explain:
1. What the error means
2. Why it's happening
3. How to fix it (show code)
```

## Algorithm Implementation

```
Implement [algorithm name] in [language].

Requirements:
- Time complexity: O([target])
- Space complexity: O([target])
- Include comments explaining the logic
- Add test cases

Show your reasoning before coding.
```

## Code Explanation

```
Explain this code step by step:

```[language]
[code]
```

For each section:
- What it does
- Why it's written this way
- Any potential issues
```

## Llama 3.1 Specific Tips

 **DO:**
- Use clear, direct instructions
- Ask for reasoning before code (improves quality)
- Specify language explicitly
- Request comments/docs

 **DON'T:**
- Expect 8B to handle complex multi-file projects
- Use overly complex nested instructions
- Assume it knows your codebase context
