#!/usr/bin/python3
"""Test Base class module"""
import unittest


from models import base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_module_doc(self):
        """Module documentation"""
        doc = base.Base.__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """Class documentation"""
        doc = base.Base.__doc__
        self.assertGreater(len(doc), 1)

    def test_constructor_doc(self):
        """Constructor documentation"""
        doc = base.Base.__doc__
        self.assertGreater(len(doc), 1)
