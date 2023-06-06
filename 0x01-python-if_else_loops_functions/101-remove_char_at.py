#!/usr/bin/python3
def remove_char_at(str, n):
    '''This function removes the char of a string at position n'''
    # creating a copy of the str
    new_str = str[:]
    for position in new_str:
        if position == n:
            new_str.replace(position, "")
    print("{}".format(new_str))
