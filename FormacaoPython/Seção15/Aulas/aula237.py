#graficos empilhados
import matplotlib.pyplot as plt
import numpy as np

xs = np.array(['Janeiro', 'Fevereiro', 'Março', 'Abril'])
time1 = np.array([5, 10, 15, 20])
time2 = np.array([2, 6, 4, 10])
time3 = np.array([6, 13, 5, 2])
time4 = np.array([1, 4, 11, 7])

#barras verticais
#plt.bar(xs, time1, color='red', width=0.5)
#plt.bar(xs, time2, bottom=time1, color='green', width=0.5)
#plt.bar(xs, time3, bottom=time1+time2, color='yellow', width=0.5)
#plt.bar(xs, time4, bottom=time1+time2+time3, color='blue', width=0.5)

#barras horizontais
plt.barh(xs, time1, color='red')
plt.barh(xs, time2, left=time1, color='green')
plt.barh(xs, time3, left=time1+time2, color='yellow')
plt.barh(xs, time4, left=time1+time2+time3, color='blue')

plt.title('Rendimento no esporte')
plt.xlabel('Meses')
plt.ylabel('Gols')
plt.legend(['Time1', 'Time2', 'Time3', 'Time4'])
plt.show()
