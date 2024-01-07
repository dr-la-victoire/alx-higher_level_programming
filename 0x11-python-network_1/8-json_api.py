#!/usr/bin/python3
"""This script sends a letter as a POST request to a URL"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    default_value = ""

    if len(sys.argv) == 1:
        payload = {'q': default_value}
    else:
        payload = {'q': sys.argv[1]}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        try:
            result = response.json()

            if not result:
                print("No result")
            else:
                print("[{}] {}".format(result['id'], result['name']))
        except json.JSONDecodeError:
            print("Not a valid JSON")
