import numpy

def tem_numero_negativo(array):
    return numpy.any(array < 0)


teste = numpy.array([1,2,3,-4,5,6])

print(tem_numero_negativo(teste))
