#!/usr/bin/python3
def print_last_digit(number):
    '''This function prints the last digit of a number'''
    last = abs(number) % 10
    print("{}".format(last), end="")
