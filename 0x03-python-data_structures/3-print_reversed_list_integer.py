#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx = 0
    if my_list:
        my_list.reverse()
    while idx < len(my_list):
        print('{:d}'.format(my_list[idx]))
        idx = idx + 1
