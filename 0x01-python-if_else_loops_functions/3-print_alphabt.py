#!/usr/bin/python3
# running a loop to print the alphabets
for char in range(97, 123):
    if char != 101 and char != 113:
        print("{}".format(chr(char)), end="")
