#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        return None

    while idx <= len(my_list):
        idx = idx + 1
        return idx