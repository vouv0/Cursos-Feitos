#Inserindo linhas e colunas

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Inserindo linha
#data.loc['Carlos'] = (55, 'Jogador', 1.78)
#print(data)

#Inserindo linhas atraves de outro DataFrame
#data_nova = pd.DataFrame({
#    'Idade': [23,34,55],
#    'Profissão': ['Cozinheira', 'Contador', 'Jogador'],
#    'Altura': [1.65, 1.73, 1.78]},
#    index=['Julia', 'Roberto', 'Carlos'])

#data_nova.index.name = 'Nome'
#data = data.append(data_nova)
#print(data)


#Inserindo coluna
data['Sobrenome'] = ['Silva', 'Moraes', '','','','']
#print(data)

#Inserindo coluna em posição especifica
data.insert(loc=1, column='Data Nascimento', value=['00/00/0000' for i in range(6)])
print(data)
