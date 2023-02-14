import numpy

matriz = numpy.random.randint(0, 5, (4, 9))
print(matriz)
matriz2 = matriz.flatten()
print(matriz2)
matriz3 = matriz.reshape(6,6)
print(matriz3)
