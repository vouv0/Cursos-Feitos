lista = []
with open('exercicio1.txt', 'rt') as arquivo:
    ler = arquivo.read()
    for item in ler:
        if item == "\n":
            pass
        else:
            lista.append(item)

print(lista)
