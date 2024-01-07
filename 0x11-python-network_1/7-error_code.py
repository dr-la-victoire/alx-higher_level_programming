#!/usr/bin/python3
"""This script prints the HTTP error codes"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    status = requests.get(url)
    if status.status_code >= 400:
        print("Error code: {}".format(status.status_code))
    else:
        print(status.text)
