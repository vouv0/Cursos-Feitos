#Slices de colunas e Mascaras

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#colunas = data.iloc[:, 1:3]
#print(colunas)

#colunas = data.loc[:, 'Idade':'Profissão']
#print(colunas)


#Mascaras
mask = data['Idade'] < 50 #mostra os valores com a condição
print(mask)

nova_data = data[mask]
print(nova_data)
