#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
# printing the last digit
new = abs(number) % 10
# checking if the number is -ve
if number < 0:
    new = -new
if new_number > 5:
    print(f'Last digit of {number} is {new} and is greater than 5')
elif new_number < 6 and new_number != 0:
    print(f'Last digit of {number} is {new} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {new} and is 0')
