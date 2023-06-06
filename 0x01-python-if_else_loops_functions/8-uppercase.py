#!/usr/bin/python3
def uppercase(str):
    '''Converting a lowercase sentence to uppercase'''
    # check the lowercase chars in the sentence
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")

