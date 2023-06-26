#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''This function that prints the first x elements of a list
    and only integers'''
    num = 0
    i = 0

    while i <= x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            num += 1
        except (ValueError, TypeError):
            continue
        print("")
        return (num)
