import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.6, 1.62, 1.65, 1.7, 1.7, 1.75, 1.8,
                    1.85, 1.9, 1.9, 1.95, 2])
pesos = np.array([60, 61, 64, 67, 70, 73, 75, 80, 85,
                  90, 85, 95])
cores = np.array(['r', 'r', 'g', 'b', 'y', 'r', 'b',
                  'b', 'brown', 'y', 'r', 'y'])


plt.scatter(alturas, pesos, c=cores, marker='o')
plt.ylabel('Peso')
plt.xlabel('Altura')
plt.title('Relação Peso x Altura')
plt.show()
