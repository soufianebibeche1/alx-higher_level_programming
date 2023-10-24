#!/usr/bin/python3
# 4-square.py
""" Class File """


class Square:
    """ Square CLass Definition """
    def __init__(self, size=0):
        """ Constructor """
        self.size = size

    @property
    def size(self):
        """ Getter """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square's area"""
        return self.__size ** 2
