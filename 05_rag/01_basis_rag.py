"""
Einfachstes RAG-Beispiel.

Lädt Dokumente aus einem Ordner, baut einen Index auf
und beantwortet Fragen auf Basis dieser Dokumente.

Voraussetzung:
    export ANTHROPIC_API_KEY="dein-key"
    pip install llama-index llama-index-llms-anthropic llama-index-embeddings-huggingface

Erster Start: lädt automatisch ein Embedding-Modell (~100 MB).
"""

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


def index_aufbauen(dokumente_ordner: str):
    """Index aus Dokumenten in einem Ordner aufbauen."""
    print(f"Lade Dokumente aus: {dokumente_ordner}")
    documents = SimpleDirectoryReader(dokumente_ordner).load_data()
    print(f"{len(documents)} Dokument(e) geladen.")

    print("Baue Index auf (berechne Embeddings)...")
    index = VectorStoreIndex.from_documents(documents)
    print("Index fertig.")
    return index


def main():
    # --- Konfiguration ---

    # Ordner mit eigenen Dokumenten — anpassen
    dokumente_ordner = "./beispiel_dokumente"

    # Sprachmodell für die Generierung
    Settings.llm = Anthropic(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    # Lokales Embedding-Modell (kein API-Key nötig)
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    # --- Index aufbauen ---
    index = index_aufbauen(dokumente_ordner)
    query_engine = index.as_query_engine()

    # --- Fragen stellen ---
    print("\n" + "="*50)
    print("Index bereit. Stelle Fragen zu deinen Dokumenten.")
    print("Tippe 'exit' zum Beenden.")
    print("="*50 + "\n")

    while True:
        frage = input("Frage: ").strip()

        if not frage:
            continue

        if frage.lower() == "exit":
            break

        print("\nSuche relevante Abschnitte...")
        antwort = query_engine.query(frage)
        print(f"\nAntwort:\n{antwort}\n")


if __name__ == "__main__":
    main()
