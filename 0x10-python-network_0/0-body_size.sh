#!/bin/bash
# This script takes a UR and displays the body response size
curl -s "$1" | wc -c
