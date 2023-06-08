#!/usr/bin/python3
'''This program prints arguments passed as CL'''
# Importing the module that does this task
import sys
# Condition to check the number of arguments
if len(sys.argv) - 1 == 0:
    print("{} arguments.".format(len(sys.argv) - 1))
elif len(sys.argv) - 1 == 1:
    print("{} argument:".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
# Loop to print the arguments
if len(sys.argv) - 1 != 0:
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
