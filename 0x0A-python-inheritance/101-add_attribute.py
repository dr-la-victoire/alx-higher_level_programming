#!/usr/bin/python3
"""A special task"""


def add_attribute(mc, name, attr):
    """This function sets the attribute of an object"""
    if not hasattr(mc, "__dict__"): #  cos obj has no __dict__ attr
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, name, attr)
