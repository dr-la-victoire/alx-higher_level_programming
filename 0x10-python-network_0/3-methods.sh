#!/bin/bash
# Displaying the methods allowed by a server
curl -sIX "$1" | grep -i "Allow" | sed 's/Allow: //i'
