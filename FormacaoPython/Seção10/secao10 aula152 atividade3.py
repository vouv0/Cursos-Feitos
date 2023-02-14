class Tabuada:
    def __init__(self, numero):
        self.numero = numero
        self.numero_max = 10

    def __iter__(self):
        self.numero_atual = 0
        return self

    def __next__(self):
        if self.numero_atual <= self.numero_max:
            resultado = self.numero_atual * self.numero
            self.numero_atual += 1
            return resultado
        else:
            raise StopIteration


tabuada = Tabuada(5)
for v in tabuada:
    print(f'{v}')
