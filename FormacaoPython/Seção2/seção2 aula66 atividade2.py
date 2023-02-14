fatorial = 1
num = int(input('Digite um número: '))

for x in range(1, num+1):
    fatorial *= x

print(f'{num}! é igual a {fatorial}.')
