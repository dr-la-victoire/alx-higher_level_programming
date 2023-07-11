#!/usr/bin/python3
import json
"""This module contains a function that changes string to JSON"""


def to_json_string(my_obj):
    """Returns the JSON representation of an obj string"""
    json_str = json.dumps(my_obj)

    return json_str
