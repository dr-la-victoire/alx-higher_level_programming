#!/usr/bin/python3
def print_last_digit(number):
    '''This function prints the last digit of a number'''
    last = number % 10
    if number < 0:
        last = -last
    return last
