#!/usr/bin/python3
# 1-my_list.py:wq
""" Class MyList"""


class MyList(list):
    """ Class MyList """
    def print_sorted(self):
        """A list class that overrides some of the built-in methods."""
        print(sorted(self))
