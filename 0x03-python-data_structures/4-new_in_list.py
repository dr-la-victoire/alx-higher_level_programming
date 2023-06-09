#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''This function replaces an element in a list at a specific position
    without modifying the orignal list'''
    # Creating a copy of the list
    new = my_list.copy()
    if idx < 0:
        return (new)
    length = len(new)
    if idx > length:
        return (new)
    # Replacing the element at the index
    new[idx] = element
    return (new)
