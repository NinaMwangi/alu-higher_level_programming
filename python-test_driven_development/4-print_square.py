#!/usr/bin/python3
'''This module prints a square'''


def print_square(size):
    '''This function prints squares using the hash symbol'''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
