import turtle as turtle
from utils.usefull_functions import teken_veelhoek, teken_parallelogram


def teken_kubus(lengte, hoek):
    teken_veelhoek(lengte, 4, "right")
    teken_parallelogram(lengte, lengte/2, hoek)
    turtle.goto(0,-lengte)
    teken_parallelogram(lengte, lengte/2, hoek)
    turtle.left(hoek)
    turtle.forward(lengte/2)
    turtle.right(hoek)
    teken_veelhoek(lengte, 4, "left")

teken_kubus(100, 40)

turtle.done()