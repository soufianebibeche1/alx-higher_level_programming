#!/usr/bin/python3
# models/base.py
""" Python: 0x0C. Python - Almost a circle """
import json


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = None

        instance.update(**dictionary)
        return instance
