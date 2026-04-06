# Promptkit Korjaussuunnitelma v1

_Perustuu parallel-kritiikkiin (arkkitehtuuri, toteutus, dokumentaatio)_

---

## Yhteenveto

**Prioriteetti:** Korkein → Matalin (1-4)  
**Arvioitu työmäärä:** 6-8 tuntia  
**Aikataulu:** 1-2 viikkoa

---

## 🔴 Priority 1: Kriittiset (toimivuus)

### 1.1 Dynaaminen pattern-lataus
**Ongelma:** Patternit kovakoodattu `builder.py` PATTERNS-dictiin JA `patterns/` kansiossa — duplikaatio, ylläpito hankalaa

**Korjaus:**
```python
# Uusi lähestymistapa: Lataa patterns/ kansiosta
import os
import re

class PatternLoader:
    @staticmethod
    def load_from_markdown(patterns_dir: Path) -> Dict[str, str]:
        patterns = {}
        for md_file in patterns_dir.glob("**/*.md"):
            # Parsi YAML frontmatter tai markdown-sisältö
            content = md_file.read_text()
            pattern_name = md_file.stem
            patterns[pattern_name] = extract_pattern_content(content)
        return patterns
```

**Tiedostot:**
- `src/llm_promptkit/pattern_loader.py` (uusi)
- `src/llm_promptkit/builder.py` (refactor)

**Aika-arvio:** 2-3h

---

## 🟡 Priority 2: Tärkeät (laatu)

### 2.1 Doctor-komennon yksikkötestit
**Ongelma:** Doctor toimii heuristiikalla, mutta ei ole testikattavuutta

**Korjaus:**
```python
# tests/test_doctor.py
import pytest
from llm_promptkit.cli import analyze_prompt

def test_detects_vague_phrases():
    result = analyze_prompt("Make it good please")
    assert any("Vague" in issue.severity for issue in result)

def test_detects_missing_role():
    result = analyze_prompt("Write code")
    assert any("Missing role" in issue.suggestion for issue in result)
```

**Aika-arvio:** 1-2h

### 2.2 DRY-refaktorointi CLI:ssä
**Ongelma:** `get_prompts_dir()` fallback-logiikka toistuu

**Korjaus:**
- Eriytä utility-funktiot `utils.py`
- Käytä samaa funktiota kaikkialla

**Tiedostot:**
- `src/llm_promptkit/utils.py` (uusi)
- `src/llm_promptkit/cli.py` (refactor)

**Aika-arvio:** 1h

---

## 🟢 Priority 3: Hienosäätö (dokumentaatio)

### 3.1 Selvennä "275+ prompts" -lupaus
**Ongelma:** README sanoo "275+ curated prompts", mutta näyttää vain 9 patternia

**Korjaus:**
```markdown
<!-- README.md -->
## What's Included

- **275+ curated prompts**: Model-specific prompts in `prompts/` directory
  - Organized by provider (openai, anthropic, google, etc.)
  - Quick (~100 tokens) and Extended (~300-500 tokens) versions
  
- **9 documented patterns**: Reusable prompt engineering patterns in `patterns/`
  - Chain-of-Thought, Self-Consistency, JSON Enforcer, etc.
  - Copy-paste ready with examples
```

**Aika-arvio:** 30min

### 3.2 Lisää CLI `--help` README:hen
**Ongelma:** Käyttäjä ei näe kaikkia flags ilman asennusta

**Korjaus:**
```markdown
## CLI Reference

```bash
$ promptkit --help

Commands:
  list        List available patterns
  build       Build a prompt from pattern
  doctor      Analyze prompt for issues
  prompts     Browse included prompts
  search      Search prompts by keyword

Options:
  --persona      Set AI persona/role
  --pattern      Select prompt pattern
  --task         Main task description
  --output       Output format (json, markdown)
  --interactive  Interactive mode
```
```

**Aika-arvio:** 30min

### 3.3 Korjaa pattern-linkit
**Ongelma:** README linkittää `patterns/reasoning/chain-of-thought.md` — tarkista rakenne

**Korjaus:**
```bash
# Tarkista oikea rakenne
ls -la patterns/

# Päivitä linkit vastaamaan todellisuutta
```

**Aika-arvio:** 15min

---

## 🔵 Priority 4: Jatkokehitys (v2.0)

### 4.1 ML-pohjainen Doctor (vaihtoehto)
**Ongelma:** Nykyinen heuristiikka on jäykkä (kovakoodatut phrase-listat)

**Mahdollinen ratkaisu:**
- Pieni fine-tuned malli (esim. Qwen 2.5 1.5B) promptien analysointiin
- Tai: Sentence Transformer + classification head
- **Huom:** Kasvattaa riippuvuuksia ja kokoa

**Aika-arvio:** 4-6h (ei v1.0:een)

---

## Suoritusjärjestys

```
Viikko 1:
├── Day 1-2: Priority 1 (Dynaaminen pattern-lataus)
├── Day 3: Priority 2.1 (Doctor-testit)
└── Day 4: Priority 2.2 (DRY-refaktorointi)

Viikko 2:
├── Day 1: Priority 3.1-3.2 (Dokumentaatio)
└── Day 2: Priority 3.3 (Linkit) + testaus + git commit
```

---

## Testausstrategia

Jokaisen korjauksen jälkeen:
1. **Yksikkötestit:** `pytest tests/ -v`
2. **Integraatio:** `pip install -e . && promptkit list`
3. **Wheel-testi:** `python -m build && pip install dist/*.whl --force-reinstall`

---

## Commit-viestit

```
feat: add dynamic pattern loading from markdown

- Remove hardcoded PATTERNS dict from builder.py
- Add PatternLoader class
- Load from patterns/**/*.md automatically
- Maintains backward compatibility

Closes: #1

---

test: add unit tests for prompt doctor

- Tests for vague phrase detection
- Tests for missing role detection
- Tests for token inefficiency
- 95% coverage for doctor module

---

docs: clarify "275+ prompts" promise and add CLI help

- Explain difference between prompts/ and patterns/
- Add full --help output to README
- Fix broken pattern links

---

refactor: DRY for prompt directory resolution

- Extract get_prompts_dir() to utils.py
- Remove duplication from cli.py
- No functional changes
```

---

## Riskit

| Riski | Todennäköisyys | Vaikutus | Mitigaatio |
|-------|---------------|----------|------------|
| Dynaaminen lataus hajottaa taaksepäin yhteensopivuuden | Matala | Korkea | Ylläpidä PATTERNS dict fallbackina |
| Testit löytävät regressioita | Keskitaso | Matala | Korjaa ennen mergeä |
| Dokumentaatio epäsynkassa koodin kanssa | Korkea | Matala | Automaattiset linkkitarkistukset |

---

*Luotu: 2026-04-05*  
*Kriitikot: Kimi (arkkitehtuuri), Qwen (toteutus), Gemma (dokumentaatio)*
