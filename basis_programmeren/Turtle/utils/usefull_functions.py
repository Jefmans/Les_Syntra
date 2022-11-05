import turtle as turtle

TOTAAL_AANTAL_GRADEN = 360

def test_functie():
    global TOTAAL_AANTAL_GRADEN
    TOTAAL_AANTAL_GRADEN += 40
    print(TOTAAL_AANTAL_GRADEN)

# test_functie()

def teken_veelhoek(lengte, aantal_hoeken, richting):
    hoek_graad = TOTAAL_AANTAL_GRADEN/aantal_hoeken
    for i in range(aantal_hoeken):
        turtle.forward(lengte)
        if richting == "left":
            turtle.left(hoek_graad)
        elif richting == "right":
            turtle.right(hoek_graad)
    # print(TOTAAL_AANTAL_GRADEN)

# teken_veelhoek()


def teken_vierkant(lengte):
    for x in range(4):
        turtle.forward(lengte)
        turtle.left(90)

def teken_parallelogram(lengte_A, lengte_B, hoek):
    for x in range(2):
        turtle.forward(lengte_A)
        turtle.left(hoek)
        turtle.forward(lengte_B)
        turtle.left(180-hoek)
    # turtle.forward(lengte_A)
    # turtle.left(hoek)
    # turtle.forward(lengte_B)
    # turtle.left(180-hoek)

def teken_huis(lengte):
    
    turtle.down()
    turtle.setheading(0)
    teken_veelhoek(lengte, 4, "left")
    turtle.setheading(90)
    turtle.forward(lengte)
    turtle.setheading(60)
    teken_veelhoek(lengte, 3, "right")
    turtle.up()

def teken_huis_2(lengte, point):
    turtle.up()
    turtle.goto((point.x, point.y))
    turtle.down()
    turtle.setheading(0)
    teken_veelhoek(lengte, 4, "left")
    turtle.setheading(90)
    turtle.forward(lengte)
    turtle.setheading(60)
    teken_veelhoek(lengte, 3, "right")
