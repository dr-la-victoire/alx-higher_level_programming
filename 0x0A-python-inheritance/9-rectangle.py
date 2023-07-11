#!/usr/bin/python3
"""This module contains a class that inherits from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializing a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the shape"""
        area = self.__height * self.__width
        return area

    def __str__(self):
        """returns a rectangle description"""
        str_ = "[" + str(self.__class__.__name__) + "]"
        str_ += " " + str(self.__width) + "/" + str(self.__height)
        return str_
