#!/bin/bash
# Script that displays only the status code
curl -sw "%{http_code}" "$1"
