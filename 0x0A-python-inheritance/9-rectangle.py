#!/usr/bin/python3
# 9-rectangle.py
"""Defines a class-BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with length and width attributes."""
    def __init__(self, width, height):
        """ Intialize a new Rectangle. """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
    
    def str(str):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
