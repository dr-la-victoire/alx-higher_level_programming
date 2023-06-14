#!/usr/bin/python3
def best_score(a_dictionary):
    '''This function returns the dictionary key with the biggest score'''
    # declaring a variable 'biggest'
    biggest = 0
    # Looping through the dictionary
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            best = key
    return (best)
