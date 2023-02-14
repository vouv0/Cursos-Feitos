#Adicionando marcadores
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 19)
y = -x ** 4
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico da função y = -x**4')
plt.plot(x, y, c='orange', lw='1.5', marker='D',
         markersize=4, markerfacecolor='red', markeredgecolor='green')
plt.show()
