# Clean BibTeX Formatter for Academic Projects

**Category:** output
**Source:** prompts.chat (contributor: @recep)

## When to Use

Use this prompt when you need an AI to act as a clean bibtex formatter for academic projects.

## The Prompt

```
I am preparing a BibTeX file for an academic project.
Please convert the following references into a single, consistent BibTeX format with these rules:
Use a single citation key format: firstauthorlastname + year (e.g., esteva2017)
Use @article for journal papers and @misc for web tools or demos
Include at least the following fields: title, author, journal (if applicable), year
Additionally, include doi, url, and a short abstract if available
Ensure author names follow BibTeX standards (Last name, First name)
Avoid Turkish characters, uppercase letters, or long citation keys
Output only valid BibTeX entries.
```

## Variables

Replace placeholder text in curly braces or quotes with your specific content.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Works well |
| Claude | Yes | Works well |
| Llama 3 | Yes | Works well |
