#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''This function prints all the integers in a list in reverse order'''
    for reverse in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[reverse]))
