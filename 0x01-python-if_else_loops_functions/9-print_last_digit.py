#!/usr/bin/python3

def print_last_digit(number):
    num = number
    if num < 0:
        num = num * -1
    last_digit = num % 10
    print("{}".format(last_digit), end='')
    return last_digit
