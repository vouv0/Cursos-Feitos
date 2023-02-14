#Personalizando a linha do grafico

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x * 5 +1

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Gráfico de vendas')

#solid, dashed, dotted, dashdot
plt.plot(x, y, c='g', linewidth='6.5', linestyle='dashdot')
plt.show()
