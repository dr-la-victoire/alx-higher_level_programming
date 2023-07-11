#!/usr/bin/python3
"""This module contains the class Student"""


class Student:
    """Defines a student"""


    def __init__(self, first_name, last_name, age):
        """Initializing the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict repr of a Student instance"""
        return self.__dict__
