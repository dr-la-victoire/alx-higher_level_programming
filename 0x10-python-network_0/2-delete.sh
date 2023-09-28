#!/bin/bash
# Sending a delete request
curl -s "$1" -X DELETE | wc -c
