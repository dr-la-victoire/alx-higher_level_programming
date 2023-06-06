#!/usr/bin/python3
def remove_char_at(str, n):
    # creating a copy of the string
    new_str = str[:]
    # turning the string into a list
    list_string = list(new_str)
    # deleting the element at position n
    if n >= 0:
        del list_string[n]
    # turning the list back to a string
    the_str = ''.join(list_string)
    print("{}".format(the_str))
