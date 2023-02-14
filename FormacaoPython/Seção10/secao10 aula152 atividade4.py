class Fatorial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        self.numero_atual = self.x
        return self


    @staticmethod
    def calc_fatorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def __next__(self):
        if self.numero_atual == (self.y + 1):
            raise StopIteration
        resultado = Fatorial.calc_fatorial(self.numero_atual)
        self.numero_atual += 1
        return resultado


for i in Fatorial(1, 10):
    print(i)
