"""
System-Prompts verwenden.

Ein System-Prompt definiert das grundsätzliche Verhalten des Modells —
Ton, Sprache, Aufgabe, Einschränkungen.
Derselbe User-Input liefert je nach System-Prompt völlig unterschiedliche Ergebnisse.

Dieses Beispiel zeigt drei verschiedene System-Prompts für dieselbe Aufgabe.
"""

import anthropic
import os


def api_call(client, system_prompt, user_message):
    """Hilfsfunktion für einen API-Call mit System-Prompt."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Modellname prüfen: docs.anthropic.com/models
        max_tokens=512,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.content[0].text


def main():
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    # Eingabe — dieselbe für alle drei Varianten
    eingabe = "Unser neues Produkt ist jetzt verfügbar. Es hat viele tolle Funktionen."

    # --- Variante 1: Professionell und knapp ---
    system_professionell = """Du bist ein Business-Kommunikations-Assistent.
Formuliere Texte professionell, direkt und ohne Füllwörter.
Kein Marketing-Sprech. Antworte auf Deutsch."""

    print("=== Variante 1: Professionell ===")
    print(api_call(client, system_professionell, f"Verbessere diesen Text: {eingabe}"))
    print()

    # --- Variante 2: Für Social Media ---
    system_social = """Du bist ein Social-Media-Texter.
Schreibe kurz, prägnant und mit einem klaren Hook in der ersten Zeile.
Kein Hashtag-Spam. Maximale Länge: 3 Sätze. Antworte auf Deutsch."""

    print("=== Variante 2: Social Media ===")
    print(api_call(client, system_social, f"Schreibe einen Post für: {eingabe}"))
    print()

    # --- Variante 3: Strukturierte Analyse ---
    system_analyse = """Du bist ein kritischer Analyst.
Bewerte Texte sachlich und weise auf Schwächen hin.
Strukturiere deine Antwort mit Stichpunkten. Antworte auf Deutsch."""

    print("=== Variante 3: Kritische Analyse ===")
    print(api_call(client, system_analyse, f"Analysiere diesen Text: {eingabe}"))


if __name__ == "__main__":
    main()
