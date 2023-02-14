#Legendas e transparencia

import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0, 20, 0.5)
y1 = np.cos(x1)

x2 = np.arange(0, 20, 0.5)
y2 = np.cos(x2)*2

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Gráfico de vendas')


plt.plot(x1, y1, c='b', lw='3.5', ls='dashed', label='Vendas')
plt.plot(x2, y2, c='g', lw='2.5', ls='dashdot', label='Temperatura', alpha=0.5)
plt.legend(loc='lower right') # adiciona legenda
plt.show()
