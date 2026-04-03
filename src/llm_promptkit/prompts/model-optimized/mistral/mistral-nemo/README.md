# Mistral Nemo

## Characteristics
- **Size:** 12B parameters
- **Context:** 128K tokens
- **Strengths:** Long context, multilingual, efficient

## Key Features

- Apache 2.0 license (open)
- Trained with Nvidia
- Drop-in replacement for Mistral 7B
- Better instruction following

## Prompt Style

Works well with direct, simple prompts:

```
[Task description]

[Input/context]

[Output format]
```

## Use Cases

- Long document analysis
- Multilingual tasks
- Summarization
- Q&A over large contexts

## Example Prompts

### Summarization

```
Summarize this document in 3 bullet points:

[long document]
```

### Analysis

```
Analyze the key themes in this text:

[text]

List themes with supporting quotes.
```

### Translation

```
Translate to [language]:

[text]
```
