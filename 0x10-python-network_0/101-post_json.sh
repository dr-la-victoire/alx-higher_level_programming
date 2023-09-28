#!/bin/bash
# Sending the contents of a JSON file as POST request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
