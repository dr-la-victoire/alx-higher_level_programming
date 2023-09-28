#!/bin/bash
# Displaying the methods allowed by a server
cd -sI | tail -n 1 | sed 's/allow: //'
