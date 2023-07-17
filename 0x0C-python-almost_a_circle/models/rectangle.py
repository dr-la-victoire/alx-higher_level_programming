#!/usr/bin/python3
"""This module contains a class that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the display of a rectangle to stdout"""
        for y in range(self.y):
            print("")
        for collumn in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for rows in range(self.__width):
                print("#", end="")
            print()

    def __repr__(self):
        """overrides the __str__ method to return something special"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        flag = 0

        if args and len(args) != 0:  # because args returns a tuple
            for arg in args:
                if flag == 0:
                    if flag is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif flag == 1:
                    self.width = arg
                elif flag == 2:
                    self.height = arg
                elif flag == 3:
                    self.x = arg
                elif flag == 4:
                    self.y = arg
                flag = flag + 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():  # because kwargs returns a dict
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height. self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        dictionary = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}

        return dictionary
