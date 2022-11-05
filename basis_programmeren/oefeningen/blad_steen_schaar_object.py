import random


class BladSteenSchaarGame():
    OPTIONS = {1:"schaar", 2: "steen", 3:"blad"}

    def __init__(self):
        self.END_SCORE = 3
        self.score_speler = 0
        self.score_computer = 0

    def _input_gebruiker(self):     
        keuze = int(input(f"Kiesgetal: {self.OPTIONS}"))
        print(f"Jou keuze : {self.OPTIONS.get(keuze)}")
        return keuze

    def _vergelijk(self, keuze_speler):
        keuze_computer = random.randint(1,3)
        self._print_keuze_computer(keuze_computer)

        print(keuze_speler, ':', {self.OPTIONS.get(keuze_speler)}, ' - ', keuze_computer,':', {self.OPTIONS.get(keuze_computer)})
        if keuze_computer == keuze_speler:
            print("gelijk spel")
            return None
        elif keuze_speler == 1 and keuze_computer == 3:
            print("speler wint")
            return True
        elif keuze_speler == 3 and keuze_computer == 1:
            print("computer wint")
            return False
        elif keuze_speler > keuze_computer:
            print("speler wint")
            return True
        else:
            print("computer wint")
            return False

    def _print_keuze_computer(self, keuze):
        print(f"keuze van de computer = {self.OPTIONS.get(keuze)}")

    def _score(self, speler_gewonnen):
        if speler_gewonnen == None:
            return
        if speler_gewonnen:
            self.score_speler += 1
        elif not speler_gewonnen:
            self.score_computer  += 1

    def _scoreboard(self):
        print(f"speler: {self.score_speler} <=> computer: {self.score_computer}")

    def _get_max_score(self):
        return max(self.score_computer, self.score_speler)

    def _get_winner(self):
        if self.score_computer > self.score_speler:
            return "computer"
        else:
            return "speler"

    def run(self):
        while self._get_max_score() < self.END_SCORE:
            keuze = self._input_gebruiker()
            self._score(self._vergelijk(keuze))
            self._scoreboard()
        print(f"THE WINNER IS {self._get_winner().upper()}")
        print("-------GAME END--------")
        



game = BladSteenSchaarGame()
game.run()

