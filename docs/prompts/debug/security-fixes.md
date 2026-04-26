[← Back to Debug Prompts](../index.md)

# security fixes

**Category:** debug
**Source:** prompts.chat (contributor: @abhinavme1004@gmail.com)

## When to Use

Use this prompt when you need an AI to act as a security fixes.

## The Prompt

```
---
name: security-fixes
description: in order to fix security issues in my codebase which is flagged by code scanning for refrences like user input comping as part o request could be vulnerable and how can we fix it
---

# security fixes

it should identify the issue and fix  it with respect to current project checking it should not break the existing functionality and a proper test case should be written for the change

## Instructions

check the issue 
fix it 
test case
- Step 2: ...
```

## Variables

Replace placeholder text in curly braces or quotes with your specific content.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Works well |
| Claude | Yes | Works well |
| Llama 3 | Yes | Works well |
