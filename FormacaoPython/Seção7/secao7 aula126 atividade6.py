class Negativo:
    def __init__(self, numero):
        self.__numero = 0
        self.numero = numero

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        if numero <= 0:
            self.__numero = numero

    def __lt__(self, outro):
        return self.__numero < outro.__numero
    def __gt__(self, outro):
        return self.__numero > outro.__numero
    def __sub__(self, outro):
        sub = self.__numero - outro.__numero
        if sub > 0:
            sub = 0
        return sub

num = Negativo(-10)
num2 = Negativo(-20)
num3 = Negativo(10)
print(num.numero, num2.numero, num3.numero)
print(num > num2)
print(num - num2)
