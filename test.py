"""
Atrin Taghi Pour

"Galgenmännchen" Version 1.0
Test code
"""

# Test file, um zu sichern, dass alle Worte im Words.txt richtig gespeichert sind
import random

def words_reading(f):
    # Einlesen der Wörter aus der Datei und Erstellen eines Wörterbuchs
    word_dict = {}

    with open(f, "r") as file:
        lines = file.readlines()    # Die Datei öffnen und Zeile für Zeile lesen

    # Jede Zeile in zwei Teile durch " : " teilen und beides als Dictionary speichern
    for line in lines:
        line = line.strip()
        if line:
            word, pattern = line.split(" : ")
            word_dict[word] = pattern

    return word_dict


word_dict = words_reading("Words.txt")
print(word_dict)
for i in range(len(word_dict)):
    random_word = random.choice(list(word_dict.keys()))
    print("random word is: {}".format(random_word))
    # Das Wort mit Lücken in eine Liste umwandeln
    halb_wort = list(word_dict[random_word])
    print("Halb word is: {}".format(halb_wort))
    if len(halb_wort) != len(random_word):
        print("Fehler: Die Länge des halben Wortes stimmt nicht überein.")
        print(halb_wort, random_word)
    else:
        print("The word is correct")
