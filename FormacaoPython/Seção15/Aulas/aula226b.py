#limitando os eixos do gráfico
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(1, 10)
y1 = x1 * 2

x2 = np.arange(1, 10)
y2 = x2 ** 2

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlim(0, 10) # limita o eixo x
plt.ylim(-1, 50) # limita o eixo y
plt.show()
