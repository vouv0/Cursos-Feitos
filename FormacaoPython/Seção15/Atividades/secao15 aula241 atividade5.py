import matplotlib.pyplot as plt
import numpy as np

destinos = np.array(['China', 'Estados Unidos', 'Europa', 'Outros'])
dados = np.array([30, 40, 20, 10])
cores = np.array(['r', 'g', 'b', 'y'])

text_props = {
    'color': 'black',
    'style': 'oblique',
    'size': 7
}

plt.pie(dados, labels=destinos, colors=cores, shadow=True,
        startangle=90, radius=0.9,
        textprops=text_props, autopct=lambda value: f'{value:.2f} %')
plt.title('Destinos de exportações do Brasil')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()
