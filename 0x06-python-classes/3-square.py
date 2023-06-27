#!/usr/bin/python3
"""This class defines a square with the size attribute

    The size attribute is a private instance attribute
    It has a default value of 0 if nothing has been provided
"""


class Square:
    """Defines a class with an attribute size"""
    def __init__(self, size=0):
        """The initialization of the class"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self._size = size

    def area(self):
        """This method calculates the area of a square"""
        return (self._size * self._size)
