#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
no = number

if num < 0:
    num = num * -1

last_digit = num % 10

if last_digit > 5 and number < 0:
    last_digit *= -1
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is less than 6 and not 0")
elif last_digit > 5 and number > 0:
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
elif last_digit < 6 and last_digit != 0 and number < 0:
    last_digit *= -1
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is less than 6 and not 0")
elif last_digit < 6 and last_digit != 0 and number > 0:
    print(f"Last digit of {number:d} is {last_digit:d}"
          f" and is less than 6 and not 0")
