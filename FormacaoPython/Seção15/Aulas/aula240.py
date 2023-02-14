#grafico de dispersão
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')
x = np.arange(0, 10)
y = np.array([1, 3, 4, 7, 12, 5, 9, 11, 13, 10])

cores = np.array(['r', 'r', 'g', 'b', 'y', 'b', 'brown', 'pink', 'y', 'r'])

plt.scatter(x, y, c=cores, marker='o')
plt.title('Gráfico de Dispersão')
plt.show()
