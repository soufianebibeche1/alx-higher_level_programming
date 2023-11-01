#!/usr/bin/python3
""" Print Square """


def print_square(size):
    """Print a square with the # character."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
