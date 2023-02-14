#Data Frames

import pandas as pd

#nomes = ['Vitor', 'João', 'Maria', 'Ana']
#data_frame = pd.DataFrame(nomes)
#print(data_frame)

#Nomeando linhas e colunas
numeros = [['1','2','3','4','5'],
           ['6','7','8','9','10'],
           ['11','12','13','14','15'],
           ['16','17','18','19','20']
           ]

data_frame2 = pd.DataFrame(numeros, columns=['a','b','c','d','e'], index=['w','x','y','z'])
print(data_frame2)
