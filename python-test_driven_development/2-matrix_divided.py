#!/usr/bin/python3
'''A division matrix'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix'''
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    row_size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError('Each row of the matrix must have the same size')

        status = all(type(element) in set([int, float]) for element in row)
        if status is False:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = map(lambda x; list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(new)
