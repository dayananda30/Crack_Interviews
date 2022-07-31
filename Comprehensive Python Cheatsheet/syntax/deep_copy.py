from copy import deepcopy

list_1 = [1, 2, 3]

list_2 = deepcopy(list_1)

list_2[0] = 10
print(list_1)
print(list_2)

print(id(list_1))
print(id(list_2))

