#!/usr/bin/python3
# 3-square.py
"""class Square"""


class Square:
    """ square class definition"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square's area"""
        return self.__size ** 2 
