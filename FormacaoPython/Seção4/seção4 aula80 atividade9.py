lista = [x for x in range(0, 101) if x % 10 == 0]
print(lista)


lista = [x for x in range(0, 101) if str(x)[-1] == '0']
print(lista)
