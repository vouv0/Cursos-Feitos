# histogramas
import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75, 1.56, 1.47, 1.68, 1.72, 1.83, 1.90, 1.81, 1.73, 1.66])
plt.hist(alturas, color='g', edgecolor='b', bins=[1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2])
#plt.hist(alturas, color='g', edgecolor='b', bins=7) #gera automaticamente 7 barras
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuição das alturas')
plt.show()
