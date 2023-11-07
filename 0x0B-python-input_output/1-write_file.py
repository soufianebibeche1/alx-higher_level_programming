#!/usr/bin/python3
# 1-write_file.py
""" Python"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_chars = file.write(text)
    return nb_chars
