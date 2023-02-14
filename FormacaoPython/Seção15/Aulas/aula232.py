#Aprimorando com linhas de grade
import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(1, 100)
y1 = x1 ** 2
plt.plot(x1, y1, color='r')
plt.grid(c='b', ls='dotted', lw=1.5)
#plt.xticks([1, 2, 3, 4, 10, 20, 40, 80, 120, 180])
plt.show()
