#!/usr/bin/python3
def remove_char_at(str, n):
    # creating a copy of the string
    new_str = str[:]
    # turning the string into a list
    list_string = list(new_str)
    if n < len(str) or n > len(str):
        return (new_str)
    # deleting the element at position n
    else:
        list_string.pop(n)
        # turning the list back to a string
        the_str = ''.join(list_string)
        # return the_str
        return (the_str)
