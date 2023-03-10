from hand import Hand
from deck import Deck
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
            deck = Deck()
            deck.shuffle()
            self.cards += deck.cards
        random.shuffle(self.cards)
        
    def give_card(self):
        return self.cards.pop()


class Player(Participant):
    
    def __init__(self, naam, money, game):
        super().__init__(naam, money)
        self.game = game

    def take_action(self, choice):
        # DICT_OF_CHOICES = {"bet": "self._bet()"}
        # exec(DICT_OF_CHOICES[choice])
        choice = choice.lower()
        keep_playing = True

        if choice == "hit":
            self._hit_card()
            return keep_playing
        elif choice == "pass":
            self._pass_turn()
            return not(keep_playing)

    def _hit_card(self):
        self.hand.add_card(self.game.dealer.give_card())

    def _pass_turn(self):
        pass

