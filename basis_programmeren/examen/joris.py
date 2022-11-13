import random

# different decks
one_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
six_decks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 24

# card values
cards_values = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                "Q": 10, "K": 10}

# Amount of players
amount_of_players = ["Dealer"]
def total_amount_of_players():
    total_players = input("How many players are there in the game? Maximum 4: ")
    increment_player = 1
    for player in range(int(total_players)):
        info_player = "player" + str(increment_player)
        amount_of_players.append(info_player)
        increment_player += 1
    print(amount_of_players)

bet_amount = []
# information about placing the bets
money_available_for_user = 0
def placing_bets_of_user():
    global money_available_for_user
    money_available_for_user = 50
    amount_of_bet = input("What amount do you want to bet, you have 50 €: ")
    if int(amount_of_bet) > money_available_for_user:
        print("wrong value, try again")
        placing_bets_of_user()
    else:
        print(f"you placed a bet of {amount_of_bet} Euro")
        money_available_for_user = money_available_for_user - int(amount_of_bet)
        bet_amount.append(bet_amount)

def pick_total_of_decks():
    total_decks = input("Howmany decks do you want to choose? 1 or 6? ")
    if int(total_decks) == 1:
        return one_deck
    else:
        return six_decks



def blackjack_game():
    placing_bets_of_user()
    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []

    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    # Initial dealing for player and dealer
    while len(player_cards) < 2:
        # Randomly dealing a card
        player_card = random.choice(one_deck)
        # print(player_card)
        player_cards.append(player_card)
        one_deck.remove(player_card)

        # Updating the player score
        # Print player cards and score
        print(f"PLAYER CARD: {player_card}")
        # Updating player score
        if player_card == "A":
            ask_value = input("what value do you want? 1 or 11?")
            if len(ask_value)< 1:
                print("wrong input")
                ask_value = input("what value do you want? 1 or 11?")
            elif int(ask_value) == 11:
                player_score += 11
            elif int(ask_value) == 1:
                player_score += 1
            else:
                print("wrong input")
                ask_value = input("what value do you want? 1 or 11?")
                if int(ask_value) == 11:
                    player_score += 11
                elif int(ask_value) == 1:
                    player_score += 1
        else:
            player_score += cards_values[player_card]

        # Print player cards and score
        print(f"PLAYER SCORE = {player_score}")

        # Randomly dealing a card
        dealer_card = random.choice(one_deck)
        dealer_cards.append(dealer_card)
        one_deck.remove(dealer_card)

        # Updating the dealer score
        if dealer_card == "A":
            dealer_score += 11
        else:
            dealer_score += cards_values[dealer_card]

        # Print dealer cards and score, keeping in mind to hide the second card and score

        if len(dealer_cards) == 1:
            print("DEALER CARD = secret")
            print("DEALER SCORE = secret")
        else:
            print(f"DEALER CARD = {dealer_card}")
            print(f"DEALER SCORE = {dealer_card}")

    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        print(f"you win {bet_amount[0]}*2,5")
        global money_available_for_user
        money_available_for_user += bet_amount*2,5
        quit()

    # Managing the player moves
    while player_score < 21:
        choice = input("Enter K om te Kopen, P om te passen or O om op te geven : ")

        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != 'K' and choice.upper() != 'P' and choice.upper() != 'O'):

            print("Wrong choice!! Try Again")

        # If player decides to HIT
        if choice.upper() == 'K':

            # Dealing a new card
            player_card_2 = random.choice(one_deck)
            player_cards.append(player_card_2)
            one_deck.remove(player_card_2)

           # Updating player score
            if player_card_2 == "A":
                ask_value = input("what value do you want? 1 or 11?")
                if len(ask_value) < 1:
                    print("wrong input")
                    ask_value = input("what value do you want? 1 or 11?")
                elif int(ask_value) == 11:
                    player_score += 11
                elif int(ask_value) == 1:
                    player_score += 1
                else:
                    print("wrong input")
                    ask_value = input("what value do you want? 1 or 11?")
                    if int(ask_value) == 11:
                        player_score += 11
                    elif int(ask_value) == 1:
                        player_score += 1
            else:
                player_score = player_score + cards_values[player_card_2]

            print(f"PLAYER CARD: {player_card_2}")
            print(f"PLAYER SCORE = {player_score}")

        # If player decides to Passen
        if choice.upper() == 'P':
            break


        if choice.upper() == 'O':
            print("you quit!! you lost your bet.")
            quit()



    if player_score > 21:
        print("player lost the bet")
        print(f"you lost {bet_amount[0]}")
        quit()

    print("DEALER IS REVEALING THE CARDS....")
    print(f"DEALER CARDS: {dealer_cards}")
    print(f"DEALER SCORE = {dealer_score}")

    # Managing the dealer moves
    while dealer_score < 17:
        print("DEALER DECIDES TO HIT.....")

        # Dealing card for dealer
        dealer_card_2 = random.choice(one_deck)
        dealer_cards.append(dealer_card_2)
        one_deck.remove(dealer_card_2)

        # Updating the dealer's score
        dealer_score += cards_values[dealer_card_2]

        # Updating player score in case player's card have ace in them
        while dealer_score < 21:
            if dealer_card_2 == "A":
                if dealer_score <= 6:
                    dealer_score += 11
                else:
                    dealer_score +=1


        # print player and dealer cards
        print(f"DEALER CARDS: {dealer_card_2}")
        print(f"DEALER SCORE = {dealer_score}")

        # Dealer busts
    if dealer_score > 21:
        print("DEALER BUSTED!!! YOU WIN!!!")
        print(f"you win {bet_amount[0]}")

        quit()

    # TIE Game
    if dealer_score == player_score:
        print("TIE GAME!!!!")
        print(money_available_for_user)

        # Player Wins
    if player_score > dealer_score:
        print("PLAYER WINS!!!")
        print(money_available_for_user)

        # Dealer Wins
    else:
        print("DEALER WINS!!!")
        print(money_available_for_user)

blackjack_game()


# Plaats je inzet
