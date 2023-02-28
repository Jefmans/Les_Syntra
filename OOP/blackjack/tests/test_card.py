from ..card import Card

class TestCard:
    def test_card_set_waarde(self):
        card_dame = Card("club", "D")
        assert card_dame.waarde == 10

    def test_card(self):
        pass