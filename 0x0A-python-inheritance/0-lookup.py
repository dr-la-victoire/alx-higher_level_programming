#!/usr/bin/python3
"""This module contains the lookup function"""


def lookup(obj):
    """
    This function looks up an object
    It takes the object as parameter and returns
    a list containing the attributes and methods of the object
    """
    return dir(obj)
