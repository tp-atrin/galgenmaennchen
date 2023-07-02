"""
Atrin Taghi Pour
Klasse 10A1
Aufgabe 2 des GLNs
27.06.2023
"Galgenmännchen" Version 2.0
Der Hauptcode 
"""

import tkinter as tk            # Die Library tkinter importieren, um GUI zu haben
from tkinter import messagebox
import random

word_dict = {}  
hint_dict = {}
score = 0
wort = ""
halb_wort = []
versuche = 0

def words_reading(f):   #Die Words.txt und hints.txt lesen
    word_dict = {}

    with open(f, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line:
            word, pattern = line.split(" : ")#Die Worte und hints in zwei Teile teilen
            word_dict[word] = pattern

    return word_dict #als dictionary speichern

def update_word_label(): #Die halb_Word aktualisieren
    if word_dict:
        global wort #Wort globalisieren, damit das nutzen zu koennen
        wort = random.choice(list(word_dict.keys()))
        hint_word = hint_dict[wort]
        global halb_wort
        halb_wort = list(word_dict[wort])

        word_label.configure(text="".join(halb_wort))
    else:
        end_game()

def guess_letter():
    global wort
    global halb_wort
    global versuche
    global score

    guess = guess_entry.get().upper()
    guess_entry.delete(0, tk.END)

    if guess == "QUIT": #Wenn die Eingabe "QUIT" ist
        quit_game()
    elif guess == "HINT":#Wenn die Eingabe "HINT" ist
        messagebox.showinfo("Hinweis", hint_word)
    elif len(guess) == 1 and guess.isalpha():   #Wenn die Eingabe Buchstabe ist
        if guess in wort:   #Die Buchstabe vorhanden im Wort
            indices = [i for i, letter in enumerate(wort) if letter == guess]
            for index in indices:
                if halb_wort[index] != guess:
                    halb_wort[index] = guess

            word_label.configure(text="".join(halb_wort))

            if halb_wort == list(wort): #Wenn alle Buchstaben richtig geratten worden sind
                score += 1
                score_label.configure(text="Gesamtpunkte: {}".format(score))
                messagebox.showinfo("Gewonnen!", "Du hast das Wort richtig geraten!")
                update_word_label()
                versuche = 0 #Die Versuche nochmal fuer das neue Wort 0 machen
                versuche_label.configure(text="Versuche: {}/10".format(versuche))
        else:   # Wenn das Buchstabe nicht im WOrt vorhanden ist
            versuche += 1   
            versuche_label.configure(text="Versuche: {}/10".format(versuche))
            draw_hangman(canvas, versuche) #Galgenmaennchen vervollstaendigen
            if versuche == 10: #Wenn die Versuche ueberschritten sind
                score -= 1
                score_label.configure(text="Gesamtpunkte: {}".format(score))
                messagebox.showinfo("Verloren!", "Du hast das Wort nicht rechtzeitig geraten!")
                update_word_label()
                versuche = 0
                versuche_label.configure(text="Versuche: {}/10".format(versuche))
                clear_hangman(canvas) #Der Galgenmaennchen loeschen

    else:
        messagebox.showinfo("Ungültige Eingabe!", "Bitte gib nur einzelne Buchstaben ein.")

def quit_game():
    messagebox.showinfo("Spiel beendet", "Dein Punktestand: {}".format(score))
    window.destroy()

def end_game():
    messagebox.showinfo("Spiel beendet", "Dein Punktestand: {}".format(score))
    quit_game()

def draw_hangman(canvas, versuche): #Funktion, um Galgenmaennchen zu zeichnen
    if versuche >= 1:
        canvas.create_line(50, 250, 200, 250, width=5)  # Boden
    if versuche >= 2:
        canvas.create_line(125, 250, 125, 50, width=5)  # Pfosten
    if versuche >= 3:
        canvas.create_line(125, 50, 200, 50, width=5)  # Querbalken
    if versuche >= 4:
        canvas.create_line(200, 50, 200, 80, width=5)  # Seil
    if versuche >= 5:
        canvas.create_oval(180, 80, 220, 120, width=5)  # Kopf
    if versuche >= 6:
        canvas.create_line(200, 120, 200, 200, width=5)  # Körper
    if versuche >= 7:
        canvas.create_line(200, 140, 180, 160, width=5)  # Linker Arm
    if versuche >= 8:
        canvas.create_line(200, 140, 220, 160, width=5)  # Rechter Arm
    if versuche >= 9:
        canvas.create_line(200, 200, 180, 220, width=5)  # Linkes Bein
    if versuche >= 10:
        canvas.create_line(200, 200, 220, 220, width=5)  # Rechtes Bein

def clear_hangman(canvas):
    canvas.delete("all")

window = tk.Tk()
window.title("Galgenmännchen Spiel")

word_dict = words_reading("Words.txt")  #Worte lesen un dspeichern
hint_dict = words_reading("hints.txt")  #Hints lesen un dspeichern

word_label = tk.Label(window, text="")
word_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

guess_button = tk.Button(window, text="Buchstabe raten", command=guess_letter) 
#Das Taste "Buchstabe raten" mit Funktion "guess_letter" verbunden
guess_button.pack()

hint_button = tk.Button(window, text="Hinweis", command=lambda: messagebox.showinfo("Hinweis", hint_dict[wort]))
#Das Taste "Hinweis" mit jeweilige Hinwies verbunden
hint_button.pack()

versuche_label = tk.Label(window, text="Versuche: {}/10".format(versuche))
versuche_label.pack()

score_label = tk.Label(window, text="Gesamtpunkte: {}".format(score))
score_label.pack()

quit_button = tk.Button(window, text="Spiel beenden", command=quit_game)
#Das Taste "Spiel beenden" mit Funktion "quit_game" verbunden
quit_button.pack()

canvas = tk.Canvas(window, width=250, height=300) #Die Window erstellen
canvas.pack()

update_word_label() 

window.mainloop()
