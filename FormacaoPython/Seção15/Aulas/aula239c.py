#Gráfico de pizza - Adicionando texto
import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa', 'Classe média', 'Classe alta'])
dados = np.array([70, 30, 10])
cores = np.array(['r', 'g', 'y'])
offsets = np.array([0.03, 0.03, 0.2]) #valores da distancia do offset

edge_props = {
    'linewidth': 1,
    'edgecolor': 'black',
    'linestyle': 'solid'
}

text_props = {
    'color': 'black',
    'style': 'oblique',
    'size': 10
}

plt.figure(figsize=(7, 7))
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90,
        radius=0.8, explode=offsets, wedgeprops=edge_props,
        textprops=text_props, autopct=lambda value: f'{value:.2f} %') #função lambda pra ajeitar o texto
plt.title('Distribuição de Classes')
plt.legend(classes, loc='upper left')
plt.show()
