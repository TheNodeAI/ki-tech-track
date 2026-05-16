# 03 — OpenAI API

Erste Schritte mit der OpenAI API.

Die Konzepte sind identisch zur Claude API in `02_claude_api/`.
Unterschiede: Bibliothek, Modellnamen, minimale Syntax-Details.

## Voraussetzung

```bash
export OPENAI_API_KEY="dein-key"
pip install openai
```

---

## Dateien

| Datei | Inhalt |
|-------|--------|
| `01_erster_api_call.py` | Minimaler erster Call |
| `02_claude_vs_openai.py` | Direkter Vergleich beider APIs auf dieselbe Aufgabe |

---

## OpenAI-Modellfamilie (Stand Mai 2026)

Aktuelle Modellnamen immer prüfen: platform.openai.com/docs/models

| Modell | Anwendungsfall |
|--------|---------------|
| gpt-4o-mini / GPT-5.5 Instant | Günstig, schnell, für Standardaufgaben |
| gpt-4o / GPT-5.5 | Ausgewogen, multimodal (Text + Bilder) |
| o1 / o3 | Komplexes Reasoning, Mathematik, mehrstufiges Denken |

**Empfehlung:** Mit dem günstigsten Modell starten.

---

## LM Studio als lokale OpenAI-Alternative

Du kannst alle OpenAI-Skripte gegen LM Studio richten —
ohne Änderungen ausser der base_url:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="nicht-noetig"
)
```

Der Rest des Codes bleibt identisch.
Details dazu in `01_lokale_modelle/README.md`.
