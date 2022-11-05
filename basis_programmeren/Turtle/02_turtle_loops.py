import turtle as turtle

turtle.shape("turtle")

# aantal_hoeken = int(input("geef hoeken")
aantal_hoeken = 4

counter = 0
while (counter < 4):
    turtle.forward(90)
    print("------ 1 ------- ", counter)
    for n in range(aantal_hoeken):
        turtle.forward(90)
        turtle.right(360/aantal_hoeken)
        print("------ 2 ------- ", counter)
    counter += 1
        

while(counter < 4):
    # counter = counter + 1
    turtle.forward(90)
    turtle.right(360/4)



turtle.done()