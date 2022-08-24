#!/usr/bin/python3

number = 0

while number <= 99:
    if number != 99:
        print("{02:d}, ".format(number), end='')
    else:
        print("{02:d}".format(number))
    number = number + 1
