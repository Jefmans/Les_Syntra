

class Card:

    def __init__(self, kleur, getal):
        self.kleur = kleur
        self.getal = getal

        self.waarde = self.set_waarde()
        self.hidden = True

    def set_waarde(self):
        if self.getal == "K" or self.getal == "D" or self.getal == "V":
            return 10
        else:
            return self.getal
    
