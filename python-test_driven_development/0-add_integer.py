#!/usr/bin/python3
'''Add integer module'''


def add_integer(a, b=98):
    '''A function that adds two integers'''
    if a != int and a != float:
        raise TypeError("a must be an integer")
    if b != int and b != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
