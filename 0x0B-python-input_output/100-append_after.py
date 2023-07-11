#!/usr/bin/python3
"""This module contains a function that appends after a specific text"""


def append_after(filename="", search_string="", new_string=""):
    """Appends after a specific line of text"""
    with open(filename, "a+", encoding="utf-8") as append:
        if append.read() == search_string:
            append.write(new_string)
    append.close()
