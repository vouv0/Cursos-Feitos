import numpy

def array_divisivel_por_3(array):
    return numpy.where(array % 3 == 0)[0]


teste = numpy.array([1,2,3,9,4,5,6])

print(array_divisivel_por_3(teste))
