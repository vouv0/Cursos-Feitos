class Carro:
    def __init__(self, potencia, alcance):
        self.potencia = potencia
        self.alcance = alcance


carro1 = Carro(100,200)
carro2 = Carro(200, 350.5)
print(f'Potencia do carro1: {carro1.potencia} cavalaos')
print(f'Alcance do carro1: {carro1.alcance} km/l')
print(f'Potencia do carro2: {carro2.potencia} cavalos')
print(f'Alcance do carro2: {carro2.alcance} km/l')
