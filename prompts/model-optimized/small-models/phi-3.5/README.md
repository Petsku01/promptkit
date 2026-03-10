# Phi 3.5 (Microsoft)

## Ominaisuudet
- **Koko:** 3.8B parametria
- **Konteksti:** 128K tokens
- **Strengths:** Reasoning, koodi, matematiikka

## Prompts

| Teema | File |
|-------|----------|
| Perus | [basic.md](basic.md) |
| Koodi | [coding.md](coding.md) |

## Erikoisuudet

- Surprisingly good reasoning for its size
- Good at math
- 128K context enables long documents
- Vision-variantti kuville

## Esimerkkipromptit

### Reasoning
```
Think step by step:
1. [step]
2. [step]
Answer:
```

### Math
```
Solve: [problem]
Show work.
```

### Code
```
Write [language] function for [task].
Keep it simple.
```
