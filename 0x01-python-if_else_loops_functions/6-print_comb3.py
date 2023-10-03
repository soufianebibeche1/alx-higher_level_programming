#!/usr/bin/python3

for nb1 in range(0, 10, 1):
    for nb2 in range(nb1 + 1, 10, 1):
        if nb1 == 8 and nb2 == 9:
            print("{:d}{:d}".format(nb1, nb2))
        else:
            print("{:d}{:d}, ".format(nb1, nb2), end="")
