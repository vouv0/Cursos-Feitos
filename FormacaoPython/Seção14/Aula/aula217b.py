#Atualizando valores

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Mudando todos os valores de uma coluna
#data.loc[:, 'Idade'] = 77
#print(data)

#Mudando todos os valores de um intervalo
#data.loc[:, 'Idade':'Profissão'] = None
#print(data)

#Mudando todos os valores de colunas especificas
data.loc[:, ['Idade', 'Altura']] = (22, 1.80)
print(data)