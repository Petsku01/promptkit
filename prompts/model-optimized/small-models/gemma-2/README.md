# Gemma 2 (Google)

## Ominaisuudet
- **Koot:** 2B, 9B, 27B
- **Konteksti:** 8K tokenia
- **Vahvuudet:** Tehokas, hyvä hinta-laatu

## Promptit

Käytä samoja lyhyitä prompteja kuin Phi:
- [../phi-3.5/basic.md](../phi-3.5/basic.md)
- [../phi-3.5/coding.md](../phi-3.5/coding.md)

## Esimerkkejä

### Classification
```
Classify as positive/negative/neutral:
[text]
Answer:
```

### Summary
```
Summarize in 1-2 sentences:
[text]
Summary:
```

### QA
```
Q: [question]
Context: [context]
A:
```

## Huomioita

- 2B hyvin rajoitettu - vain yksinkertaisimmat tehtävät
- 9B hyvä yleismalli
- 27B lähestyy keskikokoisten mallien tasoa
- Lyhyt konteksti (8K) - ei pitkiä dokumentteja
