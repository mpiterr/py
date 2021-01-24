haslo = "zadanie"
max_prob = 5
print("zgadnij słowo", +max_prob, "próbach")
while max_prob > 0:
    propozycja = input("propozycja: ")

    if propozycja != haslo:
        max_prob -= 1
        print("Bedne hasło")
        print("zoatało jeszcze ", + max_prob, 'prób')

        if max_prob == 0:
            print("Przegrałeś")
    else:
        print("Gratulacje, udało sie!",)
        break