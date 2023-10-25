#!/usr/bin/python3
# 6-square.py
""" Class File """


class Square:
    """ Square CLass Definition """

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter position"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter Position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter Position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square's area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' using the position attribute."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
