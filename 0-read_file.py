#!/usr/bin/python3
"""This module contains the function that reads from a text file"""


def read_file(filename=""):
    """Prints the contents of the file to stdout"""
    with open(filename, "r", encoding="utf-8") as the_file:
        for lines in the_file:
            print("{}".format(lines), end="")
        the_file.close()
