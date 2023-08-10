#!/usr/bin/python3

for ch in range(122, 96, -1):
    if ch % 2 == 1:
        print("{}".format(chr(ch - 32)), end="")
    else:
        print("{}".format(chr(ch)), end="")
