#!/usr/bin/python3
"""This module contains the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """initialization of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implements the area"""
        area = self.__size * self.__size
        return area
