#!/usr/bin/python3
# 1-my_list.py
"""inherited list class MyList."""


class MyList(list):
    """Implements sorted print for the list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
