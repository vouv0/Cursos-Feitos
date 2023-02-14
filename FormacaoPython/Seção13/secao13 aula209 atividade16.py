import numpy

def remove_numero_negativo(array):
    filtro = array >= 0
    return array[filtro]


teste = numpy.array([1,-2,3,-4,5,6])

print(remove_numero_negativo(teste))
