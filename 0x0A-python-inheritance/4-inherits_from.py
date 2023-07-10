#!/usr/bin/python3
"""This module contains a special function"""


def inherits_from(obj, a_class):
    """
    This function checks whether or not an object is an instance of a class
    that directly inherited from a specified class
    It takes the object and the class as parameters
    It rerturns True or False depending
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
