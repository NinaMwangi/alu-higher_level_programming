#!/usr/bin/python3


'''Define a class Rectangle'''


class Rectangle:
    '''Instantiating the class'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        '''Destructor'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Get the width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''Set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''Set the height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''return the area of the rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Calculating the perimeter'''
        if self.__height == 0 or self.__width == 0:
            return (0)

        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        w, h = self.__width, self.__height
        if w == 0 or h == 0:
            return ''

        return '{}{}'.format(('#' * w + '\n') * (h - 1), '#' * w)

    def __repr__(self):
        w, h = self.__width, self.__height
        return 'Rectangle({}, {})'.format(w, h)
