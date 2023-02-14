import numpy

def ordena_par_unicos(array):
    filtro = (array % 2 == 0)
    return numpy.unique(array[filtro])


teste = numpy.random.randint(0,11,20)

print(ordena_par_unicos(teste))
