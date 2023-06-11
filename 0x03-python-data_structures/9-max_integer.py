#!/usr/bin/python3
def max_integer(my_list=[]):
    '''This function finds the biggest integer of a list.'''
    # Assuming the first number in the list is the biggest
    max = my_list[0]
    # Looping through the list and comparing them as we go
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return (max)
