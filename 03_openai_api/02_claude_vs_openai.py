"""
Direkter Vergleich: Claude Haiku vs. GPT-4o-mini.

Dieselbe Aufgabe, beide Anbieter, direkter Output-Vergleich.
Hilft dir zu entscheiden welcher Anbieter für deine Aufgabe besser passt.

Voraussetzung:
    export ANTHROPIC_API_KEY="dein-key"
    export OPENAI_API_KEY="dein-key"
    pip install anthropic openai
"""

import anthropic
import os
import time
from openai import OpenAI


def claude_call(text, aufgabe):
    """API-Call an Claude."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    start = time.time()

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        max_tokens=512,
        system="Du bist ein präziser Assistent. Antworte auf Deutsch.",
        messages=[{"role": "user", "content": f"{aufgabe}:\n\n{text}"}]
    )

    dauer = round(time.time() - start, 2)
    return response.content[0].text, dauer


def openai_call(text, aufgabe):
    """API-Call an OpenAI."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    start = time.time()

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Modellname prüfen: platform.openai.com/docs/models
        max_tokens=512,
        messages=[
            {"role": "system", "content": "Du bist ein präziser Assistent. Antworte auf Deutsch."},
            {"role": "user", "content": f"{aufgabe}:\n\n{text}"}
        ]
    )

    dauer = round(time.time() - start, 2)
    return response.choices[0].message.content, dauer


def vergleich(text, aufgabe):
    """Beide Modelle vergleichen."""
    print(f"\n{'='*60}")
    print(f"AUFGABE: {aufgabe}")
    print(f"{'='*60}")

    print("\n--- Claude Haiku ---")
    claude_antwort, claude_dauer = claude_call(text, aufgabe)
    print(claude_antwort)
    print(f"(Dauer: {claude_dauer}s)")

    print("\n--- GPT-4o Mini ---")
    openai_antwort, openai_dauer = openai_call(text, aufgabe)
    print(openai_antwort)
    print(f"(Dauer: {openai_dauer}s)")


def main():
    # Beispieltext — durch eigenen Text ersetzen
    beispieltext = """
    Das Q3-Review hat folgende Erkenntnisse gebracht: Die Kundenzufriedenheit
    ist um 12% gestiegen, hauptsächlich durch schnellere Reaktionszeiten.
    Gleichzeitig sind die Supportkosten um 8% gesunken. Das neue Onboarding-
    Prozess wird von 78% der neuen Kunden positiv bewertet. Verbesserungsbedarf
    besteht bei der Dokumentation — 34% der Anfragen betreffen Themen die
    eigentlich in der Wissensdatenbank abgedeckt sein sollten.
    """

    # Teste verschiedene Aufgaben
    vergleich(beispieltext, "Fasse in drei Sätzen zusammen")
    vergleich(beispieltext, "Extrahiere die wichtigsten Zahlen als Stichpunkte")
    vergleich(beispieltext, "Formuliere zwei konkrete nächste Schritte basierend auf diesen Daten")


if __name__ == "__main__":
    main()
