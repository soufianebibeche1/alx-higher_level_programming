#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nb_args = len(argv) - 1 #exclude script name

    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb_args))

    for i in range(1, nb_args + 1):
        print("{}: {}".format(i, argv[i]))
