#!/usr/bin/python3

"""This module contains the function that adds two integers"""


def add_integer(a, b=98):
    """
    Returns the sum of two variables a and b

    Parameters:
    a (int): the firt number
    b (int): the second (with default value 98)
    NOTE: both a and b are typecasted into ints before operated on
    in case they are floats

    Return:
    int: the sum of the two numbers

    Raises Error:
    Raises TypeError if either a or b are not integers or floats

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
