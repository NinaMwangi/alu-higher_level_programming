#!/usr/bin/python3
"""Module for the subclass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Sub class in the module"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class"""
        super().__innit__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getting the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting the value"""
        return self.__height
       
    @width.setter
    def height(self, value):
        """Setting the value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the value"""
        return self.__x

    @width.setter
    def x(self, value):
        """Setting the value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the value"""
        return self.__y

    @width.setter
    def y(self, value):
        """Setting the value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value         
