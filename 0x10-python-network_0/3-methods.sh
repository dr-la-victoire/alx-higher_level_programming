#!/bin/bash
# Displaying the methods allowed by a server
curl -sI "$1" | tail -n 1 | sed 's/allow: //'
