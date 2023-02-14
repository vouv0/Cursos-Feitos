import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def le_pessoa():
        lista = []
        texto = None
        with open('exercicio7.json', 'r') as arquivo:
            texto = arquivo.read()
        dicionario = json.loads(texto)
        for chave in dicionario:
            pessoa = Pessoa(chave, dicionario[chave])
            lista.append(pessoa)
        return lista


lista_pessoas = Pessoa.le_pessoa()

for pessoa in lista_pessoas:
    print(pessoa.nome, pessoa.idade)
