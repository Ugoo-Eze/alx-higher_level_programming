#!/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        new_string = my_string.translate({ord('C') and ord('c'): None})
        return new_string
