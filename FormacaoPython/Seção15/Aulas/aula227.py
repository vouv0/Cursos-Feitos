# Personalizando titulos e fontes
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 2

plt.xlabel('Vendas') #nome da legenda no eixo x
plt.ylabel('Temperatura') #nome da legenda no eixo y
plt.title('Gráfico de Vendas', y=0.9, loc='left', x=0.02)

plt.plot(x, y)
plt.show()
