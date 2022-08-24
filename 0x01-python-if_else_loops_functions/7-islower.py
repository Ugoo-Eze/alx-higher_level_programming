#!/usr/bin/python3

"""
def islower(c):
    if (c >= chr(97) and c <= chr(122)):
        return True
    else:
        return False

"""


def islower(c):
    if (ord(c) >= ord('a') and ord(c) <= ord('z')):
        return True
    else:
        return False
