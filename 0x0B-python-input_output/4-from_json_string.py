#!/usr/bin/python3
# 4-from_json_string.py
""" Python"""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string."""
    return json.loads(my_str)
