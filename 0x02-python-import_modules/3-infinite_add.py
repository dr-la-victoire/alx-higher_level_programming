#!/usr/bin/python3
'''This program adds all the arguments passed to it via the command line'''
# Importing the module that would do the job
from sys import argv
if __name__ == "__main__":
    add = 0
    cum = 0
    # Looping thriugh the arguments
    while add < (len(argv) - 1):
        cum += int(argv[add + 1])
        add = add + 1
    print("{}".format(cum))
