#!/usr/bin/python3
"""This module contains a function that returns the obj str of a JSON repr"""
import json


def from_json_string(my_str):
    """returns the python string obj of a JSON repr"""
    json_str = json.loads(my_str)

    return json_str
