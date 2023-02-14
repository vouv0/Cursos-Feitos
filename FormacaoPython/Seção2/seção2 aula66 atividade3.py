qnt = int(input('Quantas palavras: '))
texto = ''

for x in range(1, qnt+1):
    palavra = input("Digite uma palavra: ")
    texto += palavra

print(texto)
