#!/usr/bin/python3
""" Test case for Reactangle """
import unittest
import inspect
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests the Rectangle class for documentation and style"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""

        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)


    def test_module_docstring(self):
        """Tests for the module docstring"""
        from models import rectangle
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)
