#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''This function returns a new dictionary with all the values
    multiplied by 2'''
    # creating the new dictionary
    new_dict = {}
    # loop through the old one
    for key, value in a_dictionary.items():
        # adding to the new dictionary
        new_dict[key] = value * 2
    return (new_dict)
