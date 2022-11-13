# examen 08_11_2022 Philippe Van Pelt

import random

geld_sp1 = 50
inzet_keuze = 0
kaarten_sp1 = []
kaarten_pc = []

kaart_waardes_sp1 = []
kaart_waardes_pc = []

def inzet_speler():
    '''Vraag de speler om geld in te zetten (tss 0 en max in je portemonnee)'''
    while True:
        i_inzet = int(input("Hoeveel is je inzet: "))
        global geld_sp1
        if i_inzet > 0 and i_inzet <= geld_sp1:
            inzet_keuze = i_inzet
            geld_sp1 = geld_sp1 - inzet_keuze
            break
        else:
            print(f"Sorry, het moet tss 0 en {geld_sp1} zijn")


def genereer_deck():
    '''Genereer een deck (48 kaarten)'''
    kaarten = ['2','3','4','5','6','7','8','9','A','K','Q','B']
    # A = aas, K = koning, Q = koninging, B = boer
    kleur_kaarten = ['klaver','harten','schoppen','ruiten']
    deck = []
    
    for a in kleur_kaarten:
        for b in kaarten:
            deck.append(a + ' ' + b)
    # print(deck)
    return deck


def trek_kaart(deck):
    '''Trek een willekeurige kaart'''
    i_kaart = deck[random.randint(0,len(deck)-1)]
    # print(i_kaart)
    return i_kaart

def verwijder_kaart_deck(deck, kaart):
    '''Verwijder de willekeurige kaart uit het dek, deze kaart mag niet meer gekozen worden'''
    deck.remove(kaart)
    # print(kaart)
    # print(deck)

def add_kaart_lijst_sp(kaart):
    '''Voeg getrokken kaart toe aan de lijst van de speler'''
    kaarten_sp1.append(kaart)

def add_kaart_lijst_pc(kaart):
    '''Voeg getrokken kaart toe aan de lijst van de dealer/PC'''
    kaarten_pc.append(kaart)

def waarde_kaart(kaart):
    '''Bereken waarde van de kaart'''
    if kaart[-1] in ('K','Q','B'):
        i_waarde = 10
        # print(type(i_waarde))
        return i_waarde
    if kaart[-1] == 'A':
        while True:
            i_waarde = int(input("Je hebt een aas, wil je waarde 1 of 11: "))
            if i_waarde == 1 or i_waarde == 11:
                # i_waarde = int(i_waarde)
                return i_waarde
                break
            else:
                print("Sorry, je moet 1 of 11 kiezen.")
    if kaart[-1] in ('2','3','4','5','6','7','8','9'):
        i_waarde = int(kaart[-1])
        return i_waarde

def basis_acties():
    '''Vraag speler wat hij wil doen: passen, kopen, opgeven.'''
    while True:
        i_basis_actie = input("Wat wil je doen: K (kopen), P (passen), O (opgeven): ")
        if i_basis_actie == 'O':
            return i_basis_actie
        elif i_basis_actie == 'P':
            return i_basis_actie
        elif i_basis_actie == 'K':
            return i_basis_actie
        else:
            print("Sorry, geen andere keuze dan K/O/P.")

def check_21():
    if sum(kaart_waardes_sp1) == 21:
        print("Goed zo, je hebt 21, inzet * 1,5")
        global inzet_keuze
        global geld_sp1
        inzet_keuze = inzet_keuze * 1.5
        geld_sp1 = geld_sp1 + inzet_keuze
        inzet_keuze = 0
        return True

def speel_BJ():
    '''Spel definitie'''
    # vraag om een inzet
    inzet_speler()
    # creeer deck
    deck_BJ = genereer_deck()

    # eerste ronde (2*2 kaarten uitdelen):
    # eerste kaart speler
    kaart1_sp1 = trek_kaart(deck_BJ)
    add_kaart_lijst_sp(kaart1_sp1)
    kaart_waardes_sp1.append(waarde_kaart(kaart1_sp1))
    verwijder_kaart_deck(deck_BJ, kaart1_sp1)
    print(f"Speler, je hebt volgende kaart getrokken: {kaarten_sp1[0]}")
    # eerste kaart dealer
    kaart1_pc = trek_kaart(deck_BJ)
    add_kaart_lijst_pc(kaart1_pc)
    kaart_waardes_pc.append(waarde_kaart(kaart1_pc))
    verwijder_kaart_deck(deck_BJ, kaart1_pc)
    # tweede kaart speler
    kaart2_sp1 = trek_kaart(deck_BJ)
    add_kaart_lijst_sp(kaart2_sp1)
    kaart_waardes_sp1.append(waarde_kaart(kaart2_sp1))
    verwijder_kaart_deck(deck_BJ, kaart2_sp1)
    print(f"Speler, je hebt volgende kaart getrokken: {kaarten_sp1[1]}")
    # tweede kaart dealer
    kaart2_pc = trek_kaart(deck_BJ)
    add_kaart_lijst_pc(kaart2_pc)
    kaart_waardes_pc.append(waarde_kaart(kaart2_pc))
    verwijder_kaart_deck(deck_BJ, kaart2_pc)
    print(f"Dealer, je hebt volgende kaart getrokken: {kaarten_pc[1]}")

    print(f"Speler, de totale waarde van je kaarten is momenteel {sum(kaart_waardes_sp1)}")
    
    # check of speler 21 heeft, zo ja stop het spel.
    #### tot hier ben ik geraakt -- verder aan werken ...  
    check_21()
    volgende_actie = (basis_acties())
    print(volgende_actie)

    


speel_BJ()



