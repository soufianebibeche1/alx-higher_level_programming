#!/usr/bin/python3
"""Module defining the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """The Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position (default is 0).
            y (int): Y-coordinate of the rectangle's position (default is 0).
            id (int): If provided, assign it to the public instance attribute id.
                      If not provided, the id will be automatically assigned by the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Args:
            value (int): The value to set as the width.
        """
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Args:
            value (int): The value to set as the height.
        """
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute.

        Args:
            value (int): The value to set as the x-coordinate.
        """
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute.

        Args:
            value (int): The value to set as the y-coordinate.
        """
        self.__y = value
