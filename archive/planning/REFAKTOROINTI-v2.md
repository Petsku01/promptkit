# Promptkit Refaktorointisuunnitelma v2.0

_Perustuu parallel-analyysiin (Bloat, Clarity, Architecture)_

---

## Yhteenveto

**Nykyinen tila:** Toimiva, mutta "god CLI module" -riski  
**Maintability:** 6/10  
**Tavoite:** 8/10  
**Arvioitu työmäärä:** 8-12 tuntia  
**Aikataulu:** 2-3 viikkoa osa-aikaisesti

---

## 🔴 Phase 1: Kriittiset (Viikko 1)

### 1.1 CLI:n pilkkominen

**Ongelma:** `cli.py` (~800 riviä) sisältää presentation + business logic + doctor

**Toteutus:**
```
src/llm_promptkit/
├── cli.py                 # Thin adapter (parser + dispatch)
├── commands/
│   ├── __init__.py
│   ├── list.py           # list_patterns
│   ├── build.py          # build_prompt + interactive_build
│   ├── doctor.py         # doctor_command (CLI-only)
│   ├── prompts.py        # prompts_command
│   └── search.py         # search_command
├── services/
│   ├── __init__.py
│   ├── prompt_service.py # prompt search, indexing
│   └── doctor_service.py # doctor analysis orchestration
└── doctor/
    ├── __init__.py
    ├── models.py         # DoctorIssue, IssueSeverity (canonical)
    ├── rules.py          # analyze_prompt (rule-based)
    └── ml_backend.py     # MLDoctor integration
```

**Tiedostot:**
- Luo `commands/`, `services/`, `doctor/` hakemistot
- Siirrä funktiot oikeisiin moduleihin
- Päivitä importit
- `cli.py`: ~200 riviin

**Aika-arvio:** 3-4h

### 1.2 Yhtenäinen Issue-model

**Ongelma:** `DoctorIssue` (cli), `MLDoctorIssue` (ml_doctor), tuple-form, `IssueSeverity` (utils)

**Toteutus:**
```python
# doctor/models.py
from enum import Enum
from dataclasses import dataclass

class IssueSeverity(Enum):
    CRITICAL = "Critical"
    WARNING = "Warning"
    SUGGESTION = "Suggestion"
    INFO = "Info"

@dataclass
class DoctorIssue:
    severity: IssueSeverity
    category: str
    issue: str
    suggestion: str
    # Optional: confidence for ML, rule_id for rule-based
    metadata: dict = field(default_factory=dict)
```

**Muutokset:**
- `doctor/models.py` — uusi canonical model
- `doctor/rules.py` — käytä uutta modelia
- `ml_doctor.py` — adapter MLDoctorIssue → DoctorIssue
- `cli.py` — poista tuple-form käsittely
- `utils.py` — poista IssueSeverity (siirretty doctor/models)

**Aika-arvio:** 2h

---

## 🟡 Phase 2: Tärkeät (Viikko 2)

### 2.1 Pattern-aliakset

**Ongelma:** Testit odottavat `json-enforcer`, toteutus on `json-output`

**Toteutus:**
```python
# pattern_loader.py tai uusi registry.py
PATTERN_ALIASES = {
    "json-enforcer": "json-output",
    "json_output": "json-output",
    # etc.
}

def resolve_pattern_name(name: str) -> str:
    canonical = name.lower().replace("_", "-")
    return PATTERN_ALIASES.get(canonical, canonical)
```

**Muutokset:**
- Lisää alias-tuki pattern_loaderiin
- Päivitä testit käyttämään kanonisia nimiä
- Lisää deprecation warning aliaksille

**Aika-arvio:** 1.5h

### 2.2 Interactive Prompts - State Machine

**Ongelma:** `interactive_prompts()` ~140 riviä, nesting depth 4

**Toteutus:**
```python
# commands/prompts_interactive.py
from enum import Enum, auto

class PromptsState(Enum):
    SELECT_PROVIDER = auto()
    SELECT_MODEL = auto()
    SELECT_PROMPT = auto()
    VIEW_PROMPT = auto()

def interactive_prompts():
    state = PromptsState.SELECT_PROVIDER
    context = {}
    
    while state != PromptsState.EXIT:
        if state == PromptsState.SELECT_PROVIDER:
            state, context = select_provider(context)
        elif state == PromptsState.SELECT_MODEL:
            state, context = select_model(context)
        # etc.

def select_provider(context) -> tuple:
    # ~30 riviä
    pass
```

**Aika-arvio:** 2-3h

### 2.3 Lazy Imports

**Ongelma:** Raskaat importit ladattu heti

**Toteutus:**
```python
# cli.py

def doctor_command(args):
    if args.ml:
        from .ml_doctor import MLDoctor  # Lazy
        # ...

def build_prompt(args):
    if args.tokens:
        import tiktoken  # Lazy
        # ...
```

**Aika-arvio:** 1h

---

## 🟢 Phase 3: Hienosäätö (Viikko 3)

### 3.1 Builder Refactor

**Ongelma:** `build()` ~60 riviä, manuaalinen string-concatenation

**Toteutus:**
```python
# builder.py

class PromptBuilder:
    def build(self) -> str:
        sections = []
        sections.extend(self._render_system())
        sections.extend(self._render_patterns())
        sections.extend(self._render_constraints())
        sections.extend(self._render_output())
        sections.extend(self._render_task())
        sections.extend(self._render_context())
        return "\n\n".join(sections)
    
    def _render_patterns(self) -> List[str]:
        # Pattern-specific logic here
        pass
```

**Aika-arvio:** 1.5h

### 3.2 Dokumentaatio

**Kohteet:**
- `interactive_prompts()` — state machine behavior
- `search_prompts()` — scoring algorithm
- `doctor_command()` — ML fallback semantics
- `ml_doctor.analyze()` — error classes/timeouts

**Aika-arvio:** 1h

### 3.3 Riippuvuus-fixit

**Ongelma:** `requests` käytössä mutta ei `pyproject.toml`:ssa

**Toteutus:**
```toml
# pyproject.toml
[project]
dependencies = [
    "rich>=13.0",
    "requests>=2.28",  # Lisää tämä
]

[project.optional-dependencies]
tokens = ["tiktoken>=0.5.0"]
ml = ["requests>=2.28"]  # Tai tee ML optional
```

**Aika-arvio:** 0.5h

---

## Suoritusjärjestys

```
Viikko 1:
├── Day 1: 1.1 CLI:n pilkkominen (aloitus)
├── Day 2: 1.1 CLI:n pilkkominen (loppu)
├── Day 3: 1.2 Yhtenäinen Issue-model
└── Day 4: Testaus + commit

Viikko 2:
├── Day 1: 2.1 Pattern-aliakset
├── Day 2: 2.2 Interactive Prompts (state machine)
├── Day 3: 2.3 Lazy imports
└── Day 4: Testaus + commit

Viikko 3:
├── Day 1: 3.1 Builder refactor
├── Day 2: 3.2 Dokumentaatio
├── Day 3: 3.3 Riippuvuus-fixit
└── Day 4: Lopputestaus + final commit
```

---

## Riskit

| Riski | Todennäköisyys | Vaikutus | Mitigaatio |
|-------|---------------|----------|------------|
| Import-virheet refaktoroinnissa | Korkea | Korkea | Tee vaiheittain, testaa jokaisen jälkeen |
| Testit hajoavat | Keskitaso | Korkea | Päivitä testit samalla |
| API-muutokset rikkovat käyttäjiä | Matala | Korkea | Säilytä backward compatibility |
| Aikataulu venyy | Keskitaso | Matala | Prioritoi Phase 1, jätä Phase 3 tarvittaessa |

---

## Commit-viestit

```
refactor: split cli.py into commands/ services/ doctor/

- Move command handlers to commands/
- Move business logic to services/
- Move doctor engine to doctor/
- cli.py now thin adapter only

---

refactor: unify DoctorIssue model

- Create doctor/models.py with canonical IssueSeverity + DoctorIssue
- Remove duplicate definitions from cli.py and ml_doctor.py
- Update all references
- Remove IssueSeverity from utils.py

---

feat: add pattern name aliases

- Support json-enforcer -> json-output etc.
- Add deprecation warnings for aliases
- Update tests to use canonical names

---

refactor: interactive prompts state machine

- Split interactive_prompts() into state handlers
- Reduce nesting depth from 4 to 2
- Add explicit state enum

---

perf: lazy imports for heavy dependencies

- Import tiktoken only when --tokens used
- Import MLDoctor only when --ml used
- Faster CLI startup

---

chore: add requests to pyproject.toml dependencies

- Fix missing runtime dependency
```

---

## Testausstrategia

Jokaisen vaiheen jälkeen:
1. **Yksikkötestit:** `pytest tests/ -v`
2. **Integration:** `pip install -e . && promptkit list/build/doctor`
3. **Import-nopeus:** `time python -c "from llm_promptkit.cli import main"`

---

*Luotu: 2026-04-06*  
*Kriitikot: Codex (Bloat, Clarity, Architecture) + Kimi (yhteenveto)*
