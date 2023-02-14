palavra = input('Digite uma palavra: ')
cont = 0

for letra in palavra:
    if letra != ' ':
        cont += 1

print(f'O numero de caracteres é {cont}')
