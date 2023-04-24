#!/usr/bin/python3
"""Class Base module"""


Class Base:
    """Parent class for this project"""

    # Number of instantiated Bases.
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id
