#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    '''This function prints an integer'''
    try:
        print("{:d}".format(value), end="\n")
        return (True)
    except (ValueError, TypeError):
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return (False)
