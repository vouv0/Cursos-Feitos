lista = [x for x in range(1, 11)]
print(lista)


pares = [x for x in lista if x % 2 == 0]
print(pares)


lista_auxiliar = [2, 5, 10]
lista_aux = [x for x in range(1, 11) if x not in lista_auxiliar]
print(lista_aux)


lista2 = [x for x in range(-10, 20) if x <= 10 if x >= 0]
print(lista2)
