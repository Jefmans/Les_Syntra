# aantal decks (1-6)
# kaarten_per_soort (aantal waarden, waardes) >>>> 1/11, koning, koningin, boer, 9, ..., 2
# kaarten_deck (Klaver, Schoppen, Ruiten, Harten)
# dealer (computer)
# meerdere spelers
# inzet minimum 50€
# inzet plaatsen
# kaarten delen (wijzersin), zichtbaar & niet zichtbaar
# winstverdeling
# keuze maken (passen, kopen, opgeven (splitsen, verdubbelen))
# dealer (2de kaart zichtbaar 16++, 17ofmeer stoppen)


import random as random

aantal_spelers = 1
aantal_decks = 1


######################### Kaarten/Deck
def aanmaken_deck():
    deck = []
    for soort in ['Ruiten', 'Harten', 'Klaveren', 'Schoppen']:
            for waarde in ['Aas', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Boer', 'Koningin', 'Koning']:
                deck.append((soort, waarde))
    return deck

def toon_deck(deck):
    for kaart in deck:
        print(kaart)
            
def doorheen_schudden_deck(deck):
    random.shuffle(deck)

def deel_kaart_uit_deck(deck):
    kaart = deck[-1]
    deck.pop()
    return kaart


######################### Hand
def aanmaken_hand():
    hand = []
    return hand

def ontvang_kaart_uit_deck_voor_eigen_hand(hand, kaart):
    hand.append(kaart)
    return hand, kaart

def bepaal_waarde_hand(hand):
    waarde = 0
    for kaart in hand:
        if type(kaart[1]) == int:
            waarde += kaart[1]
        elif kaart[1] == 'Aas':
            waarde += 11
        else:
            waarde += 10
    return waarde

def toon_hand(hand):
    for kaart in hand:
        print(kaart)

def vergelijk_waarde_handen(hand_deler, hand_speler):
    winst_marge = 1.0
    if bepaal_waarde_hand(hand_deler) > 21:
        winst_marge = 2.0
    elif bepaal_waarde_hand(hand_deler) == 21:
        if bepaal_waarde_hand(hand_speler) > 21 or bepaal_waarde_hand(hand_speler) < 21:
            winst_marge = 0.0
        elif bepaal_waarde_hand(hand_speler) == 21:
            winst_marge = 1.0
    elif bepaal_waarde_hand(hand_deler) < 21:
        if bepaal_waarde_hand(hand_speler) > 21 or bepaal_waarde_hand(hand_speler) < bepaal_waarde_hand(hand_deler):
            winst_marge = 0.0
        elif bepaal_waarde_hand(hand_speler) == 21:
            winst_marge = 1.0
    return winst_marge
    
######################### Inzet
def inzet_vragen():
    inzet = int(input("Geef uw inzet?"))
    try:
        int(inzet)
    except:
        print("Gelieve een bedrag in te geven tss 0 en 50€.")       
    return inzet 

######################### Spelkeuzes
def keuze_maken():
    keuze = int(input("Geef uw keuze op: 1=Passen, 2=Kopen, 3=Opgeven"))
    try:
        int(keuze)
    except:
        print("Gelieve een nummer in te geven van 1 tot 3.")       
    return keuze



    
######################### BlackJack
######################### BlackJack
def BlackJack(aantal_spelers):
    deck_deler = aanmaken_deck()    
    doorheen_schudden_deck(deck_deler)
    hand_speler = aanmaken_hand()
    hand_deler = aanmaken_hand()
    toon_deck(deck_deler)
    print('------------------')
    inzet_vragen()
    
    print('------------------')
    for n in range(aantal_spelers+1):
        ontvang_kaart_uit_deck_voor_eigen_hand(hand_speler, deel_kaart_uit_deck(deck_deler))
        toon_hand(hand_speler)
        print(bepaal_waarde_hand(hand_speler))
        print('------------------')
        ontvang_kaart_uit_deck_voor_eigen_hand(hand_deler, deel_kaart_uit_deck(deck_deler))
        toon_hand(hand_deler)
        print(bepaal_waarde_hand(hand_deler))
    
    print('------------------')
    while keuze_maken() != 3:
        if keuze_maken() == 2:
            ontvang_kaart_uit_deck_voor_eigen_hand(hand_speler, deel_kaart_uit_deck(deck_deler))
            toon_hand(hand_speler)
            print(bepaal_waarde_hand(hand_speler))
            
    print('------------------')
    while bepaal_waarde_hand(hand_deler) <= 16:
        ontvang_kaart_uit_deck_voor_eigen_hand(hand_deler, deel_kaart_uit_deck(deck_deler))
        toon_hand(hand_deler)
        print(bepaal_waarde_hand(hand_deler))
            
    print('------------------')
    print(vergelijk_waarde_handen(hand_deler, hand_speler))


                
BlackJack(aantal_spelers)    
    
    
    
# deck = aanmaken_deck()
# # print(deck)
# # toon_deck(deck)
# doorheen_schudden_deck(deck)
# toon_deck(deck)
# print('------------------')
# kaart1 = deel_kaart_uit_deck(deck)
# toon_deck(deck)
# print(kaart1)
