import time
from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]
#1
start = time.time()
for i in long_list:
    if i == -1:
        print("znaleziono -1")
koniec = time.time()
print("1. Czas trwania:", koniec - start, "s")
#2
start = time.time()
metoda_set = set(long_list)
for i in metoda_set:
    if i == -1:
        print("znaleziono -1")
koniec = time.time()
print("2. Czas trwania:", koniec - start, "s")

# moje wyniki
# 1. Czas trwania: 0.06899714469909668 s
# 2. Czas trwania: 0.03124380111694336 s
# wniosek metoda z wykorzystaniem set jest wyraźnie szybsza