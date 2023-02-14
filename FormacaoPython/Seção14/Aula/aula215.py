#Acessando valores individuais e Slicing

import pandas as pd

data = pd.read_csv('pessoas.csv', index_col='Nome')

#acessando atraves do nome do indice
#print(data.loc['Roger']['Idade'])
#print(data.loc['Roger'][0])

#acessando atraves da posição do indice
#print(data.iloc[0]['Idade'])
#print(data.iloc[0][0])


#Slicing
#print(data.loc['Cristiano':'Jeferson']) #nome do indice
print(data.iloc[1:4]) #posição do indice
