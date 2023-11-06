#!/usr/bin/python3
# 7-base_geometry.py
"""Defines a class-BaseGeometry."""


class BaseGeometry:
    """A base geometry class for all geometrical objects in the program."""
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if the input is an integer number."""
        if type(value) != int:
            raise  TypeError("the message <name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than zero.")
