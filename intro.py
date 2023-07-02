"""
Atrin Taghi Pour

"Galgenmännchen" Version 1.0
Der Einleitungscode
"""

from Galgenmaennchen_V1 import * #Das Hauptprogramm importieren



def einleitung(a, b):   #Die Einleitungsfunktion : führt die Einleitung aus
    print("""
    ----------------------------------
              WILLKOMMEN BEI
           Galgenmännchen Spiel
    ----------------------------------
    Bei Galgenmännchen sollst du die Lücken im Wort ausfüllen, sodass das Wort auf Deutsch eine Bedeutung hat.
    Wenn du einen richtigen Buchstaben eingibst, wird die entsprechende Lücke ausgefüllt.


    Aber wenn du einen Buchstaben eingibst, der nicht im Wort vorhanden ist, wird jedes Mal einer deiner 10 Versuche abgezogen!
    Also pass auf! Du hast nur 10 falsche Raten!
    
    Bei der Vermutung eines Worts bevor 10 Versuche bekommen Sie einen Gesamtpunkt.
    Bei der Überschreitung von 10 Versuche wird einen Punkt von Ihren Gesamtpunkt reduziert.
    Wenn Sie nicht mehr spielen wollen innerhalb des Spiels, geben Sie bitte "QUIT" ein.

    Hinwies: Die Umlaute werden so dargestellt:
                            Ö : OE
                            Ü : UE
                            Ä : AE
                            ß : SS

    Um das Spiel für Sie zu vereinfachen, Können Sie bei jedem Wort eine Hinweis, die das Wort erklärt.
    Das reicht, "Hint" zu tippen bei derEingabe der Vermutung der Buchstabe
    Bist du bereit, das Spiel zu starten und Spaß zu haben?
    * Wenn ja, gebe die Zahl "1" ein.
    * Wenn nein, gebe die Zahl "2" ein.
    """)

    while True:     # Prüfen, ob der Nutzer spielen will oder nicht
        ask = int(input("Bitte gib deine Auswahl ein: \n"))

        if ask == 2:            # Er will aufhören!
            print("""
            Danke für deine Zeit!
            Auf Wiedersehen
            """)
            exit(0)
        elif ask == 1:      # Er will spielen
            main(a, b)
            break
        else:
            print("Die Eingabe muss entweder 1 oder 2 sein.")   # Er hat "aus Versehen" eine falsche Eingabe gewählt
