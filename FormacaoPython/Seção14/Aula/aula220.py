#Removendo colunas

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#data.drop(columns=['Idade'], inplace=True)
#print(data)

#Drop pelo index
data.drop(columns= data.columns[[0, 1]], axis=1, inplace=True)
print(data)
