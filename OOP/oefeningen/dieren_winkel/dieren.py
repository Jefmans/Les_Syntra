class Dier:
    
    def __init__(self, geluid, kleur, soort, verkoop_prijs=0.0):
        self.geluid = geluid
        self.kleur = kleur
        self.soort = soort
        self.verkoop_prijs = verkoop_prijs
    
    def geluid_maken(self):
        print(self.geluid)
        
    def __str__(self):
        return f"soort:{self.soort} - geluid: {self.geluid} - prijs:{self.verkoop_prijs}"

    # def __repr__(self):
    #     return f"soort:{self.soort} - geluid: {self.geluid} - prijs:{self.verkoop_prijs}"

class ZoogDier(Dier):
    
    def __init__(self, geluid, kleur, soort, vacht, verkoop_prijs=0):
        super().__init__(geluid, kleur, soort, verkoop_prijs)
        self.vacht = vacht

class Reptiel(Dier):
    
    def __init__(self, geluid, kleur, soort, verkoop_prijs=0, gewicht=0):
        super().__init__(geluid, kleur, soort, verkoop_prijs)
        self.gewicht = gewicht

    def geluid_maken(self):
        print(f"zacht {self.geluid}")
        

class Hond(ZoogDier):
    pass


class Kat(ZoogDier):
    pass

class Alien:
    def __init__(self, soort):
        self.soort = soort

    def geluid_maken(self):
        print("buitenaards gemompel")

def main():
    hond1 = Hond('woef','zwart','Labrador Retriever','zacht', 300)
    hond2 = Hond('waf','bruin','German Shepherd','zacht', 250)
    hond3 = Hond('blaf','gold','Golden Retriever','zacht', 285)
    hond4 = Hond('grrrr','bruin','German Shepherd','hard')
    hond5 = Hond('grom','zwart','Bulldog','hard')
    hond6 = Hond('wafwaf','wit','Poodle','zacht', 659)
    hond7 = Hond('woof','bruin','Rottweiler','hard', 335)
    hond8 = Hond('blafbaf','zwart','German Shepherd','zacht', 300)
    hond9 = Hond('wafblaf','wit','Siberian Husky','hard', 775)
    hond10 = Hond('wafbafblaf','bruin','Dachshund','zacht', 800)
    kat1 = Kat('miaaaw','zwart','Siamese','zacht', 125)
    kat2 = Kat('miaauw','zwart','Persian','zacht', 475)
    kat3 = Kat('miaiuw','wit','Maine Coon','zacht', 899)
    kat4 = Kat('maaaw','gold','Sphynx','zacht', 245)
    kat5 = Kat('maw','zwart','British Shorthair','hard', 85)
    kat6 = Kat('miaiaw','zwart','Bengal','zacht', 125)
    kat7 = Kat('miw','bruin','Abyssinian','zacht', 245)
    kat8 = Kat('miew','wit','American Shorthair','hard', 225)
    kat9 = Kat('miauw','zwart','Scottish Fold','hard', 215)
    kat10 = Kat('miaaaww','blauw','Russian Blue','zacht', 999)
    reptiel1 = Reptiel('ssst','geel','Snake', 5, 99)
    reptiel2 = Reptiel('rrrr','zwart','Lizard', 1, 35)
    reptiel3 = Reptiel('ggr','groen','Crocodile', 150, 599)
    reptiel4 = Reptiel('uuuh','bruin','Tortoise', 2, 45)
    reptiel5 = Reptiel('kkk','zwart','Iguana', 3, 75)
    alien1 = Alien()

    dieren = [hond1, hond2, hond3, hond4, hond5, hond6, hond7, hond8, hond9, hond10, kat1, kat2, kat3, kat4, kat5, kat6, kat7, kat8, kat9, kat10, reptiel1, reptiel2, reptiel3, reptiel4, reptiel5, alien1]

    for dier in dieren:
        print(dier)
    


if __name__ == "__main__":
    main()





