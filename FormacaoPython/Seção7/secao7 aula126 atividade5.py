class Veiculo:
    def __init__(self, peso, numero_rodas, potencia):
        self.peso = peso
        self.numero_rodas = numero_rodas
        self.potencia = potencia

    def __lt__(self, outro):
        return self.potencia < outro.potencia
    def __gt__(self, outro):
        return self.potencia > outro.potencia

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

print(f'Carro é mais potente que o Onibus: {carro > onibus}')
print(f'Onibus é mais potente que a Moto: {onibus > moto}')
print(f'Moto é menos potente que o Onibus: {moto < onibus}')
print(f'Moto mais potente que o Carro: {moto > carro}')
