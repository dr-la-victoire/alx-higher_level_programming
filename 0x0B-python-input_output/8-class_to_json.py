#!/usr/bin/python3
"""This module contains a function that returns the dict JSON serialization"""
import json


def class_to_json(obj):
    """Returns the dict repr of JSON serialization of an object"""
    return json.dumps(obj)
