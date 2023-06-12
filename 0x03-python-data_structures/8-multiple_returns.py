#!/usr/bin/python3
def multiple_returns(sentence):
    '''This function returns a tuple with the length of a string
    and its first character'''
    # Getting the length of sentence
    length = len(sentence)
    if length == 0:
        tuple_s = length, None
        return (tuple_s)
    else:
        first_char = sentence[0]
        tuple_d = length, first_char
        return (tuple_d)
