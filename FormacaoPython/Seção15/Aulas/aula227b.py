# Personalizando titulos e fontes
#mudando cores e estilo de fontes
import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'cmb10',
    'color': 'blue',
    'weight': 'bold',
    'size': 16
}
font_props2 = {
    'family': 'DejaVu Sans',
    'color': 'green',
    'weight': 'normal',
    'size': 10
}

x = np.arange(-10, 10, 0.1)
y = x ** 2

#adiciona um texto no grafico com as cordenadas
plt.text(-2.5, 50, 'É uma parábola', fontdict=font_props2)


plt.xlabel('Vendas', fontdict=font_props)
plt.ylabel('Temperatura', fontdict=font_props)
plt.title('Grafico de Vendas', fontdict=font_props)

plt.plot(x, y)
plt.show()
