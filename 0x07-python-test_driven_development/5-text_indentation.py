#!/usr/bin/python3
"""This module contains the text indentation function"""


def text_indentation(text):
    """
    This function indents the text whenever it encounters some special characters

    Parameters:
    text: the string of text that is to be indented

    Return:
    A new text with the indented characters

    Raises:
    TypeError: if the text is not a string
    """
    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a str")

    while i < len(text) and text[i] == " ":
        i = i + 1

    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == '\n' or text[i] in "?.:":
            if text[i] in "?.:":
                print('\n')
            i = i + 1
            while i < len(text) and text[i] == " ":
                i = i + 1
            continue
        i = i + 1
