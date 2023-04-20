

class Klant:

    def __init__(self, naam, winkel):
        self.naam = naam
        self.winkelmand = []
        self.rekening = 0.0
        self.winkel = winkel
        
    
    def __str__(self) -> str:
        return f"{self.naam} - {self.rekening}"

    def dier_in_winkelmand(self, dier):
        self.winkelmand.append(dier)
        self.winkel.uit_virtuele_stock(dier)

    def dier_uit_winkelmand(self, dier):
        self.winkelmand.remove(dier)
        self.winkel.in_virtuele_stock(dier)

    def aankoop(self):
        totaal_prijs = 0
        for dier in self.winkelmand:
            totaal_prijs += dier.verkoop_prijs
            self.winkel.uit_stock(dier)
        self.winkelmand = []
        self.winkel.verkoop(totaal_prijs)  
        
    

    def toon_dieren(self, soort):
        for dier in self.winkel.virtuele_stock:
            if dier.soort == soort:
                print(dier)



def main():
    from winkel import Winkel
    winkel = Winkel()
    klant = Klant("Jos", winkel)
    klant.toon_dieren("Rottweiler")
    print("<<<<<<<DONE>>>>>>>>>>>>>>>")


if __name__ == "__main__":
    main()
