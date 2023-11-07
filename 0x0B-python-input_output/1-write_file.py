#!/usr/bin/python3
# 1-write_file.py
""" Python"""


def write_file(filename="", text=""):
    """Write a string to a file ,return the number of chars written."""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
