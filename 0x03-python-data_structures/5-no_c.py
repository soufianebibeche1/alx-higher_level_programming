#!/usr/bin/python3

def no_c(my_string):
    strwoc = ""
    for character in my_string:
        if character != "c" and character != "C":
            strwoc = strwoc + character
    my_string = strwoc
    return my_string
