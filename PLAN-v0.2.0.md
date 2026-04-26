# PLAN-v0.2.0: llm-promptkit — Perustus kuntoon (v2.0)

**Versio:** 2.0 (Kimi K2.5 -sparraus huomioitu)  
**Päivä:** 2026-04-26  
**Edellinen:** v0.1.0 (Alpha)  
**Kohde:** v0.2.0 (Alpha → Beta)  
**Tyyppi:** Harrasteprojekti  

---

## 0. Kimin sparraus — otetut huomioon

| Kimin huomio | Päätös |
|-------------|--------|
| Vaihejärjestys väärin (CLI ennen dataa) | ✅ Patterns SSOT ennen CLI-refaktorointia |
| Dict-fallback on teknistä velkaa | ✅ Poistetaan kokonaan, ei deprecated-fallbackia |
| Harkitse Typeria nyt | ✅ Otetaan Typer scopeen — argparse-refaktorointi olisi kuollutta työtä |
| Resurssien paketointi patternsille | ✅ Lisätty, sama tapa kuin promptsille |
| Puuttuva skeema-validointi .md:lle | ✅ Lisätty CI-check + pre-commit hook |
| Aika-arvio optimistinen | ✅ Päivitetty 9h → 14h |
| Smoke test ennen refaktorointia | ✅ Lisätty vaihe 0 |
| importlib.resources toimii eri tavalla -e vs wheel | ✅ Lisätty wheel-smoke-test CI:hen |

---

## 1. Tavoite v0.2.0

**"Asennettu paketti toimii päästä päähän. Yksi totuuden lähde. CLI kestää kehitystä."**

v0.1.0 on Alpha. v0.2.0 on Beta — breaking changes sallittuja, mutta API:n pitäisi olla stabiili tästä eteenpäin.

---

## 2. Työtehtävät (uusi järjestys)

### Vaihe 0: Smoke test (0.5h)

Ennen mitään refaktorointia — varmista että nykyinen tila toimii.

- [ ] Aja `uv run pytest tests/ -q` → 104 passaa
- [ ] Aja `promptkit doctor "make it good"` → tunnistaa ongelmia
- [ ] Aja `promptkit prompts` → listaa promptit
- [ ] Buildaa wheel: `uv build` → asenna erilliseen ympäristöön ja testaa
- [ ] Tallenna tuloket — tämä on vertailukohta

---

### Vaihe 1: Brändäys + siivous + Typer-siirtymä (2h)

**T1: Kanoninen nimi: `promptkit`**

- `promptkit` = komento (CLI)
- `llm-promptkit` = PyPI-paketti
- Poista kaikki viittaukset "prompt-patterns" koodista
- Päivitä docstringit, README, pyproject.toml

**T2: Siirry Typeriin**

Perustelu: 719 riviä argparsea on kuollutta koodia jos Typer on tulossa joka tapauksessa. Typer pakottaa automaattisesti paremman rakenteen (komennot funktioiksi, tyypit annotaatioiksi).

Lisäriippuvuus: `typer>=0.9.0` (rich-kompat, jo optional-dependencies-listalla)

Uusi rakenne:
```
src/llm_promptkit/
    __init__.py
    builder.py
    patterns/            # .md patternitiedostot (siirretty sisälle)
    prompts/             # .md promptit (jo sisällä)
    cli/
        __init__.py      # app = Typer()
        commands/
            __init__.py
            build.py     # build-komento + interactive
            doctor.py    # doctor-komento + heuristiikat
            prompts.py   # prompts-komento (list, show)
            search.py    # search-komento
```

**T3: Siivous**

- Poista `patch_doctor.py` ja `refactor_doctor.py` juuresta
- Poista `prompts/` ja `patterns/` juuresta (duplikaatit, alkuperäiset ovat `src/llm_promptkit/` alla)
  - Varmistettu: sisältö identtinen

**T4: Korjaa riippuvuusväite dokumentaatiossa**

- `rich>=13.0` on riippuvuus, ei stdlib
- Käy docs/ läpi

- [ ] Typer-rakenne luotu
- [ ] Kaikki 5 komentoa toimii Typerillä
- [ ] argparse-poistetut
- [ ] pyproject.toml päivitetty (dependencies + entry point)
- [ ] Juuren roskat poistettu
- [ ] Dokumentaatiorikkeet korjattu

---

### Vaihe 2: Patterns SSOT (3h)

**T5: Poista hardkoodattu PATTERNS-dict kokonaan**

Ei fallbackia. Alpha→Beta -siirtymässä breaking changes on sallittu.

1. Konvertoi kaikki 13 hardkoodattua patternia `.md`-tiedostoiksi `patterns/`-hakemistoon
2. Luo `PatternLoader`-luokka joka lukee `patterns/`-hakemiston `importlib.resources`:lla
3. Päivitä `PromptBuilder.pattern()` käyttämään PatternLoaderia
4. Jos .md puuttuu → **nostetaan ValueError**, ei fallbackia

Pattern .md -formaatti:
```markdown
# chain-of-thought

## When to Use
Step-by-step logical reasoning tasks.

## Prompt
Think through this step-by-step:
1. First, analyze the problem
...
```

**T6: Resurssien paketointi**

- Varmista että `patterns/` on mukana wheelissä (sama tapa kuin promptsille)
- `pyproject.toml`: `[tool.setuptools.package-data]` — patterns jo listattu
- Lisää CI-check: build wheel → install → verify `promptkit list` toimii

- [ ] 13 patternia konvertoitu .md-muotoon
- [ ] PatternLoader implementoitu
- [ ] PATTERNS-dict poistettu builder.py:stä
- [ ] importlib.resources toimii patternsille
- [ ] Varmista että wheel sisältää patterns/

---

### Vaihe 3: Testien parantaminen (3h)

**T7: Korvaa heikot testit**

- Käy läpi kaikki 104 testiä, merkitse heikot
- Doctor-testit: assertoi että oikeat issuet tunnistetaan (sisältö, ei vain print)
- Build-testit: assertoi buildin tulos tekstisisältönä
- Prompts-testit: assertoi että listaus palauttaa oikeat nimet

**T8: Wheel-smoke-test**

- Lisää `tests/integration/test_wheel_install.py`
- Buildaa wheel, asenna erilliseen venviin, aja `promptkit prompts` ja `promptkit doctor`
- Vaihtoehto: `tox` tai yksinkertainen skripti

**T9: Pattern-validointi CI:ssä**

- Pre-commit hook tai CI-step joka varmistaa:
  - Kaikki .md-tiedostot `patterns/` alla ovat parsittavissa
  - Ei puuttuvia pakollisia kenttiä (title, when to use, prompt)
  - PatternLoader löytää kaikki tiedostot

- [ ] Heikot testit korjattu
- [ ] Wheel-smoke-test lisätty
- [ ] Pattern-validointi CI:ssä
- [ ] Assertittomat testit poistettu/korjattu

---

### Vaihe 4: Dokumentaation yhtenäistäminen (2h)

**T10: Kaikki .md:t kuntoon**

- README: päivitys (Typer-komennot, uusi rakenne)
- docs/: kaikki esimerkit oikein
- Importit: `from llm_promptkit import PromptBuilder`
- Komennot: `promptkit` (ei prompt-patterns)
- Asennus: `pip install llm-promptkit`
- Poista viittaukset deprecated-dictiin

- [ ] README päivitetty
- [ ] docs/ läpikäyty
- [ ] Esimerkit toimivia
- [ ] Changelog-merkintä v0.2.0

---

## 3. Ei scopessa v0.2.0

- ❌ Uusia prompt-patterneja
- ❌ Plugin-arkkitehtuuri
- ❌ A/B-testaus malleille
- ❌ Auto-refine Doctor (LLM-pohjainen)
- ❌ Käyttäjän custom prompt-hakemistot (XDG)

---

## 4. Hyväksymiskriteerit v0.2.0

- [ ] `pip install llm-promptkit` → `promptkit` toimii suoraan
- [ ] `promptkit prompts` listaa promptit (asennettuna)
- [ ] `promptkit doctor "make it good"` tunnistaa ongelmat
- [ ] `promptkit build --persona ... --pattern ... --task ...` toimii
- [ ] `promptkit list` näyttää patternit patterns/-kansiosta (ei hardkoodattua dictiä)
- [ ] CLI-koodi jaettu moduuleihin (Typer), ei yli 200 rivin tiedostoja
- [ ] Yksi totuuden lähde: patterns/ (.md-tiedostot)
- [ ] PATTERNS-dict poistettu koodista
- [ ] Testit assertoivat sisältöä, ei vain metodikutsuja
- [ ] Wheel-smoke-test CI:ssä
- [ ] Ei roskascriptejä juuressa
- [ ] Dokumentaatio yhtenäinen

---

## 5. Aikataulu

| Vaihe | Kesto (realistinen) | Riippuvuus |
|-------|---------------------|-----------|
| 0. Smoke test | 0.5h | Ei |
| 1. Brändäys + Typer + siivous | 2h | Ei |
| 2. Patterns SSOT | 3h | Ei (voi rinnakkain V1:n kanssa) |
| 3. Testit | 3h | V1 + V2 |
| 4. Dokumentaatio | 2h | Kaikki |
| **Yhteensä** | **~10.5h** | |

Huom: Typer säästää aikaa CLI-refaktoroinnissa (automaattinen rakenne vs käsityö argparseen), joten nettosäästö ~2h vs alkuperäinen argparse-suunnitelma.

---

## 6. Riskit ja hallinta

| Riski | Todennäköisyys | Hallinta |
|-------|---------------|----------|
| importlib.resources toimii eri tavalla -e vs wheel | Keskitaso | Wheel-smoke-test CI:ssä |
| Typer-riippuvuus rikkoo jotain | Matala | Typer on vakaa, rich-yhteensopiva |
| Pattern .md -tiedostoja ei löydy asennettuna | Keskitaso | package-data + CI-validointi |
| Komennon nimen muutos rikkoo käyttäjien skriptejä | Matala | Alpha-tila, Breaking OK |
| Testiaukko refaktoroinnissa | Keskitaso | Smoke test (V0) vertailukohtana |

---

_Suunnitelma: Kuu & Petsku, sparrattu Kimi K2.5:llä_