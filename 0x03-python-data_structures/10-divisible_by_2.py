#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''This function finds all multiples of 2 in a list'''
    new_list = []
    # Looping through the list
    for i in range(len(my_list)):
        # Checking if an element in the list is divisible by 2
        if my_list[i] % 2 == 0:
            # Appending 'True' to new_list
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
