import turtle as turtle
from utils.usefull_functions import teken_huis_2
from utils.usefulll_classes import Point

# Maak class Huis
# maak ''' comment '''
# toon help()
# verschillende __init__ tonen
# method teken()
# attribuut zonder init toevoegen
# class Point
# print(Object)
# __str__
# print(Object)

class Huis:
    '''
    Dit is een huis in turtle

    attributen zijn:
        - lengte
        - naarm
        - startpunt
    '''
    def __init__(self):
        self.lengte = int()
        self.start_punt = Point()

    def __str__(self):
        return f"huis met lengte {self.lengte}, naam {self.naam}"

    def set_lengte(self, lengte):
        self.lengte = lengte
    
    def get_lengte(self):
        return self.lengte

    def set_naam(self, naam):
        self.naam = naam
    
    def teken(self):
        teken_huis_2(self.lengte, self.start_punt)
    
    def set_startpunt(self, point):
        self.start_punt = point

    def is_grootste(self, ander_huis):
        return self.lengte < ander_huis.lengte


thuis = Huis()
buur = Huis()

thuis.set_lengte(100)
buur.set_lengte(50)

print(thuis.is_grootste(buur))


# thuis.set_naam("weltevree")
# # print(thuis)


# print(thuis)

# # thuis.teken()

# punt_1 = Point()
# print(punt_1)

# punt_2 = Point(50, 100)
# print(punt_2)

# thuis.set_startpunt(punt_1)
# buur.set_startpunt(punt_2)



# print(buur.start_punt)

# thuis.teken()
# buur.teken()


turtle.done()

# print(thuis.lengte)

# x = thuis.get_lengte()
# print(x)

# buur = Huis()
# print(buur.get_lengte())
# buur.set_lengte(50)
# print(buur.get_lengte())
# print(thuis.get_lengte())

# print(help(Huis))











# turtle.mainloop()


