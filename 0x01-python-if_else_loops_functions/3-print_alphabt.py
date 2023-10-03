#!/usr/bin/python3

for character in range(ord("a"), ord("z") + 1):
    if character == ord("q") or character == ord("e"):
        continue
    print("{}".format(chr(character)), end="")
