#!/bin/bash
# This script sends a request to a URL and displays the response
curl -sI "$1" | grep -i content-length | awk '{print $2}'
