import numpy

def concat_array(array1, array2, array3):
    if array1.shape != array2.shape or array1.shape != array3.shape:
        raise Exception('Formatos diferentes')

    return numpy.concatenate((array1,array2,array3))


arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])
arr3 = numpy.array([7, 8, 9])

print(concat_array(arr1,arr2,arr3))
