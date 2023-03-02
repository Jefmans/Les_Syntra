from ..card import Card

class TestCard:
    def test_card_set_waarde_beeldje(self):
        card_dame = Card("club", "D")
        card_heer = Card("club", "K")
        card_boer = Card("club", "V")
        assert card_dame.waarde == 10 
        assert card_heer.waarde == 10
        assert card_boer.waarde == 10
    
    def test_card_value_2_tot_10(self):
        for waarde in range(2, 10):
            card = Card("club", waarde)
            assert card.waarde == waarde

