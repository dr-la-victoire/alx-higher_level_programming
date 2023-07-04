#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''This function deletes keys with a specific value in a dictionary'''
    for key, value in a_dictionary.items():
        if value == value:
            del a_dictionary[key]
    return (a_dictionary)
