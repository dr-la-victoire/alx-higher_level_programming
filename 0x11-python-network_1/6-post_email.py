#!/usr/bin/python3
"""This module sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    info = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(info.text))
