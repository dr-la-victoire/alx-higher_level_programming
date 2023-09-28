#!/bin/bash
# Displays the body of response of a GET rewhest and sends a header varibale
curl -sH "X-School-User-Id: 98" "$1"
