#!/usr/bin/python3
'''This module takes in a division matrix'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix'''

    TypeM = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) != list:
        raise TypeError(TypeM)

    row_size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(TypeM)

        if row_size is None:
            row_size = len(row)
        elif row_size != len(row):
            raise TypeError('Each row of the matrix must have the same size')

        status = all(type(element) in set([int, float]) for element in row)
        if status is False:
            raise TypeError(TypeM)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return list(new)
