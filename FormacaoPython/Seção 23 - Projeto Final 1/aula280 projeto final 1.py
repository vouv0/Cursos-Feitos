from numpy import std, cov, var, sqrt, mean, min, max
import matplotlib.pyplot as plt


class RegressaoLinear:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def correlacao(self):
        covariacao = cov(self.x, self.y, bias=True)[0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)
        return covariacao / (sqrt(variancia_x * variancia_y))

    def inclinacao(self):
        stdx = std(self.x) #Desvio padão de x
        stdy = std(self.y) #Desvio padão de y
        return self.correlacao() * (stdy/stdx)

    def interceptacao(self):
        media_x = mean(self.x)
        media_y = mean(self.y)
        return media_y - (self.inclinacao() * media_x)

    def previsao(self, var_independente):
        return self.interceptacao() + (self.inclinacao() * var_independente)

    def grafico(self, titulo='Regressao Linear', eixo_x='Eixo x', eixo_y='Eixo y'):
        plt.xlabel(eixo_x)
        plt.ylabel(eixo_y)
        plt.title(titulo)

        plt.scatter(self.x, self.y)
        x_min = min(self.x)
        x_max = max(self.x)
        x_reta = [x_min, x_max]
        y_reta = [self.previsao(x_min), self.previsao(x_max)]
        plt.plot(x_reta, y_reta, c='r')

        plt.show()


idades = [18, 23, 25, 33, 34, 43, 48, 51, 58, 63, 67]  # idades
custo = [871, 1100, 1393, 1654, 1915, 2100, 2356, 2698, 2959, 3000, 3100]  # custo

regressao = RegressaoLinear(idades, custo)
preve = regressao.previsao(54)
teste = regressao.grafico('Plano de Saúde', 'Idades', 'Custo')
