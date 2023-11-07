#!/usr/bin/python3
# 2-append_write.py
""" Python"""


def append_write(filename="", text=""):
    """Append a string to a file ,return the number of chars written."""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
