#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element"""
    new_list = []
    for elements in my_list:
        if elements == search:
            my_list.append(replace)
        else:
            my_list.append(elements)
    return (my_list)
