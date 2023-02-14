def testa_objeto(obj):
    if isinstance(obj, (int, float, bool, str)):
        print('Objeto por valor.')
    else:
        print('Objeto por referencia.')


class Objeto:
    def __init__(self):
        pass


objeto = Objeto()
valor = 3

testa_objeto(objeto)
testa_objeto(valor)
