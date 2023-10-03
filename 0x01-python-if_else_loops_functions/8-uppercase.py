#!/usr/bin/python3

def islower(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    else:
        return False


def uppercase(str):
    result = ""
    for char in str:
        if islower(char):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        result += uppercase_char
    print(result)
