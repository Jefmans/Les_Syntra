from klanten import Klant
from dieren import Hond, Kat, Reptiel, Alien


class Winkel:

    def __init__(self):
        self.stock = self._create_stock()
        self.virtuele_stock = self.stock
        self.klanten = []

    def _create_stock(self):
        hond1 = Hond('woef','zwart','Labrador Retriever','zacht', 300)
        hond2 = Hond('waf','bruin','German Shepherd','zacht', 250)
        hond3 = Hond('blaf','gold','Golden Retriever','zacht', 285)
        hond4 = Hond('grrrr','bruin','German Shepherd','hard')
        hond5 = Hond('grom','zwart','Bulldog','hard')
        hond6 = Hond('wafwaf','wit','Rottweiler','zacht', 659)
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
        alien1 = Alien("ET")

        return  [hond1, hond2, hond3, hond4, hond5, hond6, hond7, hond8, hond9, hond10, kat1, kat2, kat3, kat4, kat5, kat6, kat7, kat8, kat9, kat10, reptiel1, reptiel2, reptiel3, reptiel4, reptiel5, alien1]


    def uit_virtuele_stock(self, dier):
        self.virtuele_stock.remove(dier)


    def in_stock(self):
        pass

    def maak_klant_aan(self, naam):
        self.klanten.append(Klant(naam, self))


def main():
    winkel = Winkel()
    winkel.maak_klant_aan("Jef")
    klant = winkel.klanten[0]

    print(len(winkel.virtuele_stock))
    print(len(klant.winkelmand))

    klant.dier_in_winkelmand(winkel.stock[0])

    print(len(winkel.virtuele_stock))
    print(len(klant.winkelmand))

if __name__ == "__main__":
    main()