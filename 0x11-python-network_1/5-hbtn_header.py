#!/usr/bin/python3
"""This script displays the value of a header variable of a URL"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = requests.get(url)
    print(value.headers.get('X-Request-Id'))
