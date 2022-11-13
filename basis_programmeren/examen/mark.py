import random
import time


while True:

   
#begin aantal punten
    aantal_punten = 0
    
# automatische keuze tussen computer of speler
    if random.randint(0, 1) == 0:
        aan_beurt = "speler1"
    else:
        aan_beurt = "computer"

    while aantal_punten < 21:

        print("Het huidige nummer is " + str(aantal_punten) + ".")
        print()

        if aan_beurt == "speler1":

            print("Voeg punten bij, de speler die boven 21 gaat verliest")

            keuze_speler = ""
            while keuze_speler not in ["1", "2", "3","4","5","6","7","8","9","10","11"]:
                keuze_speler = input("Hoeveel punten wil je erbij doen ")

            keuze_speler = int(keuze_speler)
            aantal_punten = aantal_punten + keuze_speler
            print()

            if aantal_punten > 21:
                print("Het aantal punten is  " + str(aantal_punten) + ".")
                print()
                print("Je bent verloren.")
                break
            aan_beurt = "computer"

        else:

            keuze_computer = random.randint(1, 11)
            aantal_punten = aantal_punten + keuze_computer
            print("De computer zijn beurt hij kiest " +
                  str(keuze_computer) + ".")
            print()
            time.sleep(1)

            if aantal_punten >= 21:
                print("Het aantal punten is = " + str(aantal_punten) + ".")
                print()
                print("Je hebt gewonnen !!!!!")
                break
            aan_beurt = "speler1"

    print()
    nog_een_spel = input("Wil je nog een spel spelen? ")
    if nog_een_spel.lower().startswith("j"):
        continue
    else:
        print("Tot ziens")
        break