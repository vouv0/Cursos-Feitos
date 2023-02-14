import numpy

def divide_array(a, n):
    matriz = numpy.array_split(a, n)
    matriz = numpy.abs(matriz)
    return matriz


teste = numpy.array([1,2,-3,4,-5,6])

print(divide_array(teste, 3))
