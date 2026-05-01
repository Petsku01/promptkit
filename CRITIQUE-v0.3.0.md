# KRIITTIKKI-HISTORIA: PLAN-v0.3.0

## Sykli 1: Alustava draft

Ongelmat:
1. Chat-muoto Builderista — ylikerrostausta, ei Builderin vastuulla → **poistettu**
2. Jinja2-template engine — uusi riippuvuus tarpeeton → **korvattu string.Template**
3. Frontmatter-tagit 307 promptille — piilotettu työmäärä → **poistettu scopelta**
4. Search-välimuistus — aikaista optimointi → **poistettu**
5. Aikataulu optimistinen 17h → **korjattu 22h**
6. Ei testistrategiaa → **lisätty testivaatimukset**
7. Ei yhteensopivuussuunnitelmaa → **lisätty Section 7**
8. Doctor --fix turvallisuus määrittelemätön → **rajattu 4 korjaukseen**
9. Config-formaatti päättämättä → **TOML, ehdollinen tomli**
10. platformdirs-riippuvuus kyseenalainen → **korjattu, käytetään os.environ**
11. Prioriteetti väärä → **XDG → Doctor → Builder**
12. 95% coverage-vaatimus mielivaltainen → **poistettu**
13. Kohderyhmä määrittelemättä → **LLM-kehittäjät**

## Sykli 2: Tarkennettu draft → Sykli 3

Lisäykset ja korjaukset:
1. **`string.Template` ja dollarimerkit** — Riski että patternissa olisi `$`-merkki luonnollisesti. Tutkittu: 18 nykypatternia eivät käytä `$`:tä. Turva: `safe_substitute` jättää tunnistamattomat muuttujat sellaisenaan. Lisätty `$$`-escapen huomio.
2. **`default_persona` ja `default_model` käyttö** — Ei ollut määritelty. Nyt: `default_persona` käytetään CLI:ssä kun `--persona` puuttuu. `default_model` varattu, ei API-muutosta.
3. **`please`-sanan poiston regex** — Lisätty tarkka word boundary -regex. Huomioitu että lauseen alun "Please" korjautuu "Review" jne.
4. **Vain absoluuttiset polut konfiguraatiossa** — Päätös tehty. Suhteelliset ohitetaan varoituksella.
5. **Konfiguraation virheenkäsittely** — Lisätty: virheellinen config → varoitus stderriin + oletukset.
6. **JSON-output skeemoitu** — Lisätty `version`-kenttä ja `fixable`-kenttä.
7. **Yhteensopivuustaulukko** — Lisätty Section 7: ei yhtään breaking changea.

## Lopullinen arvio

Suunnitelma on kattava, realistinen ja perusteltu. Pääasiat:
- Ei uusia riippuvuuksia (paitsi ehdollinen tomli Python <3.11)
- Täysin taaksepäin yhteensopiva
- Opt-in-periaate (config puuttuu → vanha käytös)
- Selkeä rajaus mistä ei tehdä ja miksi
- 3 iteraatiota kriitikin ja korjauksen kautta