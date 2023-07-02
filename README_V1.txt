# Galgenmännchen Version 1.0

Autor: Atrin Taghi Pour
Klasse: 10A1
GLN Aufgabe 2
Datum: 27.06.2023
Version: 1.0

## Beschreibung

Dieses Programm implementiert das Spiel "Galgenmännchen". Es wählt zufällig ein Wort aus einem Wörterbuch aus und fordert den Spieler heraus, das Wort zu erraten, indem er einzelne Buchstaben rät. Der Spieler hat eine begrenzte Anzahl von Versuchen (10), um das Wort richtig zu erraten. Das Programm hält den Punktestand des Spielers fest und gibt bei Bedarf Hinweise.


## Dateien

- `galgenmaennchen_V1.py`: Die Hauptprogrammdatei.
- `intro.py`: Ein Modul mit Funktionen für die Spiel-Einführung.
- `Words.txt`: Eine Datei mit der Liste der Wörter, die im Spiel verwendet werden sollen.
- `hints.txt`: Eine Datei mit Hinweisen für jedes Wort im Spiel.
- `test.py` : Eine Programmdatei für die Übereinstimmung jedes Worts mit jeweiligem halb_wort

## Verwendung

1. Starten Sie das Programm.
Sie können das Program auch durch dem Command ausführen:

'''
python3 Galgenmaennchen_V1.py
'''

2. Befolgen Sie die auf dem Bildschirm angezeigten Anweisungen, um das Spiel zu spielen.

3. Raten Sie Buchstaben, um das versteckte Wort zu vervollständigen. Sie haben eine begrenzte Anzahl von Versuchen.

4. Wenn Sie das Spiel beenden möchten, geben Sie bei der Aufforderung zur Eingabe eines Buchstabens "Quit" ein.

5. Das Spiel zeigt das Ergebnis und Ihren aktuellen Punktestand an.

## Besondere Vorteile von Code:
- Sie können einfach die Worte und Hinweise durch Änderungen bei txt Dateien ändern und dann durch das text.py Programm sicherstellen, dass die Worte zusammen passen

- Das Programm ist Client-orientiert aufgebaut, so alles wird erklärt und das Programm wird so lange Worte aussuchen, so es kein Wort mehr gibt.

- Das Programm ist mit Variable und Funktionen geschrieben, so dass es eine eifache Anpassung ermöglicht.

- Die Worte werden von List gelöscht, so dass der Spieler keine wiederholende Worte erfahrt.

- An jeder Stelle im Spiel gibt es "quit" Möglichkeit

- Das Code ist kommentiert

## weitere mögliche Erweiterungen:

- Die Worte anhand von Themen zuordnen und teilen

- Die Worte anhand von Schwierigkeit beim Ratten ordnen

- Die nicht im Wort vorhandene Buchstabe als Hinweis
