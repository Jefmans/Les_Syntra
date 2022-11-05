import random

OPTIONS = {1:"schaar", 2: "steen", 3:"blad"}
END_SCORE = 3
score = {"speler":0, "computer":0}

def input_gebruiker():     
    keuze = int(input(f"Kiesgetal: {OPTIONS}"))
    print(f"Jou keuze : {OPTIONS.get(keuze)}")
    return keuze

def vergelijk(keuze_speler):
    keuze_computer = random.randint(1,3)
    print_keuze_computer(keuze_computer)

    print(keuze_speler, ':', {OPTIONS.get(keuze_speler)}, ' - ', keuze_computer,':', {OPTIONS.get(keuze_computer)})
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
    print(f"keuze van de computer = {OPTIONS.get(keuze)}")

def score(speler_gewonnen):
    if speler_gewonnen == None:
        return
    if speler_gewonnen:
        score["speler"] += 1
    elif not speler_gewonnen:
        score["computer"]  += 1

def scoreboard():
    print(f"{score}")

def get_max_score():
    return max(score.values())

def get_winner():
    return max(score, key=score.get)

def game():
    while get_max_score() < END_SCORE:
        keuze = input_gebruiker()
        score(vergelijk(keuze))
        scoreboard()
    print(get_winner())
    print("-------GAME END--------")
    



game()

