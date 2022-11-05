

class Point:

    '''
    Dit is een punt in een 2D ruimte
    '''

    def __init__(self, x=0, y=0):
        # print(x)
        self.x = x
        self.y = y

    # geeft info over het object
    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    # gebruikt door de print functie -- user friendly
    def __str__(self):
        return f"({self.x}, {self.y})"