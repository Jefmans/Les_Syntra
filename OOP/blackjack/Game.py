from participants import Player, Dealer

class Game:
    
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer('jef', 9999)
        
    def turn(self, choice):
        self.player.take_action(choice)