import pandas as pd
import numpy as np

#Serie com Pandas
minha_serie = pd.Series([1,2,3,4,5], dtype='i4', name='Meus números', index=['Um', 'Dois', 'Tres', 'Quatro', 'Cinco'])
minha_serie['Seis'] = 6

print(minha_serie)

#Serie com Pandas e usando NumPy

array = np.array([45.6, 50.3, 65.7, 82.3, 98.5])
pesos = pd.Series(array, index=['Ana', 'João', 'Maria', 'Vitor', 'José'])

print(f'\n{pesos}')
