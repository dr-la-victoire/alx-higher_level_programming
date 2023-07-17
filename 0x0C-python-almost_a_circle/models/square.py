#!/usr/bin/python3
"""This module contains a class that is a subclass of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    #  Adding the getter method
    @property
    def size(self):
        """Getter method for the size"""
        return self.__width

    #  Adding the setter method
    @size.setter
    def size(self, value):
        """Setter method for the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Assigning attributes to the square method"""
        flag = 0

        #  checking if args exists and is not empty
        if args is not None and len(args) != 0:
            for arg in args:
                if flag == 0:
                    if flag is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if flag == 1:
                    self.size = arg
                if flag == 2:
                    self.x = arg
                if flag == 3:
                    self.y = arg
                flag = flag + 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    value = self.id
                elif key == "size":
                    value = self.size
                elif key == "x":
                    value = self.x
                elif key == "y":
                    value = self.y

    def to_dictionary(self):
        """Return the dictionary representation of a square"""
        dictionary = {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}

        return dictionary
