#Multiplos graficos
import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0, 20, 0.5)
y1 = x1 * 2

x2 = np.arange(0, 20, 0.5)
y2 = np.sin(x2)

plt.subplot(1, 2, 1)
plt.title('A primeira função')
plt.plot(x1, y1, c='g')

plt.subplot(1, 2, 2)
plt.title('A segunda função')
plt.plot(x2, y2, c='b')

plt.show()
