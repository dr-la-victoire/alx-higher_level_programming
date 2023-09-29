#!/usr/bin/python3
"""This module displays the value of a response in the header of a URL"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.headers
        header_dict = dict(html)
    for header, value in header_dict.items():
        if header == "X-Request-Id":
            print("{}".format(value))
