#!/usr/bin/python3
# 7-add_item.py
""" Python """
import sys
import json
from os import path


# Define the file name
filename = "add_item.json"

# Check if the file exists, and create an empty list if it doesn't
if path.isfile(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        my_list = json.load(file)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to a JSON file
with open(filename, mode="w", encoding="utf-8") as file:
    json.dump(my_list, file)
