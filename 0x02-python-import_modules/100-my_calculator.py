#!/usr/bin/python3
'''This program imports functions from a module to execute simple calculations
from the command line'''
# Importing the functions
from sys import argv, exit
from calculator_1 import add, sub, mul, div
# Adding the main guard
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    # Running a loop to get all the arguments
    if argv[2] == "+":
        print("{} + {} = {}".format(int(argv[1]), int(argv[3]), add(int(argv[1]), int(argv[3]))))
        exit(0)
    elif argv[2] == "-":
        print("{} - {} = {}".format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))
        exit(0)
    elif argv[2] == "*":
        print("{} * {} = {}".format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))
        exit(0)
    elif argv[2] == "/":
        print("{} / {} = {}".format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
