from ..participants import Dealer


class TestDealer:
    def test_number_of_cards_from_decks(self):
        dealer = Dealer('jef', '999')
        assert dealer.nr_decks * 52 == len(dealer.cards)

    