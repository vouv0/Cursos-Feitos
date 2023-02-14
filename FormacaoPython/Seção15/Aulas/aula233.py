#Aplicando estilos
import matplotlib.pyplot as plt
import numpy as np


#print(plt.style.available) #mostra os estilos disponiveis

x1 = np.arange(1, 100)
y1 = x1 ** 2
plt.style.use('classic') #aplica o estilo
plt.grid(c='b')
plt.plot(x1, y1, color='r')
plt.show()
