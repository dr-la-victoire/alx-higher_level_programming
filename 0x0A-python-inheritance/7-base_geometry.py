#!/usr/bin/python3
"""This module contains the geometry class"""


class BaseGeometry:
    """This class is the base class for geometry"""

    def area(self):
        """This method does nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
