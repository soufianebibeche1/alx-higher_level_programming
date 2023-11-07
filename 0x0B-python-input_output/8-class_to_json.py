#!/usr/bin/python3
# 8-class_to_json.py
""" Python"""
import sys


def class_to_json(obj):
    """ Convert a class to JSON format."""
    return obj.__dict__
