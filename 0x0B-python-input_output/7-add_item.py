#!/usr/bin/python3
"""This module adds all args to a Python list, and saves them to a file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# define an empty list and the JSON filename
args_list = []
file = 'add_items.json'

# get the python args
len_args = len(sys.argv)
counter = 1

# add them to the list
while counter < len_args:
    args_list.append(sys.argv[counter])

# convert the list to a json file
save_to_json_file(args_list, file)

# convert the json back to a python list
load_from_json_file(file)
