#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''This function returns a new set with elements present in only one set'''
    return (set_2.symmetric_difference(set_1))
