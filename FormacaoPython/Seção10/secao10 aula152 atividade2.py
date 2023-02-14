def func2(lista):
    for n in lista:
        yield n*2


lista1 = [1, 2, 3, 4]

for i in func2(lista1):
    print(i)
