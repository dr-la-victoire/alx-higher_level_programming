#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The initialization of the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                the_rectangle += str(self.print_symbol)
            if height < self.__height - 1:
                the_rectangle += "\n"
        return (the_rectangle)

    def __repr__(self):
        """This function returns a string representation of the rectangle"""
        return ("Rectangle.({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """This function is the garbage collector: for deleting an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 == area_2:
            return (rect_1)
        elif area_1 > area_2:
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new instances where a rectangle becomes a square"""
        height = size
        width = size
        return (Rectangle(height, width))
