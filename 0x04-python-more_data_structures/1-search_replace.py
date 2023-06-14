#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''This function replaces all occurrences of an element by another
    in a new list'''
    # create a new list
    new_list = my_list.copy()
    # loop through the old one to find and replace
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list.remove(search)
            new_list.insert(i, replace)
    return (new_list)
