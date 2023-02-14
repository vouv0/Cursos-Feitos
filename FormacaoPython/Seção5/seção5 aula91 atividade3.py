def num_vogais(texto):
    cont = 0
    vogais = ('a', 'e', 'i', 'o', 'u')
    for letra in texto:
        if letra in vogais:
            cont += 1
    print(f'A string {texto} tem {cont} vogais')


num_vogais('abelhao')
