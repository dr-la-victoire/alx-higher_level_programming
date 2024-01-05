#!/bin/bash
# This script sends a request to a URL and displays the response

curl -s -w '%{size_download}\n' $1
