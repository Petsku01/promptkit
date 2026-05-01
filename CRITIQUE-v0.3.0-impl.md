# Kritiikki: promptkit v0.3.0 toteutus

## KRIITTINEN (korjattava ennen releasea)

### 1. [CRITICAL] `_apply_safe_fixes` "please" poistaa liian aggressiivisesti
**Tiedosto:** `doctor.py` rivi 332
**Ongelma:** `\b[Pp]lease\b\s*` regex poistaa "Please" lauseen alusta mutta jättää ylimääräisen välin. "Please review this" → "review this" (väli poistetaan), mutta "Please note:" → "note:" (väli poistetaan). Tämä on ok. MUTTA "Please, review this" → ", review this" — pilkku jää koska `\s*` ei poista pilkkua.
**Korjaus:** `\b[Pp]lease\b[,\s]*` — poista myös mahdollinen pilkku.

### 2. [HIGH] Config-singleton `_config` globaali muuttuja on säikeistön altis
**Tiedosto:** `config.py` rivit 184-202
**Ongelma:** `_config` on moduulitason globaali. Usean säikeen samanaikainen käyttö voi johtaa kilpatilanteeseen. V0.3.0:ssa tämä ei ole käytännön ongelma koska CLI on yksisäikeinen, mutta kirjaston API-käyttäjät voivat kohdata ongelmia.
**Korjaus:** Lisää `threading.Lock` get_config/reload_config-funktioihin. Tai ainakin dokumentoi että konfiguraatio ei ole säikeistön turvallinen.

### 3. [HIGH] `_resolve_dirs` ei varoita ei-absoluuttisista poluista käytännössä
**Tiedosto:** `config.py` rivit 137-157
**Ongelma:** `_validate()` varoittaa ei-absoluuttisista poluista, mutta `_resolve_dirs` hiljaa ohittaa ne (`continue` ilman varoitusta). Jos `_validate` ajetaan ennen `_resolve_dirs`, käyttäjä näkee varoituksen JÄLKEEN että polku on ohitettu. Tämä on hämmentävää.
**Korjaus:** Yhdistä varoitus `_resolve_dirs`-metodiin ja poista `_validate`-metodin duplikaattivaroinnit.

### 4. [HIGH] `read_pattern` lru_cache ei huomioi config-muutoksia
**Tiedosto:** `_registry.py` rivi 126
**Ongelma:** `read_pattern` on `@lru_cache(maxsize=32)` mutta se kutsuu `_get_pattern_dirs()` joka kutsuu `get_config()`. Jos config muuttuu, `read_pattern` palauttaa vanhan arvon koska lru_cache ei huomaa että sisäinen riippuvuus muuttui.
**Korjaus:** `invalidate_pattern_cache()` pitää kutsua aina kun config muuttuu. Tämä on nyt testien vastuulla, mutta kirjaston käyttäjän näkökulmasta se on ansa.

### 5. [MEDIUM] `_has_any_phrase` on O(n*m) jokaisella heuristiikkakierroksella
**Tiedosto:** `doctor.py` rivi 104
**Ongelma:** Jokainen heuristiikka kutsuu `_has_any_phrase` joka kutsuu `_match_phrase` joka tekee regex-haun. Pitkillä prompteilla ja monilla heuristiikoilla tämä on hidas.
**Korjaus:** Esikäännä regexit kerran moduulin ladatessa (`_re.compile`). Mutta koska promptit ovat yleensä lyhyitä (<5000 sanaa), tämä ei ole kiireellinen.

## EI-KRIITTINEN (parannuksia myöhemmin)

### 6. [MEDIUM] Builder testi mockaa väärin
**Tiedosto:** `test_builder_variables.py` rivi 29
**Ongelma:** `_registry.read_pattern = _registry.read_pattern.__wrapped__` poistaa lru_cachen väliaikaisesti. Tämä on hauras ja riippuvainen toteutuksesta.
**Suositus:** Käytä `unittest.mock.patch` mockaamaan `read_pattern` palauttamaan custom-patternin.

### 7. [LOW] Doctorin "code only" -tarkistus ei toimi hyvin
**Tiedosto:** `doctor.py` rivi 293-302
**Ongelma:** Jos teksti on vain koodia (`text_no_code` on tyhjä), Doctor sanoo "contains only code". Mutta tämä on tarkka väite — entä jos teksti on "```python\ncode\n```\nPlease explain"? Se ei ole "only code" mutta `text_no_code` = "Please explain" joka on lyhyt.
**Suositus:** Muuta "contains only code" → "mostly code" tai tarkista väliarvot.

### 8. [LOW] Helpers.py `CHARS_PER_TOKEN` on tyhjä
**Tiedosto:** `helpers.py` rivi 14
**Ongelma:** `CHARS_PER_TOKEN=***` — näyttää siltä että arvo on redactoitu tai korruptoitunut. Tämä ei ole toimiva Python-koodi.
**Korjaus:** Aseta arvoksi `4` (kuten builder.py:n kommentti sanoo).

### 9. [LOW] `helpers.py` käyttää `get_prompts_dir()` ei `get_all_prompt_dirs()`
**Tiedosto:** `helpers.py` rivi 17-26
**Ongelma:** `get_prompts_dir()` palauttaa vain built-in hakemiston, ei custom-hakemistoja. `get_all_prompt_dirs()` palauttaa kaikki. Mutta `get_prompt_files()` (rivi 52) käyttää `directory`-argumenttina vain yhtä hakemistoa. CLI-komennot käyttävät `get_all_prompt_dirs()` oikein, joten tämä ei ole bugi, mutta nimeäminen on hämmentävää.

### 10. [LOW] `import sys as _sys` kahdesti `_load_toml`:ssa
**Tiedosto:** `config.py` rivit 54 ja 66
**Ongelma:** `_sys` on alias `sys`:lle, joka on jo importoitu rivillä 8. Ei haittaa mutta on turhaa.
**Korjausehdotus:** Poista `import sys as _sys` ja käytä `sys.stderr`.

### 11. [LOW] `_TEMPLATE_VAR_RE` ohittaa `$`-merkit matemaattisissa yhtälöissä
**Tiedosto:** `builder.py` rivi 193
**Ongelma:** Regex `\$(?:([a-zA-Z_][a-zA-Z0-9_]*)|\\{([^}]+)\\})` löytää `$x` matemaattisista lausekkeista kuten "Solve for $x where $y = 5". Nämä eivät ole template-muuttujia.
**Suositus:** Harkitse `$`-detektoinnin parantamista (esim. vain kun patternin sisällä on template-sisältöä). Tämä on kuitenkin edge case ja `safe_substitute` ei korvaa mitään jos `builder._variables` on tyhjä, joten käytännössä ei vakava.

## Yhteenveto

**Käsiteltävää ennen releasea:**
1. ✅ `CHARS_PER_TOKEN=***` — korjattava (rikkoaa helpers.py:n)
2. ✅ `_apply_safe_fixes` — pilkku "please" jäljessä
3. ✅ `import sys as _sys` — siivous
4. 📝 Cache-invalidation-dokumentaatio — lisättävä docstringiin

**Kaikki muut** ovat joko ei-kriittisiä tai parannuksia myöhemmin.