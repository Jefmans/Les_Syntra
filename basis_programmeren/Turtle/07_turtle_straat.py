from random import randint
import turtle as turtle
import math, random
from utils.usefull_functions import teken_huis

turtle.shape("turtle")

def distance_between_points(point_1, point_2):
    som_kwadraten = math.pow((point_2[0]-point_1[0]), 2) + math.pow((point_2[1]-point_1[1]), 2)
    # print(som_kwadraten)
    return math.sqrt(som_kwadraten)

def hoogte_gelijkbenige_driehoek(lengte):
    # stelling van pythagoras -- middelijn staat loodrecht
    return math.sqrt(math.pow(lengte,2) - math.pow(lengte/2, 2))

# middelpunt van een huis is de hoogte van de driehoek + hoogte van het vierkant
# dat delen door 2
# 
# voor de breedte geldt de helft van de lengte.
#  
# We willen een lijst bijhouden van de middelpunten van de huizen en de bijhorende straal (verder weggelegen huizen zullen kleiner zijn)
# 
# Voor nu zetten we de huizen op 1 rij => dus is enkel de breedte voldoende om ervoor te zorgen dat ze niet overlappen 


def is_punt_in_cirkel(punt, middelpunt_cirkel, straal):
    return distance_between_points(punt, middelpunt_cirkel) < straal

def direction_vector(punt_1, punt_2):
    radians = math.atan2((punt_2[1]-punt_1[1]), (punt_2[0]-punt_1[0]))
    return math.degrees(radians)

punt = (0, 0)
middelpunt_cirkel = (50, (hoogte_gelijkbenige_driehoek(100)+100)/2)
heading = direction_vector(punt, middelpunt_cirkel)
start_punt = (random.randint(-200, 200), random.randint(-200, 200))


def genereer_huizen(aantal, start_punt, lengte):
    straal = (hoogte_gelijkbenige_driehoek(lengte)+lengte)/2
    middelpunten = [start_punt]
    print(middelpunten)
    print("------- start : ", start_punt)
    for n in range(aantal-1):
        print("-------- n --------- : ", n)
        nieuw_punt = (random.randint(-200, 200), random.randint(-200, 200))
        point_added = False
        while not point_added:
            print("+++++++ ++ +++++", nieuw_punt)
            for x in middelpunten:
                print(f"{nieuw_punt} in cirkel van {x}: ", is_punt_in_cirkel(nieuw_punt, x, 2.5*straal))
                if is_punt_in_cirkel(nieuw_punt, x, 2.5*straal):
                    print("----A----")
                    nieuw_punt = (randint(-200, 200), randint(-200, 200))
                    print("======== BREAK ========")
                    point_added = False
                    break                    
                else:
                    point_added = True
            if point_added:                
                middelpunten.append(nieuw_punt)
                point_added = True
                print("::::::: ADDED ::::::::::")
                
                    
            print(middelpunten)                
            
                    
    return middelpunten

huizen = genereer_huizen(8, start_punt, 50)

# afstand tussen middelpunt en hoekpunt_huis
straal_2 = distance_between_points(punt, middelpunt_cirkel)


for middelpunt in huizen:
    turtle.up()
    turtle.goto(middelpunt)
    turtle.setheading(180+heading)
    turtle.forward(straal_2)
    turtle.setheading(0)
    turtle.down()
    teken_huis(50)


turtle.done()