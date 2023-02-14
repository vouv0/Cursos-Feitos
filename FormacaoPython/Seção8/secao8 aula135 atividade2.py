from random import randrange

soma = 0

for n in range(0, 100):
    num = randrange(2, 100)
    soma += num

print(f'O resultado da soma dos números aleatórios é {soma}')
