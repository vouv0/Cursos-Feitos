import numpy

def ordena_par(array):
    filtro = (array % 2 == 0)
    return numpy.sort(array[filtro])


teste = numpy.array([4,2,3,9,5,6,7,8,0])

print(ordena_par(teste))
