#!/usr/bin/python3
"""This script uses my GitHub credentials to display my ID"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    url = "https://api.github.com/users/{}".format(username)
    headers = {"Authorization": "Bearer {}".format(sys.argv[2])}

    # sending the get request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print("{}".format(result['id']))
    else:
        print("None")
