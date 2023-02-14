cont = soma = 0
qnt = int(input('Quantos numeros inserir na soma? '))

while cont < qnt:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

print(f'Foram digitados {qnt} números e a soma é {soma}')
