#!/usr/bin/python3
# 7-base_geometry.py
"""Defines a class-BaseGeometry."""


class BaseGeometry:
    """A base geometry class for all geometrical objects in the program."""
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
