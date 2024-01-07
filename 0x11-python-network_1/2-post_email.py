#!/usr/bin/python3
"""This script sends a POST request to the URL with an email as a parameter"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {}
    data['email'] = sys.argv[2]

    # parsing the data
    url_values = urllib.parse.urlencode(data).encode('ascii')

    # creating the POST request
    request = urllib.request.Request(url, url_values)

    # displaying the body of the response
    with urllib.request.urlopen(request) as response:
        value = response.read()
    print(value.decode("utf-8"))
