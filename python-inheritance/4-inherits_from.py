#!/usr/bin/python3
'''Module for Task 4'''


def inherits_from(obj, a_class):
    '''Return True if obj instance is inherited directly/indirectly, False'''
    return issubclass(type(obj), a_class) and type(obj) != a_class
