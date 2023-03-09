

class Hand:
    
    def __init__(self):
        self.cards = []
        self.blackjack = False
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value_hand(self):
        value = 0
        for card in self.cards:
            value += card.waarde
        return value

    def check_if_blackjack(self):
        if len(self.cards) == 2 and self.get_value_hand() == 21:            
            self.blackjack = True
