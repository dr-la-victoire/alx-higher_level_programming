#!/usr/bin/python3
"""This module fetches a particular website"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()
