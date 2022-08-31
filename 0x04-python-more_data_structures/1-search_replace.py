#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is not None:
        return([x if x != search else replace for x in my_list])
    return None


"""
def search_replace(my_list, search, replace):
    my_list_dup = my_list.copy

    for i in range(len(my_list)):
        my_list_dup[i] = replace if my_list[i] == search else my_list[i]
    return my_list_dup
"""

"""
def search_replace(my_list, search, replace):
    my_list_dup = my_list.copy()

    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list_dup[i] = replace
    return my_list_dup
"""
