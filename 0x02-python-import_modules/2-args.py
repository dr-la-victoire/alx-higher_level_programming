#!/usr/bin/python3
'''This program prints arguments passed as CL'''
# Importing the module that does this task
from sys import argv
# Condition to check the number of arguments
if len(argv) - 1 == 0:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) - 1 == 1:
    print("{} argument:".format(len(argv) - 1))
else:
    print("{} arguments:".format(len(argv) - 1))
# Loop to print the arguments
if len(argv) - 1 != 0:
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
