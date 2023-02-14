#grafico de barras

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

#plt.bar(x, y, color='g', width=0.5) #barras na vertical
plt.barh(x, y, color='g', height=0.5) #barras na horizontal

plt.show()
