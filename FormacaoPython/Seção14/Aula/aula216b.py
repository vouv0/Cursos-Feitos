#Slices de colunas e Mascaras

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Mascaras com 2 condições
nova_data = data[(data['Idade'] > 40) & (data['Altura'] > 1.75)]
print(nova_data)
