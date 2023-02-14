#Removendo linhas

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Drop por copia
#data2 = data.drop(index=['Roger', 'Diego'])
#print(data2)

#Drop no original
#data.drop(index=['Roger', 'Diego'], inplace=True)
#print(data)

#Removendo com condição
data.drop(index=data[data['Altura'] >= 1.7].index, inplace=True)
print(data)
