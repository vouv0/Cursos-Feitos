cont = soma = 0

while cont < 5:
    num = int(input("Digite um número: "))
    if num < 0:
        cont += 1
        continue
    else:
        soma += num
        cont += 1

print(f'A soma dos valores é {soma}')
