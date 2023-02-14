#Ajustando multiplos graficos
import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0, 20, 0.5)
y1 = np.cos(x1)

x2 = np.arange(0, 20, 0.5)
y2 = np.cos(x2)*2

plt.subplot(2, 2, 1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A primeira função')
plt.plot(x1, y1, c='g', label="y=cos(x)")
plt.legend(loc='lower right')
plt.ylim(-3, 3)

plt.subplot(2, 2, 2)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A segunda função')
plt.plot(x2, y2, c='b', label="y=cos(x)*2")
plt.legend(loc='lower right')
plt.ylim(-3, 3)

plt.subplot(2, 2, 3)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A primeira função')
plt.plot(x1, y1, c='y', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 3)

plt.subplot(2, 2, 4)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A segunda função')
plt.plot(x2, y2, c='r', label='y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3, 3)

plt.subplots_adjust(hspace=0.8, wspace=0.4)
plt.suptitle('Meus gráficos')

plt.show()
