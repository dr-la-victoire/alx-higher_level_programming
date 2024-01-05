#!/bin/bash
# Script that displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
