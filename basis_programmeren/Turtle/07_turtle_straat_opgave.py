from random import randint
import turtle as turtle
from utils.usefull_functions import teken_huis

COORDINATEN = [(0,0), (150, 0), (300, 0)]
AANTAL_COORDINATEN = 2

# teken_huis(100)

def teken_straat(coordinaten):
    for coor in coordinaten:
        print("coordinaat : ",coor)
        teken_huis(100, coor)

# teken_straat(COORDINATEN)


coordinaten = []

for x in range(AANTAL_COORDINATEN):
    coordinaten.append((randint(-200, 200), 0))

print(coordinaten)
letters ="abc"

# for coord_a in coordinaten:
#     print("///////////////////")
#     for coord_b in coordinaten:
#         print("-------------------------")
#         # x-waarde van coord_a
#         print("a_x : ", coord_a[0])
#         # y-waarde van coord_a
#         print("a_y : ", coord_a[1])
#         # x-waarde van coord_b
#         print("b_x : ", coord_b[0])
#         # y-waarde van coord_b
#         print("b_y : ", coord_b[1])

# for A in range(3):
#     for B in letters:
#         print(A, "-", B)

# print(coordinaten)

# # we voegen random coordinaten toe aan de lijst
for x in range(AANTAL_COORDINATEN*3):
    coordinaten.append((randint(-200, 200), 0))

# print(coordinaten)

nieuw_punt = ((randint(-200, 200), 0))
# print(nieuw_punt)
# teken_huis(100, nieuw_punt)

# # Dit is niet de enige manier. Het kn waarschijnlijk eenvoudiger. Maar het geeft een mogelijkheid om te vergelijken of 2 huizen met elkaar overlappen langs links van het nieuwe punt
# # je zal in dit geval ook moeten checken of ze lans de andere kant overlappen
# # wanneer 2 punten overlappen moet je het niet toevoegen (append) aan de "list" -- anders wel
# # Er zijn ook andere manieren om te checken of ze overlappen
for coord in coordinaten:
    if nieuw_punt[0] < coord[0] or nieuw_punt[0] > coord[0] + 100:
#         # tekenen moet je niet doen. Dit dient enkel om te visueel na te gaan of de 2 huizen inderdaad langs deze kant overlappen
#         # In je functie zal je enkel nakijken of de 2 punten in de lijst overlappen en zal je de lijst bouwen.
#         # Daarna zal je de gemaakte lijst gebruiken om de huizen te tekenen
        teken_huis(100, coord)
#         print(f"het punt {coord} raakt ons (nieuw_punt) huis ({nieuw_punt}) langs rechts ")
    

# # In een mogelijke oplossing zal je een punt toevoegen aan de lijst wanneer het niet overlapt met de punten in de lijst. 
# # Wanneer het wel overlapt maak je een nieuw random punt.

turtle.done()