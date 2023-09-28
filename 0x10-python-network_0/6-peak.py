#!/usr/bin/python3
"""This function finds the peak of a list of numbers"""


def find_peak(list_of_integers):
    """This function finds a peak jn thr list"""
    length = len(list_of_integers)
    if length == 0:
        return None
    else:
        peak = list_of_integers[0]
        for i in range(length):
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
    return peak
