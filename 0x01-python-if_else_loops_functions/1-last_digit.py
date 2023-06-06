#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
# checking if number is -ve
if number < 0:
    number = number * -1
# printing the last digit
new_number = number % 10
if new_number > 5:
    print(f'Last digit of {number} is {new_number} and is greater than 5')
elif new_number < 6 and not 0:
    print(f'Last digit of {number} is {new_number} and is less than 6 and not 0')
elif new_number == 0:
    print(f'Last digit of {number} is {new_number} and is 0')
