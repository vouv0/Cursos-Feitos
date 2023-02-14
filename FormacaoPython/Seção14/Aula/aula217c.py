#Atualizando valores

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Mudando todos os valores atraves de uma condição
data.loc[(data['Idade'] < 40), 'Altura'] = 1.99
print(data)
