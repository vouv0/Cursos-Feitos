class Veiculo:
    def __init__(self, peso, numero_rodas, potencia):
        self.peso = peso
        self.numero_rodas = numero_rodas
        self.potencia = potencia

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

print(f'Ônibus: Peso {onibus.peso} / Rodas {onibus.numero_rodas} / Potencia {onibus.potencia}')
print(f'Carro: Peso {carro.peso} / Rodas {carro.numero_rodas} / Potencia {carro.potencia}')
print(f'Moto: Peso {moto.peso} / Rodas {moto.numero_rodas} / Potencia {moto.potencia}')
