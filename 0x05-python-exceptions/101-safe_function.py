#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    '''This function executes a function safely'''
    try:
        result = fct(*args)
        return (result)
    except Exception as m:  # using a variable to access error details
        print("Exception: {}".format(m), file=sys.stderr)  # printing to stderr
        return (None)
