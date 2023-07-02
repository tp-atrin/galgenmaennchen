"""
Atrin Taghi Pour
Klasse 10A1
Aufgabe 2 des GLNs
27.06.2023
"Galgenmännchen" Version 1.0
Der Hauptcode
"""


# -*- coding: utf-8 -*-
import random  			#Die library random importieren, um Worte zufaellig auszusuchen
from intro import *		#Die selbst geschriebene library intro importieren, um die Einleitung auszufuehren


def words_reading(f):
    # Einlesen der Wörter aus der Datei und Erstellen eines Wörterbuchs
    word_dict = {}

    with open(f, "r") as file:	
        lines = file.readlines()	#Die file oeffnen und Zeil zu Zeil lesen

    # Jede Zeil in zwei Teile durch " : " teilen und die beide als dictionary speichern
    for line in lines:
        line = line.strip()
        if line:
            word, pattern = line.split(" : ")
            word_dict[word] = pattern

    return word_dict


def main(words_dict, hint_dict):
    score = 0	# Zähler für richtige Wort-Vermutungen

    while len(words_dict) > 0:	#Eine  Schleife, bis der Nutzer raus gehen will oder die Worte fertigg sind
        # Zufälliges Wort aus dem Wörterbuch auswählen
        random_word = random.choice(list(words_dict.keys()))
        # Die Hint fuer das Wort speichern
        hint_word = hint_dict[random_word]
        # Das Wort mit Lücken in eine Liste umwandeln
        halb_wort = list(words_dict[random_word])
        if len(halb_wort) != len(random_word):
            print("Fehler: Die Länge des halben Wortes stimmt nicht überein.")
        print("".join(halb_wort))
        versuche = 0  # Zähler für falsche Versuche
        guessed_indices = []  # Liste, um die Indizes der korrekt geratenen Buchstaben zu speichern

        while True:
        	# Die Zustand des Nutzers checken
            if versuche >= 10:
                # Spieler hat das Spiel verloren
                print("""
                ####################
                --------------------
                Du hast verloren!
                :(    :(
                --------------------
                ####################

                Das richtige Wort war:
                {}
                """.format(random_word))
                score -= 1	# von Gesamtpunkt eins reduzieren
                print("Dein aktueller Punktestand: {}".format(score))
                break

            if halb_wort == list(random_word):
                # Spieler hat das Wort korrekt geraten
                score += 1	# Zu GEsamt Punkt eins hinzufuegen
                print("""
                ####################
                --------------------
                Du hast gewonnen!
                :)    :)
                --------------------
                ####################

                Das richtige Wort war:
                    ----------
                    |   {}   |
                    ----------
                """.format(random_word))
                print("Dein aktueller Punktestand: {}".format(score))
                break

            else:
            	#erratener Buchstabe bekommen 
                r_buchstabe = input("Gib bitte deinen geratenen Buchstaben ein ('Quit' zum Beenden ; 'Hint' zur Hilfe): ").upper()
                # Wenn die Buchstabe gleich "QUIT" ist, der Spiel beenden und die Gesamtpunkt zeigen
                if r_buchstabe == 'QUIT':
                    # Spiel beenden
                    print("Spiel beendet. Dein Punktestand: {}".format(score))
                    exit(0)
                # Wenn die Buchstabe gleich "HINT" ist, die Erklährung zeigen
                if r_buchstabe == 'HINT':
                	#TODO: die Hilfe zu zeigen
                	print("Die Erklährung des Wortes : " + hint_word)
                	print("Dein aktueller Fortschritt: {}".format("".join(halb_wort)))

                if r_buchstabe.isalpha() and len(r_buchstabe) == 1 and r_buchstabe != 'HINT' and r_buchstabe != 'QUIT': #Wenn die Eingabe eine Buchstabe ist
                    if r_buchstabe in random_word:
                        # Buchstabe ist im Wort enthalten
                        print("Der Buchstabe ist im Wort vorhanden.")
                        # Eine Liste der Indizes erstellen, an denen der geratene Buchstabe im Wort vorkommt
                        indices = [i for i, letter in enumerate(random_word) if letter == r_buchstabe]
                        for index in indices:
                            if index not in guessed_indices:
                            	# Überprüfen, ob der Index bereits geraten wurde
                                guessed_indices.append(index)
                                # Index zur Liste der geratenen Indizes hinzufügen
                                halb_wort[index] = r_buchstabe
                                # Das geratene Zeichen an der entsprechenden Stelle im halben Wort einfügen
                        print("Dein aktueller Fortschritt: {}".format("".join(halb_wort)))
                    else:
                        # Buchstabe ist nicht im Wort enthalten
                        versuche += 1
                        print("Der Buchstabe ist nicht im Wort enthalten")
                        print("Du hast jetzt {} von 10 Versuchen gemacht".format(versuche))
                        print("Dein aktueller Fortschritt: {}".format("".join(halb_wort)))
                elif r_buchstabe != 'HINT' and r_buchstabe != 'QUIT':
                    # Ungültige Eingabe
                    print("Ungültige Eingabe.")
                    print("Du hast jetzt {} von 10 Versuchen gemacht".format(versuche))
                    print("Dein aktueller Fortschritt: {}".format("".join(halb_wort)))

        # Entferne das geratene Wort aus dem Wörterbuch
        del words_dict[random_word]


if __name__ == "__main__":
	# Die Worte als ein Dictionary Variable speichern
    word_dict = words_reading("Words.txt")
    # Die Worterklährungen als ein Dictionary Variable speichern
    hint_dict = words_reading("hints.txt")
    # Die Einleitung ausfuehren
    einleitung(word_dict, hint_dict)
    # Die Hauptteil ausfuehren
    main(word_dict, hint_dict)
