import matplotlib.pyplot as plt
import numpy as np

anos = np.array(['2016', '2017', '2018', '2019', '2020', '2021', '2022'])
valor_dolar = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])
pib = np.array([8710.50, 9928.50, 9151.58, 8897.29, 6795.32, 7500.21, 7542.34])


plt.subplot(1, 2, 1)
plt.xlabel('Ano')
plt.ylabel('Real')
plt.title('Valor do Real em relação ao Dólar')
plt.plot(anos, valor_dolar, color='green', marker='o')

plt.subplot(1, 2, 2)
plt.xlabel('Ano')
plt.ylabel('PIB')
plt.title('PIB per Capita do Brasil em Dólar')
plt.plot(anos, pib, color='blue', marker='s')

plt.subplots_adjust(hspace=0.8, wspace=0.4)
plt.suptitle('Situação Economica do Brasil')
plt.tight_layout()

plt.show()
