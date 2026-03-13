# Promptkit Repo Deep Review - Tehtävänanto

**Ajankohta:** Yöllä 2026-03-13  
**Suorittaja:** Codex  
**Lähestymistapa:** Senior Engineering - ei kiirettä, perusteellinen analyysi

---

## Repo sijainti
`~/.openclaw/workspace/promptkit/`

## Tehtävät

### 1. Rakenne-analyysi
- Käy läpi koko hakemistorakenne
- Dokumentoi mitä kukin kansio/tiedosto tekee
- Tunnista puuttuvat tai epäjohdonmukaiset osat

### 2. Koodin laatu
- Tarkista Python-koodi (syntaksi, tyylit, bugit)
- Aja testit: `cd ~/.openclaw/workspace/promptkit && python -m pytest`
- Tunnista refaktorointitarpeet

### 3. Dokumentaatio
- Onko README kattava?
- Puuttuuko esimerkkejä?
- Onko API-dokumentaatio ajan tasalla?

### 4. Prompt-patternit
- Käy läpi kaikki patternit (docs/patterns/ tai vastaava)
- Arvioi niiden laatu ja hyödyllisyys
- Ehdota uusia patterneita

### 5. Kilpailija-analyysi (Scrapling)
```bash
source ~/.openclaw/workspace/tools/scrapling-venv/bin/activate
python ~/.openclaw/workspace/tools/scraper.py "https://github.com/topics/prompt-engineering"
python ~/.openclaw/workspace/tools/scraper.py "https://github.com/dair-ai/Prompt-Engineering-Guide"
```

### 6. Innovaatiot
- Mitä puuttuu kilpailijoilta?
- Miten erottautua?
- Uudet ominaisuusideat

---

## Output
Luo: `~/.openclaw/workspace/promptkit/REVIEW-2026-03-13.md`

Sisältö:
1. Executive Summary (max 10 riviä)
2. Vahvuudet
3. Heikkoudet ja bugit
4. Korjausehdotukset (priorisoitu: P1/P2/P3)
5. Innovaatiomahdollisuudet
6. Toimenpidesuunnitelma (mitä tehdä ensin)

---

## Tärkeää
- Jos jokin ei toimi → kokeile toista tapaa
- Testaa löydökset ennen dokumentointia
- Ota aikaa - tämä on yötehtävä
- Commitoi: `git add -A && git commit -m "Deep review 2026-03-13"`
