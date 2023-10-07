#!/usr/bin/python3

def max_integer(my_list=[]):
    max_item = 0
    i = 0
    while i < len(my_list) - 1:
        if my_list[i] > max_item:
            max_item = my_list[i]
        i = i + 1

    return max_item
