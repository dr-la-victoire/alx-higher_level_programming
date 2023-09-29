#!/usr/bin/python3
"""This script fetches from a website"""
import requests

if __name__ == "__main__":
    info = requests.get("https://alx-intranet.hbtn.io/status")
    str_info = info.text
    print(
            "Body response:\n\t- type: {}\n\t- content: {}".format(
                str_info.__class__, str_info))
