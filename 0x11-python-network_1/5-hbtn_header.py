#!/usr/bin/python3
"""This script gets the value of a header variable"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    info = requests.get(url)
    print("{}".format(info.headers["X-Request-Id"]))
