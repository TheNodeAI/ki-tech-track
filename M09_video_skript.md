# M09 — Lokale KI: Vollständiges Video-Skript (L1–L3)

Der technische Deep-Dive (APIs, Python, RAG) ist im GitHub-Repository:
github.com/[dein-nutzername]/ki-tech-track

---

## Lektion 1: Warum lokale KI?

### HOOK

Thomas hat in M08 eine Frage gestellt die er nicht vollständig beantwortet hat:
Was passiert mit den Daten die er an die Claude API schickt? Er hat seinen
E-Mail-Workflow anonymisiert — aber er fragt sich: Geht das auch ohne Cloud?

Was passiert wenn sein Arbeitgeber Cloud-KI aus Datenschutzgründen einschränkt?
Was wenn er Dokumente verarbeiten will die seinen Rechner wirklich nicht verlassen
dürfen? Was wenn er verstehen will wie das alles unter der Haube funktioniert?

Dann braucht er das hier.

### INHALT

Direkt an M08 anknüpfend: Thomas hat gelernt wie er KI in Workflows einbindet.
In diesem Modul gehen wir den nächsten Schritt: KI vollständig lokal betreiben,
eigene API-Calls bauen, eigene Anwendungen schreiben.

**Was "lokale KI" konkret bedeutet**

Wenn du ein Modell lokal betreibst, läuft die KI-Inferenz vollständig auf deiner
eigenen Hardware. Kein Text verlässt deinen Rechner. Kein API-Call geht nach aussen.
Du kannst offline sein. Du hast volle Kontrolle.

Das klingt nach einer klaren Verbesserung. Aber es gibt drei Einschränkungen die ich
direkt ansprechen will.

Erstens: Qualität. Die besten Cloud-Modelle sind erheblich leistungsfähiger als
was lokal läuft. Lokale Modelle sind gut — aber für komplexe Analysen schneiden
sie meistens schlechter ab.

Zweitens: Hardware-Anforderungen. Ein 7B-Modell braucht 8 GB RAM.
Darunter wird es langsam bis unbenutzbar.

Drittens: Einrichtungsaufwand. Cloud-KI ist sofort verfügbar.
Lokale KI braucht Installation und Konfiguration.

**Wann lokale Modelle sinnvoll sind**

Datenschutz: Wenn vertrauliche Dokumente keinen externen Server berühren dürfen.
Offline-Nutzung: Auf Reisen oder in schlecht verbundenen Umgebungen.
Hohe Volumen: Täglich tausende einfacher Anfragen ohne API-Kosten.
Technisches Verständnis: Wer verstehen will wie es funktioniert.

**Kosten: lokal vs. Cloud**

| Anwendungsfall | Cloud (Haiku) | Lokal (Ollama) |
|---------------|--------------|----------------|
| 1.000 Klassifizierungen | ca. 0.50–1.00 USD | 0 USD |
| 10.000 Zusammenfassungen | ca. 5–15 USD | 0 USD |
| 100.000 einfache Anfragen | ca. 50–150 USD | 0 USD |

Für gelegentliche Nutzung ist Cloud günstiger — kein Setup.
Ab regelmässig hohem Volumen rechnet sich lokal schnell.

**Wann du besser bei Cloud-APIs bleibst**

Für komplexe qualitätskritische Aufgaben. Wenn dein Rechner weniger als 8 GB RAM hat.
Wenn du schnell Ergebnisse brauchst ohne Einrichtungsaufwand.

**Wo der technische Deep-Dive zu finden ist**

APIs, Python-Code, eigene Anwendungen bauen, RAG — das ist im begleitenden
GitHub-Repository: github.com/[dein-nutzername]/ki-tech-track

Hier in den Video-Lektionen zeigen wir Ollama und LM Studio als Screencast.
Der Rest ist Dokumentation und Code zum selbst Durcharbeiten.

### ACTION BRIDGE

Identifiziere eine Aufgabe für die du normalerweise Cloud-KI nutzt —
aber bei der du dir wünschst dass die Daten deinen Rechner nicht verlassen.
Das ist dein persönlicher Anwendungsfall für die nächsten zwei Lektionen.

### CLIFFHANGER

In der nächsten Lektion zeige ich live: Ollama installieren, ein Modell laden,
erste Antwort erhalten — in unter 15 Minuten. Für Mac, Windows und Linux.

---

## Lektion 2: Ollama — lokale Modelle in 15 Minuten

### HOOK

In 15 Minuten läuft ein KI-Modell auf deinem Laptop — ohne Internet, ohne Abo,
ohne Datenschutzbedenken. Das Versprechen halte ich.

Ollama macht das Betreiben lokaler Modelle so einfach wie möglich.
Installation, Modell laden, loslegen.

### INHALT

**[SCREENCAST BEGINNT]**

Ollama ist ein Open-Source-Tool das grosse Sprachmodelle lokal verwaltet.
Es läuft im Hintergrund und stellt eine einheitliche Schnittstelle bereit.

Thomas' Anwendungsfall: Er will seine internen Protokolle zusammenfassen ohne
den Text in ChatGPT einzufügen. Mit Ollama verlässt der Text seinen Rechner nie.

**Installation**

[ZEIGEN: ollama.com im Browser]

Mac: Installer herunterladen, ausführen. Ollama erscheint als Hintergrundprozess.
Linux: `curl -fsSL https://ollama.com/install.sh | sh`
Windows: Windows-Installer von ollama.com

**Erstes Modell laden**

[ZEIGEN: Terminal öffnen]

```
ollama pull llama3.2
```

Das lädt das Modell herunter — einige Minuten je nach Verbindung.

[ZEIGEN: Download-Fortschritt]

Aktuelle Modellempfehlungen auf ollama.com/library — dort ändert sich die
Liste regelmässig. Als Orientierung: 3B für den Einstieg, 7B für bessere Qualität.

**Modell starten**

```
ollama run llama3.2
```

[ZEIGEN: Prompt erscheint]

Jetzt kannst du direkt tippen. Thomas gibt sein Protokoll ein und fragt nach
einer Zusammenfassung.

[ZEIGEN: Eingabe und Antwort]

Der Text verlässt den Rechner nicht. Keine API, kein Internet.

**Wichtige Befehle**

```
ollama list       # alle geladenen Modelle
ollama rm NAME    # Modell entfernen
ollama ps         # laufende Modelle
```

**OpenWebUI — Browser-Interface**

Für den täglichen Gebrauch ist ein Chat-Interface komfortabler.
OpenWebUI gibt Ollama eine ChatGPT-ähnliche Oberfläche — vollständig lokal.

[ZEIGEN: OpenWebUI Interface im Browser unter localhost:3000]

Installation über Docker (Befehl im GitHub-Repository unter 01_lokale_modelle/).

**[SCREENCAST ENDET]**

**RAM-Richtwerte**

| Modellgrösse | RAM-Bedarf | Empfehlung |
|-------------|-----------|------------|
| 3B | ~4 GB | Schneller Einstieg |
| 7B | ~8 GB | Gute Qualität |
| 13B | ~16 GB | Sehr gut, langsamer |

### ACTION BRIDGE

Installiere Ollama heute und lade ein Modell. Teste die Aufgabe die du in
Lektion 1 identifiziert hast. Wie gut schlägt sich das lokale Modell —
und wie vergleicht es sich mit dem Cloud-Modell das du sonst nutzt?

### CLIFFHANGER

Ollama ist terminal-orientiert. Wer eine grafische Oberfläche bevorzugt
ohne Docker — dafür gibt es LM Studio. Das schauen wir uns als nächstes an.
Und ich zeige dir dabei ein Feature das für alle interessant ist die eigene
Workflows testen wollen.

---

## Lektion 3: LM Studio — GUI und lokaler API-Server

### HOOK

LM Studio ist mehr als eine grafische Alternative zu Ollama. Es kann als
lokaler API-Server laufen der die OpenAI-Spezifikation nachbildet.

Das bedeutet: Jede Anwendung die für OpenAI gebaut wurde kann gegen ein
lokales Modell gerichtet werden — ohne eine Zeile Code zu ändern.

Für Thomas: Er kann seine n8n-Workflows aus M08 vollständig lokal testen
bevor er entscheidet ob er Cloud-APIs einbindet.

### INHALT

**[SCREENCAST BEGINNT]**

**Installation**

[ZEIGEN: lmstudio.ai im Browser]

Download für Mac/Windows/Linux — Standard-Installer ausführen.

**Modelle laden**

[ZEIGEN: LM Studio Suchinterface]

LM Studio durchsucht Hugging Face und zeigt verfügbare Modelle mit
Grösse und Anforderungen. Es empfiehlt automatisch was zu deiner Hardware passt.

[ZEIGEN: Modell laden]

**Chat-Interface**

[ZEIGEN: Chat-Tab]

Eingabefeld, Gesprächsverlauf, System-Prompt setzen.
Thomas lädt sein Protokoll ein und stellt Fragen.

**Der lokale API-Server**

Das ist das entscheidende Feature.

[ZEIGEN: "Local Server"-Tab]

Modell auswählen → Server starten.
LM Studio startet unter localhost:1234 und verhält sich wie die OpenAI API.

Du ersetzt in jedem Code der OpenAI nutzt einfach die base_url:

Von: https://api.openai.com/v1
Zu: http://localhost:1234/v1

[ZEIGEN: Python-Code im Editor, nur base_url Zeile ändern]

Der Rest des Codes bleibt identisch. Kein Internet, keine Kosten, keine Daten raus.

Thomas kann damit seinen n8n-Workflow lokal testen — in den Anthropic/OpenAI-Nodes
einfach auf localhost zeigen statt auf die Cloud.

**[SCREENCAST ENDET]**

**LM Studio vs. Ollama**

| | LM Studio | Ollama |
|---|-----------|--------|
| Oberfläche | GUI | Terminal |
| API-Server | Direkt eingebaut | Über n8n/Code |
| Modell-Discovery | Hugging Face Browser | ollama.com/library |
| Server-Betrieb | Desktop-App | systemd-Service möglich |

Beide sind valide Optionen. Viele haben beides installiert.

### ACTION BRIDGE

Installiere LM Studio, lade ein Modell und starte den lokalen API-Server.
Dann nimm einen der Python-Code-Beispiele aus dem GitHub-Repository
(03_openai_api/) und ändere nur die base_url auf localhost:1234.
Sieh ob das Ergebnis identisch ist.

### CLIFFHANGER

Du hast jetzt lokale Modelle laufen. Der nächste Schritt — APIs, eigene
Anwendungen, RAG — ist im GitHub-Repository dokumentiert mit fertigem Code
zum Durcharbeiten. Link in der Kursbeschreibung.

Für alle die tiefer einsteigen wollen: Das Repository enthält vier weitere
Kapitel mit vollständigem Code und Schritt-für-Schritt-Erklärungen.
Kein Video nötig — die Dokumentation ist eigenständig nutzbar.
