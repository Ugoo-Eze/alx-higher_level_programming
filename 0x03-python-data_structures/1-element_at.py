#!/usr/bin/python3

def element_at(my_list, idx):
    
    while idx <= len(my_list):
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            idx = idx + 1
            return idx
