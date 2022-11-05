import turtle as turtle
from utils.usefull_functions import teken_huis


coordinaten = []

coordinaten.append((0,0))

# coordinaten.append("a")
# coordinaten.append("b")
# coordinaten.append("a")

print(coordinaten)
# coordinaten.append("a", "b")

coordinaten.append((100, 100))

print(coordinaten)
# laatste = coordinaten.pop()
# print(laatste)
print(coordinaten)


print(type("a"))
print(type((0,0)))
print(type(5))

print(coordinaten[0])

for x in range(len(coordinaten)):
    print(coordinaten[x])

for coor in coordinaten:
    print(coor)



# for data in list:
#     try:
#         int(data)


def print_woord(woord, naam="jef"):
    print(woord)
    print(naam)

print_woord("hallo", naam="kevin")


lst = (2, 0)

print(lst[0])
