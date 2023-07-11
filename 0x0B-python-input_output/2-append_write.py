#!/usr/bin/python3
"""This module contains the function that appends to a file"""


def append_write(filename="", text=""):
    """Appends to a file and returns the number of chars appended"""
    with open(filename, "a", encoding="utf-8") as the_file:
        chars = the_file.write(text)

    return chars
