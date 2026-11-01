# Small mallit (< 10B parametria)

## Models

| Model | Sizes | Strengths |
|-------|------|-----------|
| [Phi 3 / 3.5](phi-3.5/) | 3.8B | Microsoft; yhteinen setti molemmille (phi-3-kopiot poistettu duplikaattina) |
| [Gemma 2](gemma-2/) | 2B, 9B | Google, tehokas |

##  General rules for small models

1. **LYHYET PROMPTIT** (< 200 tokens)
2. **ONE task at a time**
3. **SHOW format** - provide example
4. **YKSINKERTAINEN kieli** - ei monimutkaisia ohjeita
5. **NO deep reasoning** - use a larger model

## When to use a small model?

 **Sopii:**
- Luokittelu
- NER (nimien/paikkojen tunnistus)
- Simple Q&A
- Tekstin muotoilu
- Kielentunnistus

 **Ei sovi:**
- Complex reasoning
- Long code generation
- Luova kirjoitus
- Complex JSON structures
