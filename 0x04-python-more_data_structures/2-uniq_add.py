#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''This function adds all unique integers in a list'''
    # Turning the list to a set
    set_list = set(my_list)
    # Setting the total to zero
    total = 0
    # Looping through the set
    for i in set_list:
        total += i
    return (total)
