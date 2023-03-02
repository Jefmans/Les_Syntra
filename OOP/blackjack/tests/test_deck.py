from deck import Deck



class TestDeck:
    def test_52_cards_in_deck(self):
        deck = Deck()
        assert len(deck.cards) == 52