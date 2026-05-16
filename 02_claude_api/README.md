# 02 — Claude API

Erste Schritte mit der Anthropic Claude API.

## Voraussetzung

API-Key auf console.anthropic.com erstellen und als Umgebungsvariable setzen:

```bash
export ANTHROPIC_API_KEY="dein-key"
```

Bibliothek installieren:
```bash
pip install anthropic
```

---

## Dateien in diesem Ordner

| Datei | Inhalt |
|-------|--------|
| `01_erster_api_call.py` | Minimaler erster Call — Text zusammenfassen |
| `02_mit_system_prompt.py` | System-Prompt verwenden für spezialisiertes Verhalten |
| `03_konversation.py` | Mehrstufige Konversation mit Gesprächsgedächtnis |

---

## Schnellstart

```bash
python3 01_erster_api_call.py
```

---

## Wichtige Hinweise

**Modellnamen ändern sich.** Immer aktuellen Stand prüfen:
https://docs.anthropic.com/models

**Kosten pro 1M Tokens (Richtwert Mai 2026):**
- Haiku (günstig, schnell): ~$0.80 Input / $4.00 Output
- Sonnet (ausgewogen): ~$3.00 Input / $15.00 Output
- Opus (leistungsstark): ~$15.00 Input / $75.00 Output

Für alle Beispiele in diesem Ordner: unter $0.10 Gesamtkosten.

**Empfehlung:** Immer mit dem günstigsten Modell starten.
Nur upgraden wenn die Qualität nicht ausreicht.
