#!/usr/bin/python3
# running the loop
for char in range(97, 123):
    # checking for 'e' or 'q'
    if char == 101 or char == 113:
        continue
    print("{}".format(chr(char)), end="")
