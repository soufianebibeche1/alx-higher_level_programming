#!/usr/bin/python3
# 1-my_list.py:wq
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """A list class that overrides some of the built-in methods."""
        print(sorted(self))
