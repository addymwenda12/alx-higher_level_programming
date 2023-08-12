#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # Exclude the script name from the argument
    argv = sys.argv[1:] 

    # Convert the arguments to integers
    integers = [int(arg) for arg in argv]

    result = sum(integers)
    print(result)
