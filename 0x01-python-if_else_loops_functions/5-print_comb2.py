#!/usr/bin/python3

number = 0

#for number in range(100):

#    if number <= 9:
#        print("{:d} ".format(0), end='')
#        
#    print("{:02d}".format(number), end='')

while number <= 99:
    if number != 99:
        print("{:02d}, ".format(number), end='')
    else:
        print("{:02d}".format(number))
    number = number + 1
