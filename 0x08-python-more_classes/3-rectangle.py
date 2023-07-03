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

    def area(self):
        """This function returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This function returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """This function prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        the_rectangle = ""
        for height in range(self.__height):
            for width in range(self.__width):
                the_rectangle += "#"
            if height < self.__height - 1:
                the_rectangle += "\n"
        return (the_rectangle)
