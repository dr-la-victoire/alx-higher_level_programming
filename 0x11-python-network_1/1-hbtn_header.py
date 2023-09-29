#!/usr/bin/python3
"""This module displays the value of a response in the header of a URL"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.headers
for header, value in html.items():
    if header == "X-Request-Id":
        print("{}".format(value))
