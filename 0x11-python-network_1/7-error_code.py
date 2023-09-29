#!/usr/bin/python3
"""This module handles error codes with requests"""
import sys
import requests

if __name__ == "__main__":
    info = requests.get(sys.argv[1])
    code = info.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print("{}".format(info.text))
