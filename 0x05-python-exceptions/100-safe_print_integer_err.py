#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''This function prints an integer'''
    try:
        print("{:d}".format(value), end="\n")
        return (True)
    except Exception as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return (False)
