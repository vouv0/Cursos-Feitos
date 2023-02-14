#Tratando valores Nulos e Ordenando

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')
data.loc['Roger', 'Idade'] = None #colocando um valor nulo

#verificando se ha valor nulo
#print(data.isnull())
#print(pd.isnull(data))
#data.notnull() #para valores NÃO nulos

#verificando apenas uma coluna
#print(pd.isnull(data['Idade']))

#utilizando mascara
mask = pd.notnull(data['Idade'])
print(data[mask])

