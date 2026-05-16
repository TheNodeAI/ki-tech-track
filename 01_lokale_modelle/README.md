# 01 — Lokale Modelle

Begleitmaterial zu M09 Video-Lektionen 1–3.

Dieses Kapitel hat keinen eigenen Code — die Installation von Ollama und LM Studio
wird in den Video-Lektionen als Screencast gezeigt. Hier findest du die wichtigsten
Befehle und Hinweise zum Nachschlagen.

---

## Ollama

### Installation

**Mac:**
Download auf ollama.com → Installer ausführen

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download auf ollama.com → Windows-Installer ausführen

### Wichtige Befehle

```bash
# Modell laden
ollama pull llama3.2

# Modell starten (interaktiv)
ollama run llama3.2

# Alle geladenen Modelle anzeigen
ollama list

# Modell entfernen (spart Speicherplatz)
ollama rm llama3.2

# Ollama-Status prüfen
ollama ps
```

### Empfohlene Modelle

Aktuelle Empfehlungen auf ollama.com/library. Als Orientierung:

| Grösse | RAM-Bedarf | Anwendungsfall |
|--------|-----------|----------------|
| 3B | ~4 GB | Schneller Einstieg, einfache Aufgaben |
| 7B | ~8 GB | Gute Qualität für die meisten Aufgaben |
| 13B | ~16 GB | Sehr gute Qualität, langsamere Antworten |

### Ollama als API nutzen

Ollama läuft standardmässig unter `http://localhost:11434`.
Du kannst es direkt über HTTP ansprechen:

```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "llama3.2",
    "prompt": "Erkläre mir was RAG ist, in zwei Sätzen.",
    "stream": false
  }'
```

### OpenWebUI installieren (Browser-Interface)

Voraussetzung: Docker installiert (docker.com)

```bash
docker run -d \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Danach unter http://localhost:3000 erreichbar.

---

## LM Studio

### Installation

Download auf lmstudio.ai → Installer für dein Betriebssystem

### Lokaler API-Server

1. Modell laden über die Suchoberfläche
2. Tab "Local Server" öffnen
3. Modell auswählen → "Start Server"
4. Server läuft unter `http://localhost:1234`

Die API ist OpenAI-kompatibel. Du kannst den Server in Python so ansprechen:

```python
from openai import OpenAI

# LM Studio statt OpenAI verwenden
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="nicht-noetig"  # LM Studio prüft den Key nicht
)

response = client.chat.completions.create(
    model="local-model",  # Name des geladenen Modells
    messages=[
        {"role": "user", "content": "Hallo, wie geht es dir?"}
    ]
)

print(response.choices[0].message.content)
```

Das ist identisch zum OpenAI-Code in `03_openai_api/` — nur die `base_url` ändert sich.

### RAM-Richtwerte nach Hardware

| Hardware | Empfehlung |
|----------|-----------|
| Mac M1/M2/M3, 8 GB | 3B–7B Modelle |
| Mac M1/M2/M3, 16 GB | 7B–13B Modelle |
| Windows/Linux, 16 GB RAM, keine dedizierte GPU | 3B–7B Modelle (langsam) |
| Windows/Linux, Nvidia GPU 8 GB VRAM | 7B Modelle (schnell) |

---

## Datenschutz-Checkliste

Bevor du ein lokales Modell für vertrauliche Daten nutzt:

- [ ] Ollama läuft lokal (kein Cloud-Hosting)
- [ ] Kein OpenWebUI mit externem Zugriff
- [ ] Kein Modell-API-Call geht nach aussen
- [ ] Dokumente bleiben auf dem lokalen Rechner

Bei n8n-Workflows: In den Anthropic/OpenAI-Nodes die base_url auf `http://localhost:11434` (Ollama) oder `http://localhost:1234` (LM Studio) setzen statt auf die Cloud-API.
