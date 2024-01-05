#!/bin/bash
# Script that displays all the methods allowed by a URL
curl -sI "$1" | grep -i allow | awk -F ": " '{print $2}'
