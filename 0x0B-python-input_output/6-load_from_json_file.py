#!/usr/bin/python3
"""This module contains a function that creates an obj from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as obj_file:
        return json.load(obj_file)
