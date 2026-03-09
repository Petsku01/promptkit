# Pienet mallit (< 10B parametria)

## Mallit

| Malli | Koot | Vahvuudet |
|-------|------|-----------|
| [Phi 3](phi-3/) | 3.8B | Microsoft, reasoning |
| [Phi 3.5](phi-3.5/) | 3.8B | Parannettu, vision |
| [Gemma 2](gemma-2/) | 2B, 9B | Google, tehokas |

##  Yleiset säännöt pienille malleille

1. **LYHYET PROMPTIT** (< 200 tokenia)
2. **YKSI tehtävä kerrallaan**
3. **NÄYTÄ formaatti** - anna esimerkki
4. **YKSINKERTAINEN kieli** - ei monimutkaisia ohjeita
5. **EI syvää päättelyä** - käytä isompaa mallia

## Milloin käyttää pientä mallia?

 **Sopii:**
- Luokittelu
- NER (nimien/paikkojen tunnistus)
- Yksinkertainen Q&A
- Tekstin muotoilu
- Kielentunnistus

 **Ei sovi:**
- Monimutkainen päättely
- Pitkä koodin generointi
- Luova kirjoitus
- Monimutkaiset JSON-rakenteet
