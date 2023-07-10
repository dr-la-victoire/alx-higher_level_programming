#!/usr/bin/python3
"""This module contains a special function"""


def is_kind_of_class(obj, a_class):
    """
    This function checks whether an object is an instance of a class
    or an instance of another object that inherited from the class
    It takes the object and class as parameter
    It returns True or False depending on the results
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
