#!/usr/bin/python3
# running a loop
for i in range(97, 123):
    # checking for e or q
    if i == 101 or i == 113:
        continue
    print('{}'.format(chr(i)), end="")
