#!/usr/bin/python3
# base.py
""" Python: 0x0C. Python - Almost a circle """


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
