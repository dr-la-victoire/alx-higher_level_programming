#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''This function prints all the integers in a list in reverse order'''
    # list method to reverse the list
    my_list.reverse()
    # Looping to print the reversed list
    for reverse in my_list:
        print("{}".format(reverse))

