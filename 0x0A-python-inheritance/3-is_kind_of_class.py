#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines an inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """Returns True if obj's class is the same as or inherits from a_class; otherwise False."""
    if isinstance(obj,a_class):
        return True
    return False
