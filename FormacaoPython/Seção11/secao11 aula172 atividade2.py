class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


lista = []
with open('exercicio2.txt', 'rt') as file:
    for linha in file:
        indice_separa = linha.index('R$')
        nome = linha[ : indice_separa - 1]
        preco = linha[indice_separa : - 1]
        produto = Produto(nome, preco)
        lista.append(produto)

for item in lista:
    print(item.nome, item.preco)
