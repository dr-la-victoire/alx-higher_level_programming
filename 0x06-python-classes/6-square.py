#!/usr/bin/python3
"""This class defines a square with the size attribute

    The size attribute is a private instance attribute
    It has a default value of 0 if nothing has been provided
"""


class Square:
    """Defines a class with an attribute size"""
    def __init__(self, position, size=0):
        """The initialization of the class"""
        self._position = position
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self._size = size

    @property
    def position(self):
        """This method is the getter to retrieve the position"""
        return (self._position)

    @position.setter
    def position(self, value):
        """This method is the setter to set the value of the position"""
        if value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        """This method calculates the area of a square"""
        return (self._size * self._size)

    @property
    def size(self):
        """This method is the getter method to retrieve the size"""
        return (self._size)

    @size.setter
    def size(self, value):
        """This method is the setter method to set the size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def my_print(self):
        """This method prints the square with char #"""
        if self._size < 0:
            raise ValueError("size must be >= 0")
        elif self._size > 0:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end="")
                print()
        else:
            print("")
