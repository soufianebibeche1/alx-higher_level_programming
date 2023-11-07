#!/usr/bin/python3
# 1-write_file.py
""" Python"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written."""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
