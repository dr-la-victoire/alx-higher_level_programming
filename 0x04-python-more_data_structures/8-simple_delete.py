#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''This function deletes a key from a dictionary'''
    # check if the key is in the dictionary
    if key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    else:
        return (a_dictionary)
