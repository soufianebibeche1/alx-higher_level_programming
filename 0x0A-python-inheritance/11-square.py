#!/usr/bin/python3
# 10-square.py
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square is a rectangle with equal sides and opposite angles."""

    def __init__(self, size):
        """ initialisie size and validate """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """  str function """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
