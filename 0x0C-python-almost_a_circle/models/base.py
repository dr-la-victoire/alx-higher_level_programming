#!/usr/bin/python3
"""This is a special module"""
import json


class Base:
    """This class defines the almost a circle class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The function to initialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr of the dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string repr to a file"""
        the_file = cls.__name__ + ".json"
        with open(the_file, "w", encoding="utf-8") as newfile:
            if list_objs is None:
                the_file.write("[]")
            else:
                #  getting a list of dict repr of the list_objs
                dict_repr = [dic.to_dictionary() for dic in list_objs]
                newfile.write(Base.to_json_string(dict_repr))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return list(json.loads(json_string))
