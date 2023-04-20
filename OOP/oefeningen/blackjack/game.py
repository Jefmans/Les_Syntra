from participants import Player, Dealer

PLAYERS = [("jos", 200), ("jef", 100), ("jan", 40), ("joris", 10)]

class Game:
    
    def __init__(self, nr_players):
        self.players = []
        self.dealer = Dealer('Soufiane Escobar', 9999)
        self.nr_players = nr_players
    
    def run(self):
        self.create_players()
        self.deel_kaarten_start()
        for player in self.players:
            self.turn(player)

    def create_players(self):
        for i in range(self.nr_players):
            naam, geld = PLAYERS[i]
            self.players.append(Player(naam, geld, self))

    def deel_kaarten_start(self):
        for i in range(2):
            self.deel_kaarten_per_ronde(i)
    
    def deel_kaarten_per_ronde(self, ronde):
        for player in self.players:
            card = self.dealer.give_card()
            player.hand.add_card(card)
        card = self.dealer.give_card()
        if ronde == 0:
            card.set_hidden()
        self.dealer.hand.add_card(card)

    def turn(self, player):
        print("="*20)
        print(player.naam)
        print("="*20)
        print(player.hand)
        if player.hand.check_if_blackjack():
            print("Jeeuh gewonnen - BLACKJACK") 
        else:
            playing = True
            while playing:
                input_choice = input("kies: Hit of Pass\n" )
                playing = player.take_action(input_choice)
                if playing: 
                    print(player.hand)
                    if player.hand.check_if_burned():
                        if not(player.hand.adjust_A()):
                            print("Verloren")
                            playing = False
                        else:
                            print('-'*20)
                            print("waarde Aas aangepast naar 1")
                            print(player.hand)
            
        
        # self.player.take_action(choice)





def main():
    game = Game(len(PLAYERS))
    game.run()

if __name__ == "__main__":
    main()