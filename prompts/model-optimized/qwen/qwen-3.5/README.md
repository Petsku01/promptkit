# Qwen 3.5 (Pieni malli)

## Ominaisuudet
- **Koot:** 0.6B, 1.7B, 4B, 8B, 14B, 32B
- **Konteksti:** 32K tokenia
- **Vahvuudet:** Nopea, edge-käyttö, kustannustehokas

## Promptit teemoittain

| Teema | Tiedosto |
|-------|----------|
| Perus | [basic.md](basic.md) |
| Koodaus | [coding.md](coding.md) |
| JSON | [json-output.md](json-output.md) |

##  Pienten mallien säännöt

1. **LYHYET promptit** - alle 200 tokenia
2. **YKSI tehtävä kerrallaan**
3. **Selkeä formaatti** - näytä esimerkkioutput
4. **Ei monimutkaista päättelyä** - käytä isompaa mallia

## Kokosuositukset

| Koko | Sopii | Ei sovi |
|------|-------|---------|
| 0.6B-1.7B | Luokittelu, NER, yksinkertainen | Koodi, päättely |
| 4B-8B | Peruskoodaus, yhteenveto | Monimutkainen analyysi |
| 14B+ | Useimmat tehtävät | - |
