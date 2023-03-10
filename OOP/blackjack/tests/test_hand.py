from ..hand import Hand
from ..card import Card

def test_blackjack():
    hand = Hand()
    hand.add_card(Card("clubs", "A"))
    hand.add_card(Card("clubs", 10))
    hand.check_if_blackjack()
    assert hand.blackjack == False

def test_print_hand():
    hand = Hand()
    hand.add_card(Card("clubs", "A"))
    # hand.add_card(Card("clubs", 10))
    print(hand)

