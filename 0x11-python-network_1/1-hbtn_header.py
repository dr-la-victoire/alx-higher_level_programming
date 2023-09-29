#!/usr/bin/python3
"""This module displays the value of a response in the header of a URL"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    html = response.headers
    header_dict = dict(html)
header_variable = header_dict.get("X-Request-Id")
print(header_variable)
