#!/usr/bin/python3
# 2-square.py
"""class Square"""


class Square :
    """ square class definition"""
    def __init__(self, size):
        if not isinstance(size, int)
            raise TypeError("size must be an integer")
        elif size < 0:
            raiise ValueError("size must be >= 0")
        else:
            self.size = size
