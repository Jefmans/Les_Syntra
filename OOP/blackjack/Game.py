from participants import Player

class Game:
    
    def __init__(self):
        self.player = Player()

    def turn(self, choice):
        self.player.take_action(choice)