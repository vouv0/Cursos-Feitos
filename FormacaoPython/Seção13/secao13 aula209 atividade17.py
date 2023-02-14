import numpy

def intervalo_array(n_inicial, n_final, array):
    filtro = (array >= n_inicial) & (array <= n_final)
    return array[filtro]


teste = numpy.array([4,2,3,9,5,6])

print(intervalo_array(2,5,teste))
