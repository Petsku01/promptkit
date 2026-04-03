# Rubber Duck Debugging

**Category:** debug
**Source:** Classic technique

## When to Use

When you are completely stuck on a bug and don't even know what's wrong.

## The Prompt

```
I have a bug in my code, but I don't want you to write the solution yet. 

Act as a senior mentor. I will describe the symptoms of the bug and provide the code. 
Ask me one diagnostic question at a time to help me narrow down the issue myself. 

Do not give me the answer outright.

[Insert context]
```

## How It Works

Interactive debugging forces you to think through the problem while the LLM acts as a sounding board, often leading to better understanding than just copy-pasting a fix.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Great at Socratic method |
| Claude | Yes | Excellent |
| Llama 3 | Yes | Good |
