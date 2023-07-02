# Galgenmännchen Version 2.0 (GUI)

Autor: Atrin Taghi Pour
Klasse: 10A1
GLN Aufgabe 2
Datum: 27.06.2023
Version 2.0 (GUI)

## Beschreibung

Dieser Code implementiert das Spiel "Galgenmännchen" mit einer grafischen Benutzeroberfläche (GUI) mithilfe der Tkinter-Bibliothek. Das Spiel wählt zufällig ein Wort aus einem Wörterbuch aus und fordert den Spieler heraus, das Wort zu erraten, indem er einzelne Buchstaben rät. Der Spieler hat insgesamt 10 Versuche, um das Wort richtig zu erraten. Das Spiel enthält auch die Möglichkeit, einen Hinweis abzurufen. Der Punktestand des Spielers wird verfolgt und am Ende des Spiels angezeigt.


## Dateien

- `galgenmaennchen_V2.py`: Die Hauptprogrammdatei.
- `Words.txt`: Eine Datei mit der Liste der Wörter, die im Spiel verwendet werden sollen.
- `hints.txt`: Eine Datei mit Hinweisen für jedes Wort im Spiel.
- `test.py` : Eine Programmdatei für die Übereinstimmung jedes Worts mit jeweiligem halb_wort


Verwendung:
1. Starten Sie das Spiel, indem Sie den Code ausführen.
Sie können das Program auch durch dem Command ausführen:

'''
python3 Galgenmaennchen_V2.py
'''

2. Ein Fenster mit dem Titel "Galgenmännchen Spiel" wird geöffnet.

3. Geben Sie Buchstaben in das Eingabefeld "Buchstabe raten" ein und klicken Sie auf die Schaltfläche "Buchstabe raten", um Ihren Tipp abzugeben.

4. Sie können auch auf die Schaltfläche "Hinweis" klicken, um einen Hinweis für das aktuelle Wort zu erhalten.

5. Das Spiel aktualisiert das Wortlabel, zeigt den Fortschritt beim Raten des Wortes an und zeichnet das Galgenmännchen entsprechend den falschen Versuchen.

6. Wenn Sie das Spiel beenden möchten, klicken Sie auf die Schaltfläche "Spiel beenden".

7. Nach dem Ende des Spiels wird eine MessageBox mit Ihrem Punktestand angezeigt.


## Besondere Vorteile von Code:
- Sie können einfach die Worte und Hinweise durch Änderungen bei txt Dateien ändern und dann durch das text.py Programm sicherstellen, dass die Worte zusammen passen

- Das Programm ist Client-orientiert aufgebaut, so alles wird erklärt und das Programm wird so lange Worte aussuchen, so es kein Wort mehr gibt.

- Das Programm ist mit Variable und Funktionen geschrieben, so dass es eine eifache Anpassung ermöglicht.

- An jeder Stelle im Spiel gibt es "quit" Möglichkeit

- Das Code ist kommentiert

## weitere mögliche Erweiterungen:

- Die Worte anhand von Themen zuordnen und teilen

- Die Worte anhand von Schwierigkeit beim Ratten ordnen

- Die nicht im Wort vorhandene Buchstabe als Hinweis
