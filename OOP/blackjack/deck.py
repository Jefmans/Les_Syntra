from card import Card
import random

KLEUREN = ["clubs", "spades", "hearts", "diamonds"]
GETALLEN = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "K"]

class Deck:

    def __init__(self):
        self.cards = []
        self._create()

    def _create(self):
        for kleur in KLEUREN:
            for getal in GETALLEN:
                self.cards.append(Card(kleur, getal))

    def shuffle(self):
        random.shuffle(self.cards)

    