"""
KI-Assistent mit Gesprächsgedächtnis.

Interaktiver Chatbot der sich den Konversationsverlauf merkt
und auf frühere Nachrichten Bezug nehmen kann.

Starten:
    python3 assistent.py

Befehle:
    exit  → Beenden
    neu   → Neue Konversation starten

Anpassen:
    Ändere den system_prompt unten um das Verhalten des Assistenten anzupassen.
"""

import anthropic
import os


# --- Konfiguration ---

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Gesprächsgeschichte — wird bei jedem Call mitgeschickt
conversation_history = []

# System-Prompt — hier das Verhalten anpassen
system_prompt = """Du bist ein Assistent für interne Dokumentenarbeit.
Du hilfst dabei Berichte zu strukturieren, Kernaussagen zu extrahieren
und Protokolle zusammenzufassen.
Antworte immer auf Deutsch. Sei präzise und strukturiert. Keine Füllwörter."""


# --- Funktionen ---

def chat(user_message):
    """Einen Schritt in der Konversation durchführen."""
    # Nutzernachricht zur Geschichte hinzufügen
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # API-Call mit gesamter Konversationsgeschichte
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        max_tokens=2048,
        system=system_prompt,
        messages=conversation_history
    )

    # Antwort zur Geschichte hinzufügen
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    print("Assistent gestartet.")
    print("Befehle: 'exit' zum Beenden, 'neu' für neue Konversation.")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nDu: ").strip()

            # Leere Eingabe überspringen
            if not user_input:
                continue

            # Beenden
            if user_input.lower() == "exit":
                print("Beendet.")
                break

            # Neue Konversation
            if user_input.lower() == "neu":
                conversation_history.clear()
                print("Neue Konversation gestartet.")
                continue

            # Antwort holen und ausgeben
            response = chat(user_input)
            print(f"\nAssistent: {response}")

        except KeyboardInterrupt:
            print("\nBeendet.")
            break


if __name__ == "__main__":
    main()
