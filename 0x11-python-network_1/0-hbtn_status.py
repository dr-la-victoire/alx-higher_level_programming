#!/usr/bin/python3
"""This module fetches a particular website"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
print(
        "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 \
                content: {}".format(
                    html.__class__, html, html.decode("utf-8")))
