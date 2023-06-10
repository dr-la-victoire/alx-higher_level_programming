#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''This function prints all the integers in a list'''
    # Looping through the list
    for k in range(len(my_list)):
        print("{:d}".format(my_list[k]))
