#Atualizando valores

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Mudando o valor da celula pelo nome
#data.at['Diego', 'Idade'] = 56
#print(data)

#Mudando o valor da celula pelo indice
#data.iat[2,0] = 56
#print(data)


#Alterando mais de um valor em um intervalo
#data.loc['Cristiano', 'Idade':'Profissão'] = (45, 'Dev')
#print(data)

#Alterando mais de um valor por colunas especificas
data.loc['José', ['Idade', 'Altura']] = (65, 1.78)
print(data)
