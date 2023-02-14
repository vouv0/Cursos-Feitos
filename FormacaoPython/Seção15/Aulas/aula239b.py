#Gráfico de pizza - Destacando os dados do grafico
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

plt.figure(figsize=(7, 7)) #muda o tamanho da figura
#diminuindo o raio e 'explodindo' os pedaços do grafico
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90,
        radius=0.8, explode=offsets, wedgeprops=edge_props)
plt.title('Distribuição de Classes')
plt.legend(classes, loc='upper left')
plt.show()
