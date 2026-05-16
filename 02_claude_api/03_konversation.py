"""
Mehrstufige Konversation mit Gesprächsgedächtnis.

Das Modell hat kein eigenes Gedächtnis zwischen Calls.
Wir simulieren Gedächtnis indem wir die gesamte Konversationsgeschichte
bei jedem Call mitschicken.

Dieses Beispiel zeigt das Grundprinzip — der vollständige Chatbot
ist in 04_chatbot/assistent.py zu finden.
"""

import anthropic
import os


def main():
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    system_prompt = """Du bist ein Assistent für interne Dokumentenarbeit.
Du hilfst dabei Berichte zu strukturieren und Protokolle zusammenzufassen.
Antworte auf Deutsch. Sei präzise."""

    # Gesprächsgeschichte — startet leer, wächst mit jedem Schritt
    history = []

    print("Mehrstufige Konversation — drei Schritte\n")

    # --- Schritt 1 ---
    nachricht_1 = "Ich habe ein Meeting-Protokoll mit diesen Punkten: Projektstart verschoben, neuer Termin in 2 Wochen, Thomas koordiniert Kundenkommunikation."
    history.append({"role": "user", "content": nachricht_1})

    response_1 = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=system_prompt,
        messages=history
    )
    antwort_1 = response_1.content[0].text
    history.append({"role": "assistant", "content": antwort_1})

    print(f"Du: {nachricht_1}")
    print(f"Assistent: {antwort_1}\n")

    # --- Schritt 2 (bezieht sich auf Schritt 1) ---
    nachricht_2 = "Wer ist für die Kundenkommunikation zuständig?"
    history.append({"role": "user", "content": nachricht_2})

    response_2 = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=system_prompt,
        messages=history  # gesamte Geschichte wird mitgeschickt
    )
    antwort_2 = response_2.content[0].text
    history.append({"role": "assistant", "content": antwort_2})

    print(f"Du: {nachricht_2}")
    print(f"Assistent: {antwort_2}\n")

    # --- Schritt 3 ---
    nachricht_3 = "Schreibe eine kurze Follow-up E-Mail an Thomas mit den wichtigsten Punkten."
    history.append({"role": "user", "content": nachricht_3})

    response_3 = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=system_prompt,
        messages=history
    )
    antwort_3 = response_3.content[0].text

    print(f"Du: {nachricht_3}")
    print(f"Assistent: {antwort_3}\n")

    print(f"--- Gesprächsschritte: {len(history) // 2} ---")


if __name__ == "__main__":
    main()
