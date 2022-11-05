import turtle as turtle

turtle.shape("turtle")

def naam_functie(variabele, naam):
    if variabele == "turtle" or variabele == "Turtle":
        print(f"Jeey het is schilpad ! Hij heet {naam}")
    # elif variabele == "Turtle":
    #     print("het is toch een schilpad")
    else:
        print("Het is geen schilpad")

# naam_functie("turtle", "Leo")

def teken_vierkant(lengte):
    for x in range(4):
        turtle.forward(lengte)
        turtle.right(90)

def teken_driehoek(lengte):
    for x in range(3):
        turtle.forward(lengte)
        turtle.right(120)

def teken_vijfhoek(lengte):
    for x in range(5):
        turtle.forward(lengte)
        turtle.right(360/5)

def teken_huis(lengte):
    teken_vierkant(lengte)
    teken_driehoek(lengte)

# teken_huis(50)

def teken_veelhoek(lengte, hoeken):
    for x in range(hoeken):
        turtle.forward(lengte)
        turtle.right(360/hoeken)
n = 20
teken_veelhoek(200/n, n)

turtle.done()
