#!/usr/bin/python3
"""A special task"""


def add_attribute(mc, name, attr):
    """This function sets the attribute of an object"""
    #  if not hasattr(mc, "attr"):
        #  raise Exception("can't add new attribute")
    setattr(mc, name, attr)
