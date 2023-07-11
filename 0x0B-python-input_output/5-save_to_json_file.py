#!/usr/bin/python3
"""This module contains a function that saves data to a file in JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    """Saves JSON data to a file"""
    with open(filename, "w", encoding="utf-8") as the_json_file:
        json.dump(my_obj, the_json_file)
    the_json_file.close()
