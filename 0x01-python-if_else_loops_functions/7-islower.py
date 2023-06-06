#!/usr/bin/python3
def islower(c):
    '''This function checks whether or not a letter  is lowercase'''
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
