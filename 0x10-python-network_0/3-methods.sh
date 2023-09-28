#!/bin/bash
# Displaying the methods allowed by a server
curl -sI "$1" | grep "allow" | sed 's/allow: //' | tail -n 1
