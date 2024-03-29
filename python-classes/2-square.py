#!/usr/bin/python3


'''Define the class Square'''


class Square:
    '''Class with size attribute'''
    def __init__(self, size=0):
        '''Initialise Square'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
