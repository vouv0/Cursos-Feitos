#Tratando valores Nulos e Ordenando

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')
data.loc['Roger', 'Idade'] = None #colocando um valor nulo


#Ordenando de forma Crescente a idade
#copia = data.sort_values('Idade', ascending=True, inplace=False)
#print(copia)

#Ordenando de forma Decrescente a idade
#copia = data.sort_values('Idade', ascending=False, inplace=False)
#print(copia)

#Ordenando com os valores Nulos no começo ou no fim
#copia = data.sort_values('Idade', ascending=False, inplace=False, na_position='first') #Começo
copia = data.sort_values('Idade', ascending=False, inplace=False, na_position='last') #Fim
print(copia)
