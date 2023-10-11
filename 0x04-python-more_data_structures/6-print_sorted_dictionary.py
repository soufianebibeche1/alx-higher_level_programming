#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorte = sorted(a_dictionary.keys())

    for key in dict_sorte:
        value = a_dictionary[key]
        print(f"{key}: {value}")
