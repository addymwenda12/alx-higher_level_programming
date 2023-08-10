#!/usr/bin/python3

def print_last_digit(number):
    # Ensure that the number is positive
    number = abs(number)

    # Get the last digit using modulo
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end="")

    # Return last digit
    return (last_digit)
