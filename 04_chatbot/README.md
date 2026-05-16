# 04 — Chatbot mit Gesprächsgedächtnis

Ein vollständiger, interaktiver Chatbot in ~50 Zeilen Python.

## Starten

```bash
python3 assistent.py
```

## Befehle im Chat

| Befehl | Aktion |
|--------|--------|
| `exit` | Programm beenden |
| `neu` | Gesprächsverlauf löschen, neue Konversation starten |
| Strg+C | Sofort beenden |

## Anpassen

Der einfachste Hebel: den **System-Prompt** in `assistent.py` ändern.

Beispiele:

```python
# Übersetzungsassistent
system_prompt = """Du bist ein Übersetzungsassistent.
Übersetze alles was der Nutzer schreibt auf Englisch.
Antworte nur mit der Übersetzung, ohne Erklärungen."""

# Code-Reviewer
system_prompt = """Du bist ein erfahrener Python-Entwickler.
Reviewe den Code den der Nutzer schickt.
Zeige konkret was verbessert werden sollte und warum."""

# Meeting-Protokoll-Assistent
system_prompt = """Du bist ein Assistent für Meeting-Protokolle.
Wenn der Nutzer Stichpunkte aus einem Meeting schickt,
strukturiere sie in: Entscheidungen, Offene Punkte, Nächste Schritte.
Antworte auf Deutsch."""
```

## Erweiterungsideen

**API-Key aus .env-Datei laden:**
```python
from dotenv import load_dotenv
load_dotenv()
```

**Konversation speichern:**
```python
import json

def speichern(history, dateiname="konversation.json"):
    with open(dateiname, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
```

**Gegen LM Studio richten (lokal, kein Internet):**
```python
# In assistent.py die Zeile mit Anthropic ersetzen durch:
from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="nicht-noetig")
# Dann die messages.create()-Syntax auf OpenAI-Format anpassen (siehe 03_openai_api/)
```
