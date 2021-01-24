from random import randint

# 1
imiona = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
imiona = [imiona[0] for imiona in imiona]
print(imiona)
# 2
los = [[randint(1, 10) for i in range(4)] for j in range(5)]
print(los)