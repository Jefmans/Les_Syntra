

class Hand:
    
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value_hand(self):
        value = 0
        for card in self.cards:
            value += card.waarde



        return value
    
    def check_if_burned(self):
        return self.get_value_hand() > 21
    
    def adjust_A(self):
        for card in self.cards:
            if card.waarde == 11:
                card.waarde = 1
                return True
        return False


    

    def check_if_blackjack(self):
        return len(self.cards) == 2 and self.get_value_hand() == 21          


    # def print_cards_and_value(self):
    #     for card in self.cards:
    #         print(f"{}")

    # def __str__(self):
    #     for card in self.cards:
    #         print(card)
    #     string = str(self.get_value_hand())
    #     return string
    def __str__(self):
        string =""
        for card in self.cards:
            # string += f"{card.__str__()} \n"
            string += f"{str(card)} \n"
        string += f"waarde : {str(self.get_value_hand())}"
        return string

def main():
    from card import Card
    hand = Hand()
    hand.add_card(Card("clubs", "A"))
    hand.add_card(Card("clubs", 10))
    print(hand)

if __name__ == "__main__":
    main()