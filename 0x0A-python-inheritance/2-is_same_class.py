#!/usr/bin/python3
"""This module contains a special function"""


def is_same_class(obj, a_class):
    """
    This function checks whether or not an object is an instance
    of a specified class
    It takes the object and class as parameters
    It returns True if the object is an instance of the class
    or False otherwise
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
