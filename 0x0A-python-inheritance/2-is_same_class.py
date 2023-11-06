#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object belongs to the given class or not."""
    if type(obj) is a_class:
        return True
    return False
