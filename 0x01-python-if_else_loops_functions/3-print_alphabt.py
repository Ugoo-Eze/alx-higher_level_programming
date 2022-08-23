#!/usr/bin/python3

number = 97

while number < 123:
    if number == 101 or number == 113:
        number += 1
        continue
    print("{:s}".format(chr(number)), end='')
    number += 1
