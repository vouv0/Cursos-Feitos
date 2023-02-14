import csv

class Empresa:
    def __init__(self, id_empresa, nome, funcionarios, lucro):
        self.id_empresa = id_empresa
        self.nome = nome
        self.funcionarios = funcionarios
        self.lucro = lucro


empresas = []
with open('exercicio6.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linha in leitor:
        #print(id_empresa, nome, funcionarios, lucro)
        empresa = Empresa(linha[0], linha[1], linha[2], linha[3])
        empresas.append(empresa)

for emp in empresas:
    print(emp.id_empresa, emp.nome, emp.funcionarios, emp.lucro)
