#!/usr/bin/python3
"""This script sends a POST request to a URL with an email as param"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = requests.post(url, data={'email': email})

    # printing the response
    print(value.text)
