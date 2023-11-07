#!/usr/bin/python3
# 11-square.py
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """  str function """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
