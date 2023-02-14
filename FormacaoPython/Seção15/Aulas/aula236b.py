#grafico de barras

import matplotlib.pyplot as plt
import numpy as np

valores_esqurda = np.arange(0, 6)
valores_direita = np.arange(6, 0, -1)
#ys = np.arange(6)
xs = np.arange(6)

#plt.barh(ys, valores_esqurda, color='y')
#plt.barh(ys, -valores_direita, color='c')
plt.bar(xs, valores_esqurda, color='y')
plt.bar(xs, -valores_direita, color='c')

plt.legend(['a', 'b'])

plt.title('Gráfico de barras dividido')
plt.ylabel('Valores de Y')
plt.xlabel('Valores esquerda vs direita')

plt.show()
