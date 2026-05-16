"""
Erster API-Call mit OpenAI.

Identisches Ergebnis wie 02_claude_api/01_erster_api_call.py —
nur mit OpenAI-Bibliothek und anderem Modell.

Voraussetzung:
    export OPENAI_API_KEY="dein-key"
    pip install openai
"""

from openai import OpenAI
import os


def main():
    # Client initialisieren
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Beispieltext
    beispieltext = """
    Das Meeting heute hat folgendes ergeben: Wir werden das Projekt um zwei Wochen
    verschieben. Der Hauptgrund ist, dass das Design-Team noch ausstehende Punkte
    klären muss. Thomas übernimmt die Koordination mit dem Kunden und informiert
    bis Freitag über den neuen Zeitplan. Alle anderen Aufgaben bleiben unverändert.
    Das nächste Meeting ist in zwei Wochen.
    """

    # API-Call
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Modellname prüfen: platform.openai.com/docs/models
        max_tokens=512,
        messages=[
            {
                "role": "system",
                "content": "Du bist ein präziser Assistent. Antworte auf Deutsch."
            },
            {
                "role": "user",
                "content": f"Fasse folgenden Text in drei Sätzen zusammen:\n\n{beispieltext}"
            }
        ]
    )

    # Antwort ausgeben
    print("Zusammenfassung:")
    print(response.choices[0].message.content)

    # Token-Verbrauch
    print(f"\nVerbrauchte Tokens: {response.usage.prompt_tokens} Input, {response.usage.completion_tokens} Output")


if __name__ == "__main__":
    main()
