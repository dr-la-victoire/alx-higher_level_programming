#!/usr/bin/python3
"""This module contains the geometry class"""


class BaseGeometry:
    """This class is the base class for geometry"""

    def area(self):
        """This method does nothing"""
        raise Exception("area() is not implemented")
