#!/usr/bin/python3
# 9-student.py
""" Python """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student"""
        return self.__dict__
