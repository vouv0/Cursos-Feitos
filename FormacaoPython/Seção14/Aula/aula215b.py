#Acessando valores individuais e Slicing

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#print(data['Idade'])

#idade = data['Idade']
#print(idade[2])
#print(idade['Diego'])


#mais de uma coluna
print(data[['Idade','Altura']])
