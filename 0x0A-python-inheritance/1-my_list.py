#!/usr/bin/python3
# 1-my_list.py
"""an inherited list class MyList."""


class MyList(list):
    """Implements sorted print for built-in list."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
