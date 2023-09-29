#!/usr/bin/python3
"""This script sends a POST request with an email as parameter"""
import urllib.request
import sys
import urllib.parse

url = sys.argv[1]
values = {"email": sys.argv[2]}
data = urllib.parse.urlencode(values)
encoded_data = data.encode("ascii")
info = urllib.request.Request(url, encoded_data)
with urllib.request.urlopen(info) as response:
    html = response.read()
print("{}".format(html.decode("utf-8")))
