#grafico de dispersão - mais de uma série
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10, size=10)
y = np.random.randint(10, size=10)
x2 = np.random.randint(10, size=10)
y2 = np.random.randint(10, size=10)

plt.scatter(x, y, label='Meninos')
plt.scatter(x2, y2, label='Meninas')
plt.title('Gráfico de Dispersão')
plt.legend()
plt.show()
