#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''This function that prints x elements of a list'''
    num = 0
    i = 0

    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
            num += 1
        except IndexError:
            return (num)
    print("")
    return (num)
