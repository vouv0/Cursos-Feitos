import numpy

matriz = numpy.random.randint(1, 5, (3, 3))
print(matriz)

for i in matriz:
    print(numpy.sum(i))
