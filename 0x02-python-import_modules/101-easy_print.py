#!/usr/bin/python3
import os
words = "#pythoniscool\n"
os.write(1, words.encode())
