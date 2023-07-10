#!/usr/bin/python3
"""This module contains the class that inherits from list"""


class MyList(list):
    """This class inherits from the list class"""

    def print_sorted(self):
        """prints the list in sorted order"""
        print(sorted(self))
