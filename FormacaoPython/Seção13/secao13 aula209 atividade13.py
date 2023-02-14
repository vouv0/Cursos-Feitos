import numpy

def array_positivo(array):
    return len(numpy.where(array >= 0)[0])


teste = numpy.array([1,2,3,-4,-5,-6])

print(array_positivo(teste))
