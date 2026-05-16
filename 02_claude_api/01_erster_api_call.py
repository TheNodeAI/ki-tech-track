"""
Erster API-Call mit Claude.
Sendet einen Text und bekommt eine Zusammenfassung zurück.

Voraussetzung:
    export ANTHROPIC_API_KEY="dein-key"
    pip install anthropic
"""

import anthropic
import os


def main():
    # Client initialisieren — Key kommt aus Umgebungsvariable
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    # Beispieltext — ersetze das durch deinen eigenen Text
    beispieltext = """
    Das Meeting heute hat folgendes ergeben: Wir werden das Projekt um zwei Wochen
    verschieben. Der Hauptgrund ist, dass das Design-Team noch ausstehende Punkte
    klären muss. Thomas übernimmt die Koordination mit dem Kunden und informiert
    bis Freitag über den neuen Zeitplan. Alle anderen Aufgaben bleiben unverändert.
    Das nächste Meeting ist in zwei Wochen.
    """

    # API-Call
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": f"Fasse folgenden Text in drei Sätzen zusammen:\n\n{beispieltext}"
            }
        ]
    )

    # Antwort ausgeben
    print("Zusammenfassung:")
    print(response.content[0].text)

    # Token-Verbrauch anzeigen
    print(f"\nVerbrauchte Tokens: {response.usage.input_tokens} Input, {response.usage.output_tokens} Output")


if __name__ == "__main__":
    main()
