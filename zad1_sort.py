def dwa(le):
    return  le[1], le[2]

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

list_to_sort.sort(key=dwa)

print('Lista posortowana', list_to_sort)
