#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]  # exclude script name

    sum = 0
    for arg in arguments:
        sum = sum + int(arg)

    print(sum)
