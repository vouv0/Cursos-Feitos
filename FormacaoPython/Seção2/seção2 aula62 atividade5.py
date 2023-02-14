texto = input('Digite um texto: ')
cont = vazio = 0

while cont < len(texto):
    if texto[cont] == ' ':
        vazio += 1
    cont += 1

print(f'O número de espaços vazios é {vazio}.')
