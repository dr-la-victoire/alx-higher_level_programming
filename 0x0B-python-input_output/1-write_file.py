#!/usr/bin/python3
"""This module defines the function that writes to a file"""


def write_file(filename="", text=""):
    """Writes to a file and returns the number of chars written"""
    with open(filename, "w", encoding="utf-8") as the_file:
       chars = the_file.write(text)

    return chars
