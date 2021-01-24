try:
    zaw_plik = ""
    with open("plik.txt", "r") as file:
        for linia in file:
            zaw_plik += linia
    with open("plik1.txt", "w") as file:
        file.write(zaw_plik)
except IOError as blad:
    print(blad)