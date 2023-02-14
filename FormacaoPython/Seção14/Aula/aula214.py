#Importando dados

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')
#print(data)
#print('')
#print(data.loc['Diego'])


#Propriedades do DataFrame
print(len(data.columns))
#print(data.columns)
print(len(data.index))
#print(data.index)

print(data.shape) #mostra a quandidade de linhas e colunas
