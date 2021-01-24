def Sortowanie(sort):
    return sorted(sort, key=lambda x: (x[1],x[2]))
    
    
list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
print(Sortowanie(list_to_sort))
print(Sortowanie(list_to_sort_2))