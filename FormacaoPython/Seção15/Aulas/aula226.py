#mais elementos em um grafico
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1, 2, 3, 4, 5])
y1 = x1 * 2

x2 = np.array([5, 10, 15])
y2 = x2 * 2

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()
