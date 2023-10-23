#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        cpt = 0
        for i in range(x):
            print(my_list[i], end="")
            cpt += 1
    except IndexError:
        pass
    print()
    return cpt
