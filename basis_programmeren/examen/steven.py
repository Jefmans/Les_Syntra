import random

dek = [] # hier stoppen we de kaarten in (zes deks)

# maak één dek kaarten
def bepaal_dek():
    for i in range(0,4): # dit staat voor de kleur
        kleur = i
        for j in range(1,14): # dit staat voor het getal (waarbij boer 11 is, dame 12 & heer 13)
            getal = j
            if 1 > j < 10: # definieert meteen ook waarde voor kaart, zodat beeldjes (10-13) de correcte waarde 10 krijgen
                waarde = j
            if j == 1: # geeft waarde 11 aan de aas (is niet juist, maar belangrijkere waarde dan 1)
                waarde = 11
            else:
                waarde = 10
            kaart = kleur,getal,waarde
            dek.append(kaart)
# we hebben zes deks nodig in de lijst van alle kaarten
def zes_deks():
    for i in range(0,7):
        bepaal_dek()

zes_deks()
# print(dek) #print was om te checken of de kaarten goed in het dek zitten

# leg aantal spelers vast

AANTAL_SPELERS = 1

# initieer inzetbaar_bedrag

INZETBAAR_BEDRAG = 50

# functie om geld in te zetten, rekening houdend met mogelijke inputs van de speler
def leg_in():
    while True:
        try:
            ingezet_bedrag = int(input("geef je inzet in"))
            if ingezet_bedrag > inzetbaar_bedrag:
                print("je kunt niet meer inzetten dan je hebt")
                continue
            if ingezet_bedrag < 0:
                print("je kunt geen negatief bedrag inzetten")
                continue
            return ingezet_bedrag
        except ValueError:
            print("dat is geen bedrag, voor je inzet in")

# functie om een kaart te delen
def deel_kaart():
    gedeelde_kaart = random.choice(dek) # gedeelde kaart is een willekeurige kaart uit de lijst
    return gedeelde_kaart

# alle spelers (incl computer) zullen kaarten hebben in het spel
kaarten_computer = []
kaarten_speler_1 = []


# functie voor eerste kaartdeling
def start_deling():
    kaart1_speler_1 = deel_kaart()
    kaarten_speler_1.append(kaart1_speler_1)
    print(f"eerste kaart speler is {kaarten_speler_1[0:2]}") # bij de spelers worden de kaarten zichtbaar gemaakt, daarom print (enkel kleur & getal)
    kaart1_computer = deel_kaart()
    kaarten_computer.append(kaart1_computer)

    kaart2_speler_1 = deel_kaart()
    kaarten_speler_1.append(kaart2_speler_1)
    print(f"kaarten speler zijn {kaarten_speler_1[0:2]}") # bij de spelers worden de kaarten zichtbaar gemaakt, daarom print (enkel kleur & getal)
    kaart2_computer = deel_kaart()
    print(f"2de kaart computer is {kaart2_computer[0:2]}") # de tweede kaart van de computer moet wel getoond worden (enkel kleur & getal)
    kaarten_computer.append(kaart2_computer)

# een functie om te checken of je 21 hebt
def check_of_gewonnen():
    totale_waarde = 0
    gewonnen = False
    for kleur, getal, waarde in kaarten_speler_1:
        totale_waarde += waarde
    print(totale_waarde)
    if totale_waarde == 21:
        gewonnen = True
        print("gewonnen!")
        return gewonnen


# een functie om het spel te starten
def startspel():
    inzetbaar_bedrag = 50
    ingezet_bedrag = leg_in() # start met geld in te zetten
    inzetbaar_bedrag = inzetbaar_bedrag - ingezet_bedrag # het resterend inzetbaar bedrag zakt eenmaal is ingezet
    print(f"ingezet bedrag is {ingezet_bedrag}, resterend bedrag in te zetten is {inzetbaar_bedrag}")
    start_deling()
    gewonnen = check_of_gewonnen()
    if gewonnen == true:
        winst = 1.5 * ingezet_bedrag
        inzetbaar_bedrag = inzetbaar_bedrag + winst
        startspel() # 21 gehaald dus spel is opnieuw te beginnen
    else:
        pass

startspel()

# een functie voor de eerste zet

# def (keuzespeler)