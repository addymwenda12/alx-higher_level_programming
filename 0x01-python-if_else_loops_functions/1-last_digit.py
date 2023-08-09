#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit
# Build the output of the program
output = f"Last digit of {number:d} is {last_digit:d}"

if last_digit > 5:
    output += " and is greater than 5"

elif last_digit == 0:
    output += " and is 0"

else:
    output += " and is less than 6 and not 0"

# print the final output
print(output)
