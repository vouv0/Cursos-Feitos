#Gráfico de pizza
import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa', 'Classe média', 'Classe alta'])
dados = np.array([70, 30, 10])
cores = np.array(['r', 'g', 'y'])

plt.figure(figsize=(7, 7)) #muda o tamanho da figura
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90)
plt.title('Distribuição de Classes')
plt.legend(classes, loc='upper left')
plt.show()
