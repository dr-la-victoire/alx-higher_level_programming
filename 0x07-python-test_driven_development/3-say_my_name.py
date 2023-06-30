#!/usr/bin/python3
"""This module contains the function that prints an individual's name"""


def say_my_name(first_name, last_name=""):
    """
    This functioin prints the name of a given person

    Parameters:
    first_name: the person's first name
    last_name: the person's last name (it has an empty string as a default)

    Return:
    A format string with the person's full name and a specialized message
    printed

    Raises Errors:
    Raises a TypeError if any of the parameters are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
