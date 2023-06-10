#!/usr/bin/python3
def element_at(my_list, idx):
    '''This function retrieves an element from a list'''
    # Checking whether or not idx is -ve
    if idx < 0:
        return (None)
    # Assigning the range of the list
    length = len(my_list) - 1
    # Checking whether or not idx is out of range
    if idx > length:
        return (None)
    # Retrieving the element
    element = my_list.pop(idx)
    return (element)
