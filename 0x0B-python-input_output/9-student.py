#!/usr/bin/python3
# 9-student.py
""" Python """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        """ json json """
        return self.__dict__
