

class Card:

    def __init__(self, kleur, getal):
        self.kleur = kleur
        self.getal = getal

        self.waarde = self.set_waarde()
        self.hidden = False

    def set_waarde(self):
        if self.getal == "K" or self.getal == "D" or self.getal == "V":
            return 10
        elif self.getal == "A":
            return 11
        else:
            return self.getal
    
    def set_hidden(self):
        self.hidden = True
    
    def __str__(self):
        return f"{self.kleur} - {self.getal}"
