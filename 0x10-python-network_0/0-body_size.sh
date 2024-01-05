#!/bin/bash
# This script sends a request to a URL and displays the response

curl -s "$1" | wc -c
