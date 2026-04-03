# Qwen 3.5 (Pieni malli)

## Features
- **Sizes:** 0.6B, 1.7B, 4B, 8B, 14B, 32B
- **Context:** 32K tokens
- **Strengths:** Fast, edge use, cost-effective

## Prompts by theme

| Theme | File |
|-------|----------|
| Perus | [basic.md](basic.md) |
| Coding | [coding.md](coding.md) |
| JSON | [json-output.md](json-output.md) |

##  Small model rules

1. **LYHYET promptit** - alle 200 tokens
2. **ONE task at a time**
3. **Clear format** - show example output
4. **No complex reasoning** - use a larger model

## Kokosuositukset

| Koko | Sopii | Ei sovi |
|------|-------|---------|
| 0.6B-1.7B | Classification, NER, simple | Code, reasoning |
| 4B-8B | Peruskoodaus, yhteenveto | Complex analyysi |
| 14B+ | Most tasks | - |
