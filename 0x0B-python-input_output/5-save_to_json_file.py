#!/usr/bin/python3
# 5-save_to_json_file.py
""" Python"""
import json

def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
