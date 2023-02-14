import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def trans_dict(*pessoas):
        dicionario = dict()
        for pessoa in pessoas:
            dicionario[pessoa.nome] = pessoa.idade
        return dicionario


pessoa1 = Pessoa('Vitor', 28)
pessoa2 = Pessoa('Ana', 22)
pessoa3 = Pessoa('João', 30)

dicionario_pessoas = Pessoa.trans_dict(pessoa1, pessoa2, pessoa3)
texto = json.dumps(dicionario_pessoas, indent=4)
with open('exercicio7.json', 'wt') as arquivo:
    arquivo.write(texto)
