#!/usr/bin/python3
"""This script displays the value of a variable in the header"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        header_var = header.get('X-Request-Id')
    print(header_var)
