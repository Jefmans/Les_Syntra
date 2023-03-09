lijst = ["1234567", "12345678", "1234 a 2345"]
goed_nr = []
slechte_nr = []

def check_nummer(nr):
    try:
        # print("----1-----")
        int(nr)
        # print("----2-----")
        goed_nr.append(nr)
        try:
            if "8" in nr:
                print("JJJJJJEEEEEEUUUUYYY", nr)
            else:
                raise RuntimeError
        except:
            print("LOSERS")
    except:
        slechte_nr.append(nr)

for nr in lijst:
    check_nummer(nr)

print("GOEDE")
print(goed_nr)
print("--"*20)
print("SLECRT")
print(slechte_nr)

