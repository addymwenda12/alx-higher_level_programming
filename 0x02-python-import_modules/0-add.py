#!/usr/bin/python3

if __name__ == "__main__":
    def add(a, b):
        """Suming value from add_0.py"""
        from add_0 import add

        a = 1
        b = 2
        print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
