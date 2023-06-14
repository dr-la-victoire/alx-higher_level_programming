#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''This function prints a dictionary in sorted order'''
    # turning the dictionary to a list of dictionary keys
    dict_list = list(a_dictionary.keys())
    # sorting the list of keys
    dict_list.sort()
    # printing the sorted list
    for keys in dict_list:
        print("{} : {}".format(keys, a_dictionary[keys]))
