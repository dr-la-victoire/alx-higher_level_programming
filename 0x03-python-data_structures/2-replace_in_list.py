#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''This function replaaces an element in a list'''
    # Checking whether or not the idx is -ve
    if idx < 0:
        return (my_list)
    # Checking whether or not the list is out of range
    length = len(my_list) - 1
    if idx > length:
        return (my_list)
    # Replacing element in list
    my_list[idx] = element
    return (my_list)
