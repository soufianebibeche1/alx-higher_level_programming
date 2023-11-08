#!/usr/bin/python3
# 1-my_list.py
""" Python """


class MyList(list):
    """ Define a MyList class """

    def print_sorted(self):
        """ Print the list in sorted order """
        print(sorted(self))
