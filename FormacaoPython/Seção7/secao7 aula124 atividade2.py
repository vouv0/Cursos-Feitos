class Pessoa:
    def __init__(self, nome, cpf, dependente = None):
        self.nome = nome
        self.cpf = cpf
        self.dependente = dependente


filho = Pessoa('Rodrigo', '200.300.400-45')
pai = Pessoa('Fernando', '100.200.300-45', filho.nome)
print(f'Nome: {filho.nome} / CPF: {filho.cpf} / Dependente: {filho.dependente}')
print(f'Nome: {pai.nome} / CPF: {pai.cpf} / Dependente: {pai.dependente}')
