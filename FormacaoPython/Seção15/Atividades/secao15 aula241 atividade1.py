import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y = 5 * x + 1

plt.plot(x, y, c='b', marker='s', markerfacecolor='r')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Função: y = 5x+1')
plt.show()
