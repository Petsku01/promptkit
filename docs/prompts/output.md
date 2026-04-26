# Output Prompts

Prompts for controlling output format, structure, and presentation.

## Browsing Prompts

```bash
promptkit search "output"
promptkit search "format"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| diagram-generator | Diagram and chart creation |
| excel-sheet | Spreadsheet formatting |
| journalist | News-style writing |
| cyber-security-specialist | Cybersecurity analysis |
| ai-agent-security-evaluation | AI security evaluation |
| csv-converter | CSV and tabular formatting |
| json-formatter | JSON output formatting |
| markdown-formatter | Markdown output formatting |
| report-writer | Structured report generation |
| summary-generator | Summarization |
| table-generator | Table formatting |
| mermaid-diagram-creator | Generate Mermaid diagram code |
| flashcard-generator | Convert content to study flashcards |
| meeting-minutes-transcriber | Structure meeting notes |

## Built-in Patterns

The `json-output` and `json-enforcer` patterns provide structured output control:

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("json-output")
builder.output_format("json", schema={"answer": "str", "confidence": "float"})
builder.task("Analyze this text")
prompt = builder.build()
```