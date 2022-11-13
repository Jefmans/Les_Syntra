import random

# deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = ""
player_status = ""
blackJackValue = 21

def introduction():
    print("Welcome to our BlackJack game. Would you like to play a game? (YES/NO)")
    answer = input("Would you like to play a game(YES/NO):")
    while answer != "YES" or answer != "NO":
        if answer == "YES":
            player = input("Please enter your name: ")
            print(f"Allright {player}, let's play")
            break
        elif answer == "NO":
            print("No problem, we'll shut down the program")
            break   


def playerRound():
    totalPlayerValue = random.choice(playerDeck)
    playerDeck.pop(totalPlayerValue)
    print(f"Your first card is a {totalPlayerValue}. Your new total is {totalPlayerValue}")
    while True:
        if totalPlayerValue > 21:
            print(f"Your total score is {totalPlayerValue} and you lose!")
            break
        if totalPlayerValue == 21:
            print(f"Your total score is {totalPlayerValue} and you win!")
            break
        try:
            drawPlayerRound = str(input(f"Your score is {totalPlayerValue}, would you like to HIT another card?: (YES/NO)"))
        except TypeError:
            print("Only enter YES or NO!!!")
            continue
        if totalPlayerValue < 21:
            if drawPlayerRound == "YES":
                cardLocationPlayer = random.randint(1, (len(playerDeck))) # Deze variabele helpt me onthouden welke kaart werd aangeduid. Deze zal later gepopt worden
                totalPlayerValue = totalPlayerValue + playerDeck[cardLocationPlayer]
                print(f"You drew a {playerDeck[cardLocationPlayer]}. Your total score now is {totalPlayerValue}")
                playerDeck.pop(cardLocationPlayer)
            elif drawPlayerRound == "NO":
                print(f"Your total score is {totalPlayerValue} and you decide to PASS.")
                return totalPlayerValue


def dealerRound():
    totalDealerValue = random.choice(dealerDeck)
    dealerDeck.pop(totalDealerValue)
    print(f"Dealer first card is a {totalDealerValue}. His new total is {totalDealerValue}")
    while True:
        if totalDealerValue == 21:
            print(f"Dealer total score is {totalDealerValue} and it win!")
            break
        elif totalDealerValue > 16:
            print(f"Dealer value is {totalDealerValue} which is higher then 16, he stops!")
            break
        elif totalDealerValue < 21:
            cardLocationDealer = random.randint(1, (len(dealerDeck))) # Deze variabele helpt me onthouden welke kaart werd aangeduid. Deze zal later gepopt worden
            totalDealerValue = totalDealerValue + dealerDeck[cardLocationDealer]
            if totalDealerValue > 21:
                print(f"Dealer drew a {dealerDeck[cardLocationDealer]}. His total score now is {totalDealerValue}, whichis too high. The dealer loses")
                dealerDeck.pop(cardLocationDealer)
            else:
                print(f"Dealer drew a {dealerDeck[cardLocationDealer]}. His total score now is {totalDealerValue}")
                dealerDeck.pop(cardLocationDealer)


def winnerAndLoser():
    playerResult = playerRound()
    print(playerResult)
    dealerResult = dealerRound()
    if playerResult > 21:
        print(f"Player {player} loses!")
    elif playerResult == 21:
        print(f"Player {player} wins!")
    elif dealerResult > 21:
        print(f"Player {player} wins!")
    elif playerResult > dealerDeck:
        print(f"Player {player} wins!")
    else:
        print(f"Player {player} loses!")

def playGame():
    introduction()
    playerRound()
    dealerRound()
    winnerAndLoser() # enkele issues met winning function

introduction()
playerRound()
dealerRound()