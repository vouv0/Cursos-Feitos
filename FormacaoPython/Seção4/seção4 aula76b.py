lista = [x*2 for x in range(1, 11)]
print(lista)


lista = [str(x)[0] for x in range(1, 21)]
print(lista)


lista = [f'{x} é negativo' if x < 0 else f'{x} é positivo' for x in range(-3, 4)]
print(lista)


lista = [f'{x} é par' if x % 2 == 0 else f'{x} é impar' for x in range(2, 8)]
print(lista)
