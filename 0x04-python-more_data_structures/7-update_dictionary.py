#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.setdefault(key, 0)
    a_dictionary[key] = value
    return a_dictionary