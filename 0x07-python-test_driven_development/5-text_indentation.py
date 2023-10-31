#!/usr/bin/python3

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chr = 0
    while chr < len(text) and text[chr] == ' ':
        chr += 1

    while chr < len(text):
        print(text[chr], end="")
        if text[chr] == "\n" or text[chr] in ".?:":
            if text[chr] in ".?:":
                print("\n")
            chr += 1
            while chr < len(text) and text[chr] == ' ':
                chr += 1
            continue
        chr += 1
