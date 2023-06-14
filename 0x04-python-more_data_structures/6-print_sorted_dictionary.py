#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''This function prints a dictionary in sorted order'''
    sorted_dictionary = dict(sorted(a_dictionary.items()))
    print(sorted_dictionary)
