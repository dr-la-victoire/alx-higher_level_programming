#!/usr/bin/python3
def no_c(my_string):
    '''This function removes all chars c and C from a string'''
    # Turning the string to a list
    the_list = list(my_string)
    # Looping through the string to find the char that is c or C
    for char in the_list:
        # Getting the index of C or c
        if char == 'C' or char == 'c':
            index = the_list.index(char)
            the_list.pop(index)
    # Converting the list back to a string
    new_string = ''.join(the_list)
    return (new_string)
