#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10
string = "Last digit of"

if last_digit > 5 :
    print(f"{string:s} {number} is {last_digit:d} and is greater than 5\n")
elif last_digit == 0 :
    print(f"{string:s} {number} is {last_digit:d} and is 0\n")
elif last_digit < 6 and last_digit != 0 :
    print(f"{string:s} {number} is {last_digit:d} and is less than 6 and not 0\n")
