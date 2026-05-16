# KI Tech Track — Begleitmaterial zum Kurs

Dieses Repository enthält den technischen Begleitmaterial zu **Modul 09** des KI-Kurses.

Es richtet sich an alle die nach den Video-Lektionen (L1–L3) tiefer einsteigen wollen: eigene API-Calls bauen, einen Chatbot schreiben, RAG implementieren.

**Voraussetzung:** Du hast M02–M08 des Kurses abgeschlossen und weisst wie KI-Modelle und APIs grundsätzlich funktionieren.

---

## Voraussetzungen

- Python 3.10 oder höher
- Ein API-Key von Anthropic (console.anthropic.com) und/oder OpenAI (platform.openai.com)
- Grundlegende Terminal-Kenntnisse (cd, ls, python3 ausführen)

Python installiert? Prüfen mit:
```bash
python3 --version
```

---

## Einrichtung

**1. Repository klonen**
```bash
git clone https://github.com/dein-nutzername/ki-tech-track.git
cd ki-tech-track
```

**2. Virtuelle Umgebung erstellen (empfohlen)**
```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Abhängigkeiten installieren**
```bash
pip install -r requirements.txt
```

**4. API-Keys als Umgebungsvariablen setzen**
```bash
cp .env.example .env
# .env öffnen und Keys eintragen
```

Dann die .env laden:
```bash
# Mac/Linux
export $(cat .env | xargs)

# Oder direkt setzen:
export ANTHROPIC_API_KEY="dein-key"
export OPENAI_API_KEY="dein-key"
```

---

## Struktur

```
ki-tech-track/
├── 01_lokale_modelle/     → Ollama und LM Studio Setup-Notizen
├── 02_claude_api/         → Erste Schritte mit der Claude API
├── 03_openai_api/         → Erste Schritte mit der OpenAI API
├── 04_chatbot/            → Vollständiger Chatbot mit Gesprächsgedächtnis
└── 05_rag/                → RAG — KI auf eigenen Dokumenten
```

---

## Empfohlene Reihenfolge

1. **`01_lokale_modelle/`** — Ollama installieren, erstes lokales Modell starten
2. **`02_claude_api/`** — Erster API-Call, System-Prompts, Konversationen
3. **`03_openai_api/`** — Dieselben Konzepte mit OpenAI, Vergleich
4. **`04_chatbot/`** — Chatbot zusammensetzen und anpassen
5. **`05_rag/`** — RAG auf eigenen Dokumenten aufbauen

Jeder Ordner hat eine eigene `README.md` mit Erklärungen und Schritt-für-Schritt-Anleitung.

---

## Wichtige Hinweise

**API-Keys niemals in Code eintragen.** Immer über Umgebungsvariablen laden. Die `.env`-Datei ist in `.gitignore` — sie wird nicht ins Repository hochgeladen.

**Kosten:** Alle Beispiele nutzen die günstigsten verfügbaren Modelle. Typische Kosten für das Durcharbeiten aller Beispiele: unter 0.50 USD.

**Modellnamen ändern sich.** Aktuelle Modellnamen immer in der offiziellen Dokumentation prüfen:
- Anthropic: docs.anthropic.com/models
- OpenAI: platform.openai.com/docs/models

---

## Lizenz

MIT — du kannst den Code frei verwenden, anpassen und weitergeben.
