import random

OPTIONS = ("schaar", "steen", "blad")

END_SCORE = 3
score = [["speler", 0], ["computer", 0]]

def input_gebruiker():     
    keuze = int(input(f"Kiesgetal:  \n 1 voor 'schaar' \n 2 voor 'steen' \n 3 voor 'blad' \n"))
    # print(f"Jou keuze :")
    return keuze

def vergelijk(keuze_speler):
    keuze_computer = random.randint(1,3)

    print(keuze_speler, ':', OPTIONS[keuze_speler-1], ' - ', keuze_computer,':', OPTIONS[keuze_computer-1])
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

def print_keuze_computer(keuze):
    print(f"keuze van de computer = {OPTIONS[keuze-1]}")

def update_score(speler_gewonnen):
    if speler_gewonnen == None:
        return
    if speler_gewonnen:
        score[0][1] += 1
    elif not speler_gewonnen:
        score[1][1]  += 1

def scoreboard():
    for speler in score:
        print(f"{speler[0]} has a score of {speler[1]}")

def get_max_score():
    max_score = 0
    for speler in score: 
        if speler[1] > max_score:
            max_score = speler[1]
    return max_score

def get_winner():
    winner = ""
    for speler in score:
        if speler[1] == END_SCORE:
            return speler[0]

def game():
    while get_max_score() < END_SCORE:
        keuze = input_gebruiker()
        update_score(vergelijk(keuze))
        scoreboard()
    print(get_winner())
    print("-------GAME END--------")
    



game()

