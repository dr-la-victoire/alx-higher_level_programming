#!/usr/bin/python3
"""This module handles errors woth urllib"""
import urllib.request
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print(html.decode("utf-8"))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
