#!/usr/bin/python3
"""This script lists the 10 commits by someone from a repo"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()
        for res in results[:10]:
            print("{}: {}".format(res["sha"], res["author"]["login"]))
    else:
        print("IDK bro!")
