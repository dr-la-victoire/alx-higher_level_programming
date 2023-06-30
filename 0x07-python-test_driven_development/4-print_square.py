#!/usr/bin/python3
"""This module contains the function that prints a square"""


def print_square(size):
    """
    This function prints a square with the char '#'

    Parameters:
    size: the size of the square to be printed
    NOTE: size must be an integer

    Return:
    The printed square

    Raises:
    ValueError: if size less than 0
    TypeError: if size is not an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
