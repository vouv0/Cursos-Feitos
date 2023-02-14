#Importando dados - iteração dos dados

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#for indice, linha in data.iterrows():
#    print(indice, linha[0], linha[1], linha[2])

#for coluna in data:
#    print(coluna)

#print(data['Idade']) #acessando atraves do nome da coluna

for coluna in data:
    print(data[coluna])
