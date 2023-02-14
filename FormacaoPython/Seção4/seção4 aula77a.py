lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = list(filter(lambda x: x % 2 == 0, lista))
print(lista)


lista = [[x for x in range(1, 4)] for y in range(1, 4)]
print(lista)


lista = [[str(x) + str(y) for x in range(1, 4)] for y in range(1, 4)]
print(lista)
