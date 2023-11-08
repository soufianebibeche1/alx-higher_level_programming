#!/usr/bin/python3
# 10-student.py
""" Python """


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload the attributes from a JSON object."""
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """Return a string representation of a Student instance."""
        return "{} {} {}".format(self.first_name, self.last_name, self.age)
