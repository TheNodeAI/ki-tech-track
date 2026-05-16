"""
RAG mit Quellenangaben.

Zeigt welche Dokument-Abschnitte für die Antwort genutzt wurden.
Wichtig für Vertrauen und Nachvollziehbarkeit.

Voraussetzung:
    export ANTHROPIC_API_KEY="dein-key"
    pip install llama-index llama-index-llms-anthropic llama-index-embeddings-huggingface
"""

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.response.schema import Response
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


def main():
    dokumente_ordner = "./beispiel_dokumente"

    # Konfiguration
    Settings.llm = Anthropic(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    # Dokumente laden und Index aufbauen
    print("Lade Dokumente und baue Index auf...")
    documents = SimpleDirectoryReader(dokumente_ordner).load_data()
    index = VectorStoreIndex.from_documents(documents)

    # Query Engine mit Quellenangaben
    query_engine = index.as_query_engine(
        similarity_top_k=3  # Top 3 relevante Abschnitte zurückgeben
    )

    print(f"\n{len(documents)} Dokument(e) geladen. Index bereit.")
    print("Tippe 'exit' zum Beenden.\n")

    while True:
        frage = input("Frage: ").strip()

        if not frage:
            continue
        if frage.lower() == "exit":
            break

        # Antwort holen
        antwort = query_engine.query(frage)

        print(f"\nAntwort:\n{antwort.response}\n")

        # Quellen anzeigen
        if antwort.source_nodes:
            print("Genutzte Quellen:")
            for i, node in enumerate(antwort.source_nodes, 1):
                datei = node.metadata.get("file_name", "Unbekannt")
                score = round(node.score, 3) if node.score else "—"
                vorschau = node.text[:150].replace("\n", " ") + "..."
                print(f"  [{i}] {datei} (Relevanz: {score})")
                print(f"      \"{vorschau}\"")
            print()


if __name__ == "__main__":
    main()
