#!/usr/bin/python3
"""This module displays the value of a response in the header of a URL"""
import urllib.request
import sys

url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    html = response.headers
    header_dict = dict(html)
for header, value in header_dict.items():
    if header == "X-Request-Id":
        print("{}".format(value))
