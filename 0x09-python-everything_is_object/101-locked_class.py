#!/usr/bin/python3
# 101-locked_class.py

class LockedClass:
    """ Define Class """
    def __setattr__(self, name, value):
        if name != 'first_name':
            err_msg = "'LockedClass' object has no attribute '{}'"
            raise AttributeError(err_msg.format(name))
