from .hand import Hand
from .deck import Deck
import random
NR_DECKS = 6

class Participant:

    def __init__(self, naam, money):
        self.hand = Hand()
        self.naam = naam
        self.money = money

class Dealer(Participant):

    def __init__(self, naam, money):
        super().__init__(naam, money)
        self.nr_decks = NR_DECKS
        self.cards = []
        self._create_decks()
        self.turnover = 0
    
    def _create_decks(self):
        for nr in range(self.nr_decks):
            deck = Deck().shuffle()
            self.cards += deck.cards
        random.shuffle(self.cards)
        
    def give_card(self):
        return self.cards.pop()



class Player(Participant):
    
    def __init__(self, naam, money):
        super().__init__(naam, money)
        
    
    def take_action(self, choice):
        # DICT_OF_CHOICES = {"bet": "self._bet()"}
        # exec(DICT_OF_CHOICES[choice])

        if choice == "bet":
            self._bet()

    def _bet(self):
        pass

