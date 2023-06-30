#!/usr/bin/python3
"""This module contains the text_indentation function"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after characters like
    '.', '?' and ':'

    Parameters:
    text: the text to be operated on. It must be a string

    Return:
    The newly formatted string

    Raises:
    TypeError if text provided is not a string
    """
    for i in text:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if i == '.' or i == '?' or i == ':':
            print("{}".format(i), end="")
            print("\n")
        else:
            print("{}".format(i), end="")
