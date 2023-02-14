import matplotlib.pyplot as plt
import numpy as np

anos = np.array(['2016', '2017', '2018', '2019', '2020', '2021', '2022'])
valor_dolar = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])

plt.bar(anos, valor_dolar, color='green')
plt.xlabel('Ano')
plt.ylabel('Real')
plt.title('Valor do Real em relação ao Dólar')
plt.show()
