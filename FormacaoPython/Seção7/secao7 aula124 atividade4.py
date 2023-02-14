class Veiculo:
    def __init__(self, peso, numero_rodas, potencia):
        self.peso = peso
        self.numero_rodas = numero_rodas
        self.potencia = potencia

    def distancia_percorrida(self):
        return (self.peso / self.potencia) * 1000

class Onibus(Veiculo):
    def __init__(self, peso, numero_rodas, potencia):
        Veiculo.__init__(self, peso, numero_rodas, potencia)

class Carro(Veiculo):
    def __init__(self, peso, numero_rodas, potencia):
        Veiculo.__init__(self, peso, numero_rodas, potencia)

class Moto(Veiculo):
    def __init__(self, peso, numero_rodas, potencia):
        Veiculo.__init__(self, peso, numero_rodas, potencia)

onibus = Onibus(1000, 6, 400)
carro = Carro(300, 4, 100)
moto = Moto(100, 2, 50)

print(f'Ônibus: Distancia percorrida {onibus.distancia_percorrida()}')
print(f'Carro: Distancia percorrida {carro.distancia_percorrida()}')
print(f'Moto: Distancia percorrida {moto.distancia_percorrida()}')
