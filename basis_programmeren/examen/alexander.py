
import random
#deck maken. hand speler en hand dealer
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]*6
playerhand= []
dealerhand = []

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = 'J'
        if card == 12:card = 'Q'
        if card == 13: card = 'K'
        if card == 14: card = 'A'
        hand.append(card)
    return hand
#stoppen of doorgaan
def play_more():
    again = input('Do you want to continue playing? type yes or no.').strip().lower()
    if again == 'yes':
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]*6
        playerhand= []
        dealerhand = []
    else: 
        print ('See you soon.')
#waarden geven aan plaatjes.
def sum_card(hand):
    sum_card = 0
    for card in hand:
        if card == "J" or card == 'Q' or card == 'K':
            sum_card += 10
        elif card == 'A':
            if sum_card < 11:
                sum_card += 11
            else: sum_card += 1
    return sum_card

def hit(hand):
    card = deck.pop()
    if card == 11: card = 'J'
    if card == 12: card = 'Q'
    if card == 13: card = 'K'
    if card == 14: card = 'A'
    hand.append(card)
    return hand

#score. dealer 21, speler 21 D en S > 21, handen vergelijken.

def score(dealerhand, playerhand):
    if sum_card(playerhand) == 21:
        print('you got a blackjack: hands are {} and {}'.format(playerhand, dealerhand))
    elif sum_card(dealerhand) == 21:
        print('you lose, dealer has blackjack: hands are {} and {}'.format(playerhand, dealerhand))
    elif sum_card(playerhand)  > 21:
        print('you lose hands are {} and {}'.format(playerhand, dealerhand))
    elif sum_card(dealerhand)  > 21:
        print('dealer to high, you win hands are {} and {}'.format(playerhand, dealerhand))
    elif sum_card(playerhand) < sum_card(dealerhand):
        print('you lose hands are {} and {}'.format(playerhand, dealerhand))
    elif sum_card (playerhand)  > sum_card(dealerhand):
        print('you win hands are {} and {}'.format(playerhand, dealerhand)) 
        play_more()
    
#spelverloop: opgeven splitsen 

def blackjack():
    dealerhand = deal(deck)
    playerhand = deal(deck)
    options = 0
    while options != 'g':
        print('hand dealer:{}'.format(dealerhand))
        print('player hand{}'.format(playerhand))
        score(dealerhand, playerhand)
        options= input('what do you want to do: give up press g, hit press h, no cards press n'.lower().strip())
        if options == 'h':
            hit(playerhand)
            while sum_card(dealerhand) < 17:
                hit (dealerhand)
            score(dealerhand, playerhand)
            play_more()
        elif options == 'n' :
            while   sum_card(dealerhand) < 17:
                    hit(dealerhand)
            score(dealerhand, playerhand)
            play_more()
        elif options == 'g':
            print ('see you next time')   
        
                    
blackjack()