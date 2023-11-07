#!/usr/bin/python3
# 0-read_file.py
""" Python"""


def read_file(filename=""):
    """Read and print the contents of a text file (UTF8).

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
