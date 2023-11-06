#!/usr/bin/python3
""" Class MyList"""


class MyList(list):
    """A list class that overrides some of the built-in methods."""
    def print_sorted(self):
        print(sorted(self))
