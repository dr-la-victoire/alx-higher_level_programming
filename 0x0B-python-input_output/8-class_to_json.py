#!/usr/bin/python3
"""This module contains a function that returns the dict JSON serialization"""


def class_to_json(obj):
    """Returns the dict repr of JSON serialization of a data structure"""
    return obj.__dict__
