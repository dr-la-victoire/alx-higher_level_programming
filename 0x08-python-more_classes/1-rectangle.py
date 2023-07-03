#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """The initialization of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter property to retrieve the width"""
        return (self.__width)

    @property
    def height(self):
        """The getter property to retrieve the height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """The setter property to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """The setter property to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
