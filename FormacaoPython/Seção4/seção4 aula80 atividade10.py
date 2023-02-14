lista = ['0' if x % 10 == 0 else '-' for x in range(0, 21)]
print(lista)


lista = ['0' if str(x)[-1] == '0' else '-' for x in range(0, 21)]
print(lista)
