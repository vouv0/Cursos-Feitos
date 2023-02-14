#Agrupando valores

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#Adicionando valores
data.loc['Ana'] = (22, 'Programador', 1.65)
data.loc['João'] = (42, 'Programador', 1.74)
data.loc['Joaquim'] = (26, 'Programador', 1.78)
data.loc['Marta'] = (32, 'Medico', 1.67)
data.loc['Vitor'] = (28, 'Medico', 1.83)


#agrupando de acordo com a Profissao
#grupos = data.groupby('Profissão')
#for indice, grupo in grupos:
#    print('')
#    print(indice)
#    print(grupo)

#Criando um dataframe atraves de um grupo
#print(grupos.get_group('Programador'))


#Agrupando com mais colunas e mostrando dados estatisticos
grupos = data.groupby(['Profissão', 'Idade'])
print(grupos.describe())
