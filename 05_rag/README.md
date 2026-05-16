# 05 — RAG: KI auf eigenen Dokumenten

RAG (Retrieval Augmented Generation) ermöglicht es KI auf Basis
deiner eigenen Dokumente zu antworten — ohne Fine-Tuning,
ohne Daten in ein Modell einzubauen.

## Das Grundprinzip

1. **Dokumente aufteilen** — grosse Texte in kleine Abschnitte (Chunks)
2. **Embeddings berechnen** — jeden Chunk in einen Zahlenvektor umwandeln
3. **Index aufbauen** — Vektoren lokal speichern
4. **Bei Fragen suchen** — relevante Chunks finden
5. **Modell antwortet** — auf Basis der gefundenen Chunks

## Installation

```bash
pip install llama-index llama-index-llms-anthropic llama-index-embeddings-huggingface chromadb
```

Der erste Start lädt ein Embedding-Modell herunter (~100 MB). Das passiert automatisch.

## Dateien

| Datei | Inhalt |
|-------|--------|
| `01_basis_rag.py` | Einfachstes RAG-Beispiel — Index aufbauen und befragen |
| `02_rag_mit_quellen.py` | RAG mit Quellenangaben — welcher Abschnitt lieferte die Antwort? |
| `beispiel_dokumente/` | Drei Beispiel-Protokolle zum Testen |

## Schnellstart

```bash
# Dokumente vorbereiten
# Entweder: eigene .txt/.md/.pdf Dateien in einen Ordner legen
# Oder: die Beispieldokumente nutzen

python3 01_basis_rag.py
```

## Datenschutz-Variante: Vollständig lokal

Standardmässig nutzen die Beispiele die Claude API für die Generierung.
Für vollständig lokalen Betrieb (kein Internet, keine API-Kosten):

1. Ollama starten mit einem lokalen Modell (siehe `01_lokale_modelle/`)
2. In den Skripten die llm-Konfiguration anpassen:

```python
from llama_index.llms.ollama import Ollama
llm = Ollama(model="llama3.2", request_timeout=60.0)
```

Dann verlässt kein einziges Byte deiner Dokumente den Rechner.

## Fine-Tuning vs. RAG — wann was?

| | RAG | Fine-Tuning |
|---|-----|------------|
| Eigene Dokumente abfragen | ✅ Ideal | ❌ Falsch |
| Dokumentenstand aktuell halten | ✅ Sofort | ❌ Neutraining nötig |
| Quellenangaben | ✅ Möglich | ❌ Nicht möglich |
| Schreibstil anlernen | ❌ Nicht ideal | ✅ Besser |
| Aufwand | Niedrig | Hoch |
| Kosten | Gering | Hoch |
