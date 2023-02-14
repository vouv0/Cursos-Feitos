# Comparação de histogramas
import matplotlib.pyplot as plt
import numpy as np

alturas_mundial = np.random.normal(loc=175, scale=11, size=1000)/100
alturas_brasil = np.random.normal(loc=185, scale=9, size=1000)/100

plt.hist(alturas_mundial, color='g', edgecolor='b', bins=7, alpha=0.5)
plt.hist(alturas_brasil, color='y', edgecolor='r', bins=7, alpha=0.5)
plt.legend(['Altura Mundial', 'Altura Brasil'])
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuição das alturas')
plt.show()
