bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''


def utf8len(s):
    return len(s.encode('utf-8'))


plik1 = open("plik1.txt", "w")
plik2 = open("plik2.txt", "w")
plik3 = open("plik3.txt", "w")

files = [plik1, plik2, plik3]

maxsize = 100
i = 0

text_to_save = ''
file_to_save_index = 0
file_to_save = plik1

while i < len(bridge_of_death):
    text_to_save += bridge_of_death[i]
    i += 1
    if utf8len(text_to_save) == maxsize or i == len(bridge_of_death) - 1:
        file_to_save = files[file_to_save_index % len(files)]

        file_to_save.seek(0)
        file_to_save.write(text_to_save)
        file_to_save.truncate()

        text_to_save = ''
        file_to_save_index += 1


plik1.close()
plik2.close()
plik3.close()
