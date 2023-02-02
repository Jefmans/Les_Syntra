class Dier:
    
    def __init__(self, geluid, kleur, soort, verkoop_prijs=0.0):
        self.geluid = geluid
        self.kleur = kleur
        self.soort = soort
        self.verkoop_prijs = verkoop_prijs
    
    def geluid_maken(self):
        print(self.geluid)


class ZoogDier(Dier):
    
    def __init__(self, geluid, kleur, soort, vacht, verkoop_prijs=0):
        super().__init__(geluid, kleur, soort, verkoop_prijs)
        self.vacht = vacht

class Reptiel(Dier):
    pass

class Hond(ZoogDier):
    pass

class Kat(ZoogDier):
    pass


def main():
    hond = Hond("woef", "zwart", "labrador", "zaacht")
    print(hond.geluid_maken())

if __name__ == "__main__":
    main()