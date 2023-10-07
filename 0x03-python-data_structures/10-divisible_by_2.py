#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boollist = []
    for item in my_list:
        if item % 2 == 0:
            boollist.append(True)
        else:
            boollist.append(False)
    return boollist
